// Demo localStorage persistence test; run: node tests/persistence_test.cjs
const fs = require('fs'), vm = require('vm'), assert = require('assert'), path = require('path');
const code = fs.readFileSync(path.join(__dirname, '..', 'app.js'), 'utf8');
const storage = new Map();
const localStorage = {getItem: k => storage.get(k) || null, setItem: (k,v) => storage.set(k,v)};
function start() {
  const handlers = {};
  const elements = {'app': {innerHTML: ''}, 'modal-root': {innerHTML: ''}, 'toast-root': {append: () => {}}};
  const document = {
    getElementById: id => elements[id],
    body: {style: {}},
    addEventListener: (type, cb) => {handlers[type] = cb;},
    createElement: () => ({remove: () => {}})
  };
  const window = {addEventListener: () => {}, scrollTo: () => {}};
  const sandbox = {document, window, localStorage, navigator: {}, location: {protocol: 'file:'}, console, setTimeout: () => {}, structuredClone, Intl, Date};
  vm.runInNewContext(code, sandbox, {filename: 'app.js'});
  return {elements, click: (action, id) => handlers.click({
    target: {closest: () => ({dataset: {action, id}, closest: () => null})},
    preventDefault: () => {}
  })};
}
const first = start();
assert(first.elements.app.innerHTML.includes('Посмотреть рабочее демо'));
first.click('start-demo');
first.click('visit', '0');
assert(storage.has('viamitest_demo_v2'));
assert(JSON.parse(storage.get('viamitest_demo_v2')).visited.includes('myportugal:0'));
const second = start();
assert(second.elements.app.innerHTML.includes('Путешественник'));
assert(!second.elements.app.innerHTML.includes('Посмотреть рабочее демо'));
console.log('PASS: profile and visited location are persisted');
