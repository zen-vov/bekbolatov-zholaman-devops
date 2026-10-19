# Commands for demonstration

Run from the repository root unless specified. These commands change only this lab's containers. Keep Jenkins and app Compose stacks separate.

## Linux (Tasks 1–5)

```bash
docker run --rm -it -v "$PWD/bekbolatov_zholaman:/root/devops/bekbolatov_zholaman" -w /root/devops/bekbolatov_zholaman ubuntu:24.04 bash
bash scripts/linux-demo.sh
./scripts/Bekbolatov_Zholaman_system.sh
```

For a live process view, run `top`, then press q. `pwd` prints current directory; `ls` lists entries; `cd` changes directory; `mkdir` creates directories; `touch` creates an empty file; `cp` copies; `mv` moves/renames; `rm` deletes; `cat` prints all contents; `head`/`tail` print first/last lines. The demo removes only its temporary moved.txt file.

## Git (Tasks 6–10)

```bash
git status
git config --global user.name
git config --global user.email
git config user.name
git config user.email
git log --oneline --graph --all
git branch -v
git show --summary --format=fuller HEAD
git check-ignore -v bekbolatov_zholaman/logs/application.log bekbolatov_zholaman/backup/example .env
git remote -v
git ls-remote origin refs/heads/main refs/heads/development
```

The original repository was already initialized; its history starts with the actual implementation. No existing history was removed. `.gitignore` keeps logs, backups, dependencies and local secrets out of version control; it does not remove files already tracked.

## Node and Docker (Tasks 11–15)

```bash
npm ci --prefix bekbolatov_zholaman/app
npm run build --prefix bekbolatov_zholaman/app
npm test --prefix bekbolatov_zholaman/app
cat Dockerfile
docker images bekbolatov-zholaman-devops
docker ps --filter name=bekbolatov-zholaman-container
docker logs bekbolatov-zholaman-container
docker exec bekbolatov-zholaman-container printenv STUDENT_NAME STUDENT_SURNAME STUDENT_GROUP STUDENT_ID
curl http://localhost:37614/
curl http://localhost:37614/health
docker stop bekbolatov-zholaman-container
docker start bekbolatov-zholaman-container
```

For Compose demonstration after showing the Jenkins-created container:

```bash
docker stop bekbolatov-zholaman-container
docker rm bekbolatov-zholaman-container
docker compose up -d --wait
docker compose ps
docker compose down
```

Then run the Jenkins job again to restore its deployment. Before manually removing a container check its name and ownership label. See evidence/docker-lifecycle.txt for the executed run commands including all environment variables and override verification.

## Jenkins (Tasks 16–21)

```bash
# First installation only: create a local password without committing it.
mkdir -p jenkins/secrets
# If the file is absent, generate a strong random password into admin_password.
python3 -c 'import secrets,pathlib; p=pathlib.Path("jenkins/secrets/admin_password"); p.exists() or p.write_text(secrets.token_urlsafe(24)); p.chmod(0o600)'
docker compose -f jenkins/docker-compose.yml up -d --build
```

Open http://localhost:18080, sign in as zholaman using the local password file. Open Bekbolatov_Zholaman_DevOps → Build Now → latest build → Console Output. Show all five stages, commit hash and Finished: SUCCESS. Job configuration uses Pipeline script from SCM, GitHub HTTPS, main, Jenkinsfile. The repository must remain public or Jenkins credentials must be configured for private access.

Stop Jenkins without deleting its volume:

```bash
docker compose -f jenkins/docker-compose.yml down
```
