var db = require('./database');
var pythonComm = require('python-comm');


module.exports = function(app) {
  app.get('/', function(req, res) {
    res.sendFile(__dirname + '/views/main.html');
  });
  app.POST('/brew', function(req, res) {
    console.log(JSON.stringify(req.body))
  });
};
