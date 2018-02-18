const express = require('express');
const fs = require('fs');
const app = express();
const bodyParser = require('body-parser');
const exec = require('child_process').exec;

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());
app.listen(8080);

// index.html hosting
app.get('/', (req,res) => {
  fs.readFile('index.html', (err, data) => {
    res.type('text/html');
    res.send(data);
  });
});

// python exec
app.post('/post',(req,res) => {
  let b64s = req.body['test'];
  console.log('post sended');
  exec('python main.py ' + b64s, (err,stdout) => {
    console.log(stdout);
    if (err !== null) console.log(err);
    res.type('text/plain');
    res.send(stdout);
  });
});
