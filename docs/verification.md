# Real verification results

Date: 2026-10-19. Student: Zholaman Bekbolatov / IT2-2314 / 37614.

- Ubuntu 24.04 Linux demonstration: exit 0; all commands and both file-check branches executed (evidence/linux.txt).
- Node syntax build: exit 0. Node test runner: 3 passed, 0 failed; HTTP requests and environment override assertions performed (evidence/node.txt).
- Git: real implementation commits, development change and merge; origin main/development successfully pushed. Public repo confirmed by GitHub API (evidence/github-repository.json).
- Ignore rules verified with git check-ignore; password file not tracked (evidence/gitignore.txt).
- Docker image build: exit 0 (evidence/docker-build.txt). Container default environment checked via HTTP; all four overrides separately asserted. Stop/start/recheck/rm completed (evidence/docker-lifecycle.txt).
- Compose up --wait, health check and down: exit 0 (same lifecycle evidence).
- Jenkins build #1: SUCCESS. Actual source commit: `efb9022f72dfb62cddeef82a1997a9ff71212734`. GitHub HTTPS checkout succeeded (evidence/jenkins-console.txt).
- Jenkins stage API: Checkout, Build, Test, Docker Build, Docker Run all SUCCESS (evidence/jenkins-stages.json).
- Console ends with `Finished: SUCCESS`. The Docker Run stage verifies /health and student ID in the running container before success.
- Final app container health: inspect evidence/container-state.json; image/container listing evidence/docker-images.txt and evidence/docker-running.txt.

## Evidence integrity

Evidence .txt files contain real command output; none is an invented terminal transcript. linux.txt and git-history.txt screenshots display those actual text files in a local browser, not a terminal emulator. Jenkins and application screenshots are captured from their running HTTP interfaces using a real Chromium browser. PDF includes the actual screenshots. Screenshots may show private localhost URLs, which the instructor must reproduce locally.

## Remaining submission work

Record the continuous personal video with your own voice; review it and submit its link, GitHub URL and PDF. Keep Docker Desktop running for live demonstrations. Jenkins login is zholaman; read password privately from ignored jenkins/secrets/admin_password. Never submit that password file.

## Operational limits

This is a local educational Jenkins with authenticated access, localhost binding and Docker socket access. Source commit verified by Jenkins precedes later report/evidence commits; those later commits only add documentation and evidence. Pipeline can be rerun on latest main from Build Now. No webhook was required; builds start manually. No video was fabricated or recorded in the student’s voice.

PDF report: 9 pages, Times New Roman, rendered and visually reviewed. Full report generation source: docs/build-report.py. Screenshot capture used the Playwright CLI against live services.
