const http = require('node:http');
function student(env = process.env) {
  return {name: env.STUDENT_NAME || 'Zholaman', surname: env.STUDENT_SURNAME || 'Bekbolatov', group: env.STUDENT_GROUP || 'IT2-2314', id: env.STUDENT_ID || '37614', course: 'DevOps'};
}
function message(s) {
  return `================================\nDevOps Student Application\n================================\nName: ${s.name}\nSurname: ${s.surname}\nGroup: ${s.group}\nStudent ID: ${s.id}\nCourse: ${s.course}\nApplication is running successfully!\n`;
}
function createServer(env = process.env) {
  return http.createServer((req, res) => {
    if (req.url === '/health') {res.writeHead(200, {'Content-Type':'application/json'}); res.end(JSON.stringify({status:'ok', student:student(env)}));}
    else if (req.url === '/') {res.writeHead(200, {'Content-Type':'text/plain; charset=utf-8'}); res.end(message(student(env)));}
    else {res.writeHead(404); res.end('Not found\n');}
  });
}
if (require.main === module) {
  const server = createServer();
  server.listen(Number(process.env.PORT || 3000), '0.0.0.0', () => console.log(message(student())));
  for (const signal of ['SIGTERM','SIGINT']) process.on(signal, () => server.close());
}
module.exports = {student, message, createServer};
