const {test} = require('node:test');
const assert = require('node:assert/strict');
const {student, createServer} = require('./server');

test('personalized defaults', () => {
  assert.deepEqual(student({}), {
    name: 'Zholaman', surname: 'Bekbolatov', group: 'IT2-2314', id: '37614', course: 'DevOps',
  });
});

test('all four environment overrides', () => {
  const env = {STUDENT_NAME: 'Test', STUDENT_SURNAME: 'Student', STUDENT_GROUP: 'G1', STUDENT_ID: '42'};
  assert.deepEqual(student(env), {
    name: 'Test', surname: 'Student', group: 'G1', id: '42', course: 'DevOps',
  });
});

test('HTTP root, health and unknown route', async () => {
  const server = createServer({STUDENT_ID: '42'});
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  try {
    const base = `http://127.0.0.1:${server.address().port}`;
    const root = await fetch(base);
    assert.equal(root.status, 200);
    assert.match(await root.text(), /Student ID: 42/);

    const health = await fetch(base + '/health');
    assert.equal(health.status, 200);
    assert.equal((await health.json()).student.id, '42');
    assert.equal((await fetch(base + '/missing')).status, 404);
  } finally {
    await new Promise(resolve => server.close(resolve));
  }
});
