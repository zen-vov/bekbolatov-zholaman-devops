# Continuous video demonstration (about 16 minutes)

Record your actual screen and your own voice in one continuous video. Read and understand the files first. The automated setup does not replace your explanation or video.

| Time | Demonstration and explanation |
|---|---|
| 00:00–00:40 | Show Name Zholaman, Surname Bekbolatov, Group IT2-2314, Student ID 37614, Course DevOps. |
| 00:40–03:40 | Open Ubuntu using commands.md. Show pwd, ls, project folders, student file; demonstrate cp/mv/rm on the demo file. Run find, grep ERROR/WARNING, count errors, tail. Show permissions and explain owner/group/others and r/w/x. |
| 03:40–05:00 | Run the system Bash script; explain file check. Show ps aux and top, identify PID, owner, CPU/memory, exit top with q. |
| 05:00–07:00 | Show git status, identity, graph with 5+ commits and merge, development/main. Show .gitignore and check-ignore. Open the actual GitHub repository and source files. Explain push/pull and branches. |
| 07:00–09:40 | Explain Dockerfile FROM/WORKDIR/COPY/RUN/EXPOSE/CMD. Show image, running container, root and health URLs, environment variables and logs. Explain image versus container and why configuration belongs in environment. |
| 09:40–11:00 | Show stop/start; remove only lab container, run Compose up --wait, inspect result, Compose down. Explain how Compose saves run configuration. |
| 11:00–14:40 | Open Jenkins, show exact job name and GitHub SCM settings. Trigger Build Now. Show five stages and Console Output, student variables, actual Git commit, tests and Docker build/run. Show Finished: SUCCESS and deployed container. |
| 14:40–16:00 | Explain Linux → Git → GitHub → Jenkins → tests → Docker. Explain failed-stage behavior. Show PDF and conclude. |

Before recording: start Docker and Jenkins, check microphone and screen capture, open browser tabs, ensure no passwords/tokens are visible. Login before recording. After recording, review the video, check sound, upload it to the instructor-approved location and submit its link together with GitHub and PDF.

Preparation questions: explain chmod 755; find a file; grep ERROR; git pull vs push; WORKDIR; image vs container; Docker logs; why ignore backups and .env; what happens when Test or Docker Build fails; how to change one environment variable and rerun.
