FROM node:22-bookworm-slim
WORKDIR /app
COPY bekbolatov_zholaman/app/package*.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY bekbolatov_zholaman/app/ ./
ENV NODE_ENV=production PORT=3000
EXPOSE 3000
USER node
HEALTHCHECK --interval=5s --timeout=3s --start-period=5s CMD node -e "fetch('http://127.0.0.1:3000/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
CMD ["node", "server.js"]
