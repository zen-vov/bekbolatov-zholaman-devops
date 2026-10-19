FROM docker:28-cli AS dockercli
FROM node:22-bookworm-slim AS node
FROM jenkins/jenkins:lts-jdk21
USER root
COPY --from=dockercli /usr/local/bin/docker /usr/local/bin/docker
COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm
RUN jenkins-plugin-cli --plugins workflow-aggregator git pipeline-stage-view
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/
USER jenkins
