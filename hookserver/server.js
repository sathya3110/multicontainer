var http = require('http');
var express = require('express');
var app = express();
var fs = require("fs");
var sys = require('sys');
var util = require('util'),
    exec = require('child_process').exec,
    child;
 
 
app.use(express.bodyParser());
 
app.post('/downloadimage', function(req, res) {
    var object = req.body;
    console.log('body is: ' + JSON.stringify(req.body));
    child = exec('$HOME/dockerpull.sh', // command line argument directly in string
           function (error, stdout, stderr) {      // one easy function to capture data/errors
           console.log('stdout: ' + stdout);
           console.log('stderr: ' + stderr);
           if (error !== null) {
             console.log('exec error: ' + error);
           }
    });
    res.send(201, 'ok');
});
 
var server = http.createServer(app).listen(8081, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)
})

