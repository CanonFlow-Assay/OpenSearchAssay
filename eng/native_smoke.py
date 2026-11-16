"""Real OpenSearch API cases on an isolated disposable container."""
import json
from pathlib import Path
from native_common import call,container,ready

IMAGE='opensearchproject/opensearch:3.9.0@sha256:3bf4fe26aeb9f7b03c0ebcb1302bb24e855ee6b89fd926d26a71a83ef6f7e076'
ROOT=Path(__file__).resolve().parents[1]


def run():
    cases=[]
    with container(IMAGE,['--env','discovery.type=single-node','--env','DISABLE_INSTALL_DEMO_CONFIG=true','--env','DISABLE_SECURITY_PLUGIN=true','--env','OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m']) as (name,identity):
        def request(method,path,body=None,ndjson=False):
            command=['docker','exec','-i',name,'curl','--silent','--show-error','--max-time','10','-w','\n%{http_code}','-X',method,'http://127.0.0.1:9200'+path]
            if body is not None:command+=['-H','Content-Type: '+('application/x-ndjson' if ndjson else 'application/json'),'--data-binary','@-']
            text=call(command,body if isinstance(body,str) else json.dumps(body) if body is not None else None)
            value,status=text.rsplit('\n',1);return int(status),json.loads(value)
        def probe():
            status,value=request('GET','/')
            if status!=200:raise RuntimeError('engine not ready')
            return value
        server=ready(probe);assert server['version']['number']=='3.9.0';cases.append('exact engine version')
        mapping={'settings':{'number_of_shards':1,'number_of_replicas':0},'mappings':{'dynamic':'strict','properties':{'quantity':{'type':'integer'},'name':{'type':'keyword'}}}}
        status,_=request('PUT','/orders',mapping);assert status==200;cases.append('explicit mapping created')
        payload='\n'.join([json.dumps({'index':{'_index':'orders','_id':'good'}}),json.dumps({'quantity':2,'name':'one'}),json.dumps({'index':{'_index':'orders','_id':'bad'}}),json.dumps({'quantity':'not-an-integer','name':'two'}),''])
        assert len(payload.encode())<=5242880
        status,bulk=request('POST','/_bulk?refresh=wait_for',payload,True)
        assert status==200 and bulk['errors'] is True
        statuses=[item['index']['status'] for item in bulk['items']];assert statuses==[201,400];cases.append('HTTP success retains per-item failure')
        status,count=request('GET','/orders/_count');assert status==200 and count['count']==1;cases.append('rejected item not indexed')
        status,_=request('PUT','/orders/_doc/good?refresh=wait_for',{'quantity':3,'name':'updated'});assert status==200
        _,count=request('GET','/orders/_count');assert count['count']==1;cases.append('stable ID update preserves cardinality')
        status,_=request('PUT','/orders/_doc/other',{'quantity':1,'name':'one','unexpected':True});assert status==400;cases.append('strict mapping rejects unknown field')
        status,_=request('POST','/_aliases',{'actions':[{'add':{'index':'orders','alias':'current-orders'}}]});assert status==200
        _,count=request('GET','/current-orders/_count');assert count['count']==1;cases.append('alias resolves reviewed index')
        status,values=request('GET','/orders/_settings?include_defaults=true&flat_settings=true');assert status==200
        settings=values['orders']['settings'];defaults=values['orders']['defaults']
        snapshot={'schemaVersion':1,'product':'opensearch','version':'3.9.0','settings':{'plugins.security.disabled':True},'indices':[{'name':'orders','number_of_shards':int(settings['index.number_of_shards']),'number_of_replicas':int(settings['index.number_of_replicas']),'mapping_total_fields_limit':int(defaults['index.mapping.total_fields.limit'])}], 'bulk':{'inspectItemErrors':True,'maxBytes':5242880,'maxItems':1000,'maxAttempts':4}}
        out=ROOT/'artifacts';out.mkdir(exist_ok=True)
        (out/'native-snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
        return {'status':'Pass','engineVersion':server['version']['number'],'imageDigests':identity,'cases':cases,
                'expectedSnapshotVerdict':'Fail','limits':'Private no-network disposable test disables security and replicas intentionally. API semantics passed; production TLS, DLS/FLS, HA, snapshots/restore and load behavior remain unqualified.'}


if __name__=='__main__':
    result=run();(ROOT/'artifacts/native-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
