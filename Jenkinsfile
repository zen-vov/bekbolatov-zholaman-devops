pipeline {
  agent any
  options { skipDefaultCheckout(true); disableConcurrentBuilds(); timeout(time: 15, unit: 'MINUTES') }
  environment {
    STUDENT_NAME = 'Zholaman'
    STUDENT_SURNAME = 'Bekbolatov'
    STUDENT_GROUP = 'IT2-2314'
    STUDENT_ID = '37614'
    IMAGE = 'bekbolatov-zholaman-devops'
    CONTAINER = 'bekbolatov-zholaman-container'
  }
  stages {
    stage('Checkout') { steps { checkout scm; sh 'git rev-parse HEAD; printf "Student: %s %s\\nGroup: %s\\nStudent ID: %s\\n" "$STUDENT_NAME" "$STUDENT_SURNAME" "$STUDENT_GROUP" "$STUDENT_ID"' } }
    stage('Build') { steps { dir('bekbolatov_zholaman/app') { sh 'npm ci && npm run build' } } }
    stage('Test') { steps { dir('bekbolatov_zholaman/app') { sh 'npm test' } } }
    stage('Docker Build') { steps { sh 'docker build -t "$IMAGE:$BUILD_NUMBER" -t "$IMAGE:latest" .' } }
    stage('Docker Run') { steps { sh '''
      set -eu
      # Replace only this lab's container, and only when it carries our label.
      if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
        test "$(docker inspect -f '{{index .Config.Labels "devops.student"}}' "$CONTAINER")" = 37614
        docker rm -f "$CONTAINER"
      fi
      docker run -d --name "$CONTAINER" --label devops.student=37614 -p 127.0.0.1:37614:3000 \
        -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID "$IMAGE:$BUILD_NUMBER"
      for attempt in $(seq 1 30); do
        if docker exec "$CONTAINER" node -e "fetch('http://127.0.0.1:3000/health').then(r=>r.json()).then(j=>{if(j.status!=='ok'||j.student.id!==process.env.STUDENT_ID)process.exit(1)})"; then break; fi
        sleep 1
      done
      docker exec "$CONTAINER" node -e "fetch('http://127.0.0.1:3000/health').then(r=>r.json()).then(j=>{if(j.status!=='ok'||j.student.id!==process.env.STUDENT_ID)process.exit(1);console.log(j)})"
      docker logs "$CONTAINER"
      docker ps --filter name="$CONTAINER"
    ''' } }
  }
}
