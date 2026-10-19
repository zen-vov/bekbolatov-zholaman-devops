#!/usr/bin/env python3
"""Trigger authenticated Jenkins build and retain actual API/console evidence."""
import base64,json,pathlib,time,urllib.request,urllib.error
root=pathlib.Path(__file__).resolve().parent.parent
base='http://127.0.0.1:18080'
password=(root/'jenkins/secrets/admin_password').read_text().strip()
auth='Basic '+base64.b64encode(('zholaman:'+password).encode()).decode()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
def req(path,data=None,headers=None):
 return opener.open(urllib.request.Request(base+path,data=data,headers={'Authorization':auth,**(headers or {})}),timeout=25)
for n in range(60):
 try:
  crumb=json.load(req('/crumbIssuer/api/json'));break
 except Exception:
  time.sleep(2)
else: raise SystemExit('Jenkins not ready')
job='/job/Bekbolatov_Zholaman_DevOps/'
response=req(job+'build',b'',{crumb['crumbRequestField']:crumb['crumb']})
queue=response.headers['Location'].replace(base,'').replace('http://localhost:18080','')
for n in range(90):
 q=json.load(req(queue+'api/json'))
 if 'executable' in q: number=q['executable']['number'];break
 time.sleep(2)
else: raise SystemExit('Queue timeout')
print('Build',number,flush=True)
for n in range(300):
 build=json.load(req(job+str(number)+'/api/json'))
 if not build['building']: break
 time.sleep(2)
else: raise SystemExit('Build timeout')
evidence=root/'docs/evidence'
evidence.mkdir(exist_ok=True)
(evidence/'jenkins-build.json').write_text(json.dumps(build,indent=2))
(evidence/'jenkins-console.txt').write_bytes(req(job+str(number)+'/consoleText').read())
try: (evidence/'jenkins-stages.json').write_bytes(req(job+str(number)+'/wfapi/describe').read())
except urllib.error.HTTPError: pass
print('Result:',build['result'])
if build['result']!='SUCCESS':
 print((evidence/'jenkins-console.txt').read_text()[-7000:]);raise SystemExit(1)
