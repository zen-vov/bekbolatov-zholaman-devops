#!/usr/bin/env bash
set -euxo pipefail
docker images bekbolatov-zholaman-devops
docker run -d --name bekbolatov-zholaman-container --label devops.student=37614 -p 127.0.0.1:37614:3000 -e STUDENT_NAME=Zholaman -e STUDENT_SURNAME=Bekbolatov -e STUDENT_GROUP=IT2-2314 -e STUDENT_ID=37614 bekbolatov-zholaman-devops
sleep 2
docker ps
docker ps -a
docker exec bekbolatov-zholaman-container node -e "fetch('http://localhost:3000/health').then(r=>r.json()).then(j=>{require('node:assert/strict').deepEqual(j.student,{name:'Zholaman',surname:'Bekbolatov',group:'IT2-2314',id:'37614',course:'DevOps'});console.log(j)})"
docker logs bekbolatov-zholaman-container
docker stop bekbolatov-zholaman-container
docker start bekbolatov-zholaman-container
sleep 1
docker exec bekbolatov-zholaman-container node -e "fetch('http://localhost:3000').then(r=>{if(!r.ok)process.exit(1)})"
docker stop bekbolatov-zholaman-container
docker rm bekbolatov-zholaman-container
docker run --rm -e STUDENT_NAME=Override -e STUDENT_SURNAME=Verified -e STUDENT_GROUP=TEST -e STUDENT_ID=42 bekbolatov-zholaman-devops node -e "const s=require('./server').student();require('node:assert/strict').deepEqual(s,{name:'Override',surname:'Verified',group:'TEST',id:'42',course:'DevOps'});console.log(s)"
docker compose up -d --wait
docker compose ps
docker exec bekbolatov-zholaman-container node -e "fetch('http://localhost:3000/health').then(r=>r.json()).then(j=>{if(j.student.id!=='37614')process.exit(1);console.log(j)})"
docker compose down
