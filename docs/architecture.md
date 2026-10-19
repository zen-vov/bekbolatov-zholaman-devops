# Integrated DevOps Workflow

Zholaman Bekbolatov · IT2-2314 · Student ID 37614 · DevOps

Linux → project files → Git commits → GitHub main → Jenkins Checkout → Build → Test → Docker Build → Docker Run → SUCCESS.

Linux provides the filesystem, executable permissions, Bash and process tools. On macOS this laboratory uses a real Ubuntu 24.04 container; its home contains `/root/devops/bekbolatov_zholaman`. Host project sources are mounted there for the Linux demonstration.

Git records changes and merges the development branch into main. GitHub hosts the shared repository so Jenkins can fetch a specific version and the instructor can review the history. `git push` sends local commits; `git pull` fetches and integrates remote changes. Branches allow independent changes before merging.

Jenkins reads the Jenkinsfile from GitHub main, checks out the actual commit, validates Node syntax, runs HTTP tests, builds a versioned image and deploys the container. Each command must return zero. If a stage fails, subsequent normal stages are skipped and the build fails. A failed Test stage therefore prevents Docker Build and Docker Run. There is no automatic rollback: an earlier running container may remain; a failed replacement can require rerunning the corrected pipeline.

The image is an immutable application template containing Node and source files. A container is a running instance with its own process and environment. WORKDIR sets the directory used by subsequent build instructions and the application command. EXPOSE documents the internal port; the run/Compose port mapping makes it accessible on localhost:37614. The HTTP server keeps the application running and handles SIGTERM gracefully.

Environment variables configure the same image for different deployments. They must not contain secrets baked into the image or committed to Git. Jenkins displays the four required student variables. The Node tests check defaults, all four overrides, HTTP content, health and 404 behavior.

Compose describes repeatable container configuration, ports and environment in one YAML file. The app Compose stack is separate from the Jenkins stack.

Local Jenkins: http://localhost:18080, username `zholaman`; password is in ignored `jenkins/secrets/admin_password`. This local educational Jenkins runs as root with the Docker socket mounted so it can use the host daemon. This is a privileged local setup; port binding is limited to 127.0.0.1 and authentication is enabled. Do not expose it on a public host.

Permissions: r=read, w=write, x=execute. The first permission triplet is owner, second group, third others. private.txt is 600 (owner read/write); public.txt is 644 (owner read/write and everyone read). Script mode 755 allows the owner to modify it and everyone to read/execute. Git stores executable status, not full Unix modes; run linux-demo.sh to restore the private/public modes after cloning.

A process is a running program. PID identifies a process. `ps` is a snapshot; `top` refreshes live information (the evidence uses one batch iteration). Linux evidence contains PID, owner, CPU and memory columns.

Official references consulted: [Jenkins Docker installation](https://www.jenkins.io/doc/book/installing/docker/), [Jenkins Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax/).
