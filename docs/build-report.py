#!/usr/bin/env python3
"""Generate academic PDF from actual saved verification data and screenshots."""
from pathlib import Path
import json,html
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
root=Path(__file__).resolve().parent.parent
out=root/'output/pdf/Bekbolatov_Zholaman_DevOps_Report.pdf'
out.parent.mkdir(parents=True,exist_ok=True)
font=Path('/System/Library/Fonts/Supplemental')
pdfmetrics.registerFont(TTFont('TNR',str(font/'Times New Roman.ttf')))
pdfmetrics.registerFont(TTFont('TNRB',str(font/'Times New Roman Bold.ttf')))
W,H=A4
c=canvas.Canvas(str(out),pagesize=A4)
c.setTitle('DevOps Laboratory - Zholaman Bekbolatov - 37614');c.setAuthor('Zholaman Bekbolatov')
page=0;y=0
style=ParagraphStyle('body',fontName='TNR',fontSize=11,leading=15,spaceAfter=8)
def start(title):
 global page,y
 if page:c.showPage()
 page+=1;y=H-60
 c.setFont('TNR',9);c.drawString(50,H-28,'DevOps | Zholaman Bekbolatov | IT2-2314 | 37614')
 c.line(50,H-35,W-50,H-35)
 c.setFont('TNR',9);c.drawCentredString(W/2,28,str(page))
 c.setFont('TNRB',18);c.drawString(50,y,title);y-=30
def para(text):
 global y
 p=Paragraph(html.escape(text),style);_,h=p.wrap(W-100,H);p.drawOn(c,50,y-h);y-=h+10
 assert y>45, ('text overflow',page,y)
def shot(file,caption,maxh=380):
 global y
 p=root/'docs/screenshots'/file
 if not p.exists():para('MISSING SCREENSHOT: '+caption);return
 im=ImageReader(str(p));iw,ih=im.getSize();scale=min((W-100)/iw,maxh/ih)
 w,h=iw*scale,ih*scale
 c.drawImage(im,50,y-h,width=w,height=h);y-=h+10
 st=ParagraphStyle('caption',parent=style,fontSize=9,leading=11)
 a=Paragraph(html.escape(caption),st);_,h=a.wrap(W-100,H);a.drawOn(c,50,y-h);y-=h+16
 assert y>40,('image overflow',page,y)
def code(text):
 global y
 c.setFont('Courier',8)
 for line in text.splitlines():
  while len(line)>94:
   c.drawString(50,y,line[:94]);y-=11;line=line[94:]
  c.drawString(50,y,line);y-=11
 y-=8
b=json.loads((root/'docs/evidence/jenkins-build.json').read_text())
sha=next(a['lastBuiltRevision']['SHA1'] for a in b['actions'] if 'lastBuiltRevision' in a)
start('Laboratory Work 1')
para('DevOps Fundamentals: Linux, Git, Docker and Jenkins')
y-=40
for s in ['Name: Zholaman','Surname: Bekbolatov','Group: IT2-2314','Student ID: 37614','Course: DevOps','Date: 19 October 2026']:para(s)
y-=35
para('Repository: https://github.com/zen-vov/bekbolatov-zholaman-devops')
para('Requirements source: Devops_Task_6week.docx. All 21 technical tasks were implemented and verified against actual command output and a successful Jenkins build. The student must separately record and submit the continuous personal video with their own voice.')
para('Report contents: Linux; Git & GitHub; Docker; Jenkins; Integrated Workflow; final task checklist; conclusion and submission requirements.')
start('1. Linux - Tasks 1-5')
para('The Linux demonstration ran successfully in Ubuntu 24.04. Sources were mounted at /root/devops/bekbolatov_zholaman, preserving the required ~/devops/surname_name layout. Required app, scripts, config, logs and backup folders and personalized files were created.')
para('linux-demo.sh executed pwd, ls, cd, mkdir, touch, cp, mv, rm, cat, head and tail. A ten-line sample log was searched with find and grep. Exactly two ERROR and two WARNING messages were present; the last five lines were displayed.')
para('private.txt was set to 600, public.txt to 644 and the Bash script to 755. The script printed identity and system data with whoami, hostname, date, uname, df and free. Both existing-file and missing-file branches were checked. ps, ps aux and top exposed PID, owner, CPU and memory.')
shot('linux-evidence.png','Figure 1. Browser display of the actual Ubuntu command log (not an emulated terminal).',340)
para('Full evidence: docs/evidence/linux.txt. Permission bits mean read, write and execute for owner, group and others; private notes allow only owner access, while public notes allow everyone to read.')
start('2. Git & GitHub - Tasks 6-10')
para('The existing repository was reused. Git identity was checked; actual implementation was recorded in meaningful commits. The development branch introduced Jenkins automation and was merged into main with a merge commit. Both branches were pushed to the existing origin; no force push or history deletion was performed.')
para('The .gitignore excludes *.log, backup/, .env, node_modules and local Jenkins secrets. git check-ignore verified the rules. The public GitHub repository was verified through its API, and Jenkins subsequently checked out its main branch over HTTPS.')
shot('git-history.png','Figure 2. Actual git log --oneline --graph --all output viewed in the browser.',300)
para('Evidence: docs/evidence/git-history.txt, gitignore.txt, github-refs.txt, github-repository.json and git-identity.txt. Git preserves history; GitHub makes the versioned repository accessible to Jenkins and the instructor.')
start('3. Docker - Tasks 11-15')
para('The Dockerfile uses FROM, WORKDIR, COPY, RUN, EXPOSE and CMD. The dependency-free Node HTTP server displays personal information at / and provides /health. It runs as the node user, stays alive to serve requests, and closes gracefully on SIGTERM.')
para('A real image was built. The required container was started with all four student variables and verified through HTTP. A separate container execution asserted overrides of all four variables. docker logs, stop, start, exec and rm succeeded. Compose up --wait, application verification and Compose down succeeded.')
shot('application.png','Figure 3. Personal information returned by the running Docker application at localhost:37614.',290)
para('Evidence: docs/evidence/docker-build.txt, docker-lifecycle.txt and container-state.json. The final container state is running and healthy. An image is the reusable template; a container is its running instance. Environment variables configure a deployment without changing the image.')
start('4. Jenkins - Tasks 16-19')
para('Jenkins was deployed in its own Docker Compose stack at localhost:18080. Pipeline, Git and Stage View plugins were installed. An authenticated account and the exact job Bekbolatov_Zholaman_DevOps were configured. Local credentials are kept in an ignored file.')
para('The job uses Pipeline script from SCM with the public GitHub repository, main branch and Jenkinsfile. Jenkins has Node/npm and Docker CLI. The local educational controller accesses the host Docker socket; its web port is bound to localhost.')
shot('jenkins-dashboard.png','Figure 4. Running Jenkins Dashboard with the personalized job.',360)
para('The Jenkinsfile sets STUDENT_NAME, STUDENT_SURNAME, STUDENT_GROUP and STUDENT_ID. Console Output displays Zholaman Bekbolatov, IT2-2314 and 37614. The Docker Run stage passes these variables to the container and validates health and student ID.')
start('5. Pipeline stages - Tasks 17-20')
para('Build #1 completed successfully. The stage API independently records SUCCESS for Checkout, Build, Test, Docker Build and Docker Run. The Node test runner passed all three tests, including real HTTP requests and all four environment overrides.')
shot('jenkins-stages.png','Figure 5. Real Jenkins Stage View: all five required stages are green.',370)
para('Verified source commit: '+sha)
para('The source commit is the implementation merge. Later commits add documentation and evidence. The running application image is tagged bekbolatov-zholaman-devops:1 and latest. Evidence: jenkins-build.json, jenkins-stages.json, jenkins-console.txt and docker-running.txt.')
start('6. Successful execution - Task 20')
shot('jenkins-success.png','Figure 6. Actual Console Output: student data, Docker deployment and Finished: SUCCESS.',420)
para('No local-source fallback was used: Jenkins first retrieved the Jenkinsfile from GitHub and then checked out the same repository in Checkout. The health request in Docker Run returned the configured student ID. The final container is healthy according to docker inspect.')
para('All screenshots in this report were captured from a live Chromium browser. Text-log screenshots show the actual saved outputs, not recreated terminal graphics. Original images are in docs/screenshots; full outputs are in docs/evidence.')
start('7. Integrated Workflow - Task 21')
para('Linux creates and manages the project files and scripts. Git records the project changes. GitHub hosts the repository. Jenkins obtains the Jenkinsfile and a specific source revision from GitHub, builds and tests the application, creates its Docker image, and starts the container. The health check connects the successful build with a functioning application.')
code('Linux -> Project -> Git -> GitHub -> Jenkins\n          Checkout -> Build -> Test -> Docker Build -> Docker Run\n          HTTP health verification -> Finished: SUCCESS')
para('Linux provides shell and process tools; Git provides reproducible history; GitHub shares the source; Jenkins automates the ordered steps; Docker packages and executes the application. Compose describes reusable deployment configuration.')
para('A failing stage stops the normal stages that follow and marks the build as failed. For example, a failed Test stage prevents building or running a new image. This simple pipeline does not promise automatic rollback; earlier deployments can remain or require correction and rerunning.')
para('Demonstration instructions and command explanations: docs/commands.md. Detailed workflow and permission explanations: docs/architecture.md. Continuous 10-20 minute recording plan: docs/video-guide.md.')
para('Official references: Jenkins Docker installation - https://www.jenkins.io/doc/book/installing/docker/ ; Jenkins Pipeline syntax - https://www.jenkins.io/doc/book/pipeline/syntax/.')
start('8. Final checklist and conclusion')
rows=json.loads((root/'docs/task-status.json').read_text())
for r in rows:
 c.setFont('TNR',10);c.drawString(50,y,f"{r['task']:2}. {r['title']}");c.setFont('TNRB',10);c.drawRightString(W-50,y,r['status']);y-=19
para('All 21 technical tasks passed real verification. This does not constitute a guaranteed grade: the DOCX separately assesses repository organization, individual understanding and the personal video. The assessment totals 100 points, including 5 for video.')
para('Submission still required: record one continuous screen video with your own voice, review its sound and content, and submit its link together with the GitHub repository URL and this PDF. No missing technical screenshots remain.')
para('Keep Docker Desktop running for the live demonstration. Jenkins login: zholaman; read the password privately from jenkins/secrets/admin_password. Do not submit passwords or browser session artifacts.')
c.save();print(out)
