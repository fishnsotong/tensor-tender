var db = require('./database');

module.exports = function(app) {
  app.get('/', function(req, res) {
    res.sendFile(__dirname + '/views/main.html');
  });
};
