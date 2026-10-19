# DevOps laboratory — Zholaman Bekbolatov

Student ID **37614** · Group **IT2-2314** · Course **DevOps**

Source requirements: `Devops_Task_6week.docx` (21 tasks). Application sources and Linux project: `bekbolatov_zholaman/`.

```bash
npm ci --prefix bekbolatov_zholaman/app
npm test --prefix bekbolatov_zholaman/app
docker compose up -d --wait
```

Application: http://localhost:37614, health: `/health`. Run `docker compose down` before deploying with Jenkins because the required container name is shared.

Jenkins: `docker compose -f jenkins/docker-compose.yml up -d --build`; first create the ignored local password as described in [commands](docs/commands.md). Open http://localhost:18080. Job: **Bekbolatov_Zholaman_DevOps**.

- [Implementation and task checklist](docs/implementation.md)
- [Executed verification results](docs/verification.md)
- [Reproduction commands](docs/commands.md)
- [Architecture and explanations](docs/architecture.md)
- [Video script](docs/video-guide.md)
- [PDF report](output/pdf/Bekbolatov_Zholaman_DevOps_Report.pdf)

Runtime `logs/`, `backup/`, `.env` and Jenkins password are ignored. Linux demonstration recreates the sample application log. All evidence in docs/evidence is actual command output; screenshots show live browser pages. Personal video with your own voice remains a student submission requirement.
