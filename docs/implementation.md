# Implementation and final task checklist

Source: Devops_Task_6week.docx, read in full. Student: Zholaman Bekbolatov, IT2-2314, ID 37614. All PASS statuses refer to implemented and actually verified technical tasks, not to completion of the student voice/video submission.

| Task | Requirement | Status | Evidence |
|---|---|---|---|
| 1 | Project Environment | PASS | bekbolatov_zholaman/; docs/evidence/linux.txt |
| 2 | Search and File Processing | PASS | docs/evidence/linux.txt; scripts/linux-demo.sh |
| 3 | File Permissions | PASS | docs/evidence/linux.txt |
| 4 | Bash Script | PASS | scripts/Bekbolatov_Zholaman_system.sh; docs/evidence/linux.txt |
| 5 | Processes | PASS | docs/evidence/linux.txt |
| 6 | Git Repository | PASS | docs/evidence/git-identity.txt; .git/ |
| 7 | Meaningful Commit History | PASS | docs/evidence/git-history.txt |
| 8 | .gitignore | PASS |  .gitignore; docs/evidence/gitignore.txt |
| 9 | Branching and Merge | PASS | docs/evidence/git-history.txt; docs/evidence/github-refs.txt |
| 10 | GitHub | PASS | https://github.com/zen-vov/bekbolatov-zholaman-devops |
| 11 | Dockerfile | PASS | Dockerfile; docs/evidence/docker-build.txt |
| 12 | Build and Run Container | PASS | docs/evidence/docker-build.txt; docs/evidence/docker-lifecycle.txt |
| 13 | Environment Variables | PASS | docs/evidence/docker-lifecycle.txt; app/server.test.js |
| 14 | Container Management | PASS | docs/evidence/docker-lifecycle.txt |
| 15 | Docker Compose | PASS | docker-compose.yml; docs/evidence/docker-lifecycle.txt |
| 16 | Jenkins Job | PASS | jenkins/init.groovy.d/setup.groovy; docs/screenshots/jenkins-dashboard.png |
| 17 | Jenkinsfile | PASS | Jenkinsfile; docs/evidence/jenkins-stages.json |
| 18 | Jenkins + GitHub | PASS | docs/evidence/jenkins-console.txt |
| 19 | Jenkins Environment Variables | PASS | Jenkinsfile; docs/evidence/jenkins-console.txt |
| 20 | Successful Pipeline | PASS | docs/evidence/jenkins-build.json; docs/evidence/jenkins-console.txt |
| 21 | Complete DevOps Workflow | PASS | docs/architecture.md; docs/evidence/jenkins-console.txt |

## Task 1. Project Environment

Required app/scripts/config/logs/backup folders and student info created; pwd, ls, cd, mkdir, touch, cp, mv, rm, cat, head and tail executed in Ubuntu.

Evidence: bekbolatov_zholaman/; docs/evidence/linux.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 2. Search and File Processing

Ten log lines; find, grep ERROR/WARNING, ERROR count=2 and last five lines verified. Runtime log is intentionally ignored and recreated by demo.

Evidence: docs/evidence/linux.txt; scripts/linux-demo.sh. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 3. File Permissions

chmod 600 private.txt, 644 public.txt, executable Bash script; actual ls -l output saved.

Evidence: docs/evidence/linux.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 4. Bash Script

Student/system information, whoami/hostname/date/uname/df/free; both exists and missing branches executed.

Evidence: scripts/Bekbolatov_Zholaman_system.sh; docs/evidence/linux.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 5. Processes

ps, ps aux, top batch output; PID, USER, CPU and memory columns captured.

Evidence: docs/evidence/linux.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 6. Git Repository

Existing initialized repository used; identity checked; status saved. Existing user identity preserved.

Evidence: docs/evidence/git-identity.txt; .git/. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 7. Meaningful Commit History

Five meaningful implementation commits plus Jenkins development commit, merge and final documentation commits.

Evidence: docs/evidence/git-history.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 8. .gitignore

*.log, backup/, .env ignored; check-ignore confirms matching rules; local Jenkins secret also ignored.

Evidence:  .gitignore; docs/evidence/gitignore.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 9. Branching and Merge

development introduced real Jenkins implementation, then --no-ff merged into main; both branches pushed.

Evidence: docs/evidence/git-history.txt; docs/evidence/github-refs.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 10. GitHub

Existing origin used, normal push succeeded; public repository verified through GitHub API; HTTPS checkout succeeded in Jenkins.

Evidence: https://github.com/zen-vov/bekbolatov-zholaman-devops. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 11. Dockerfile

FROM, WORKDIR, COPY, RUN, EXPOSE and CMD; app runs as node user; real image build completed.

Evidence: Dockerfile; docs/evidence/docker-build.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 12. Build and Run Container

Image built, named container started, docker images/ps/ps -a executed, HTTP health checked.

Evidence: docs/evidence/docker-build.txt; docs/evidence/docker-lifecycle.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 13. Environment Variables

All four student variables checked inside real container; separate image execution verified overrides for all four.

Evidence: docs/evidence/docker-lifecycle.txt; app/server.test.js. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 14. Container Management

docker logs, stop, start, exec and rm all succeeded; restarted application checked.

Evidence: docs/evidence/docker-lifecycle.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 15. Docker Compose

compose up -d --wait, running service/health check, compose down completed.

Evidence: docker-compose.yml; docs/evidence/docker-lifecycle.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 16. Jenkins Job

Bekbolatov_Zholaman_DevOps job created with GitHub SCM; Jenkins installed in dedicated local container.

Evidence: jenkins/init.groovy.d/setup.groovy; docs/screenshots/jenkins-dashboard.png. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 17. Jenkinsfile

Checkout, Build, Test, Docker Build, Docker Run: actual stage API shows SUCCESS for each.

Evidence: Jenkinsfile; docs/evidence/jenkins-stages.json. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 18. Jenkins + GitHub

Jenkins obtained Jenkinsfile and checked out GitHub main over HTTPS; built, tested, built image and ran container.

Evidence: docs/evidence/jenkins-console.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 19. Jenkins Environment Variables

Console shows Student: Zholaman Bekbolatov, Group: IT2-2314, Student ID: 37614; passed to Docker.

Evidence: Jenkinsfile; docs/evidence/jenkins-console.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 20. Successful Pipeline

Build #1 SUCCESS; five stages SUCCESS; screenshots Dashboard/stages/console captured; source SHA preserved.

Evidence: docs/evidence/jenkins-build.json; docs/evidence/jenkins-console.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Task 21. Complete DevOps Workflow

Linux project → Git/GitHub → Jenkins Checkout/Build/Test → Docker Build/Run demonstrated successfully. Personal continuous video still must be recorded by student.

Evidence: docs/architecture.md; docs/evidence/jenkins-console.txt. Paths beginning scripts/ or app/ are inside bekbolatov_zholaman/.

## Submission and grading notes

The DOCX requires three submission items: accessible GitHub repository, PDF with screenshots, and one continuous screen recording with the student’s own voice (recommended 10–20 minutes). A recorded personal video is not generated by this project. Follow video-guide.md and submit the link.

The assessment table allocates Linux 25, Git & GitHub 25, Docker 25, Jenkins 20, Video 5 = 100 points. Individual task point labels differ from that aggregate: do not infer a guaranteed grade by adding task labels. Repository organization and oral understanding are also assessed. The instructor may ask an individual command or explanation.

The original repository already existed; git init was not repeated unnecessarily. Linux home path requirements are fulfilled inside the Ubuntu environment, avoiding host system changes. Logs and backup content are runtime artifacts excluded as required.
