var Express = require('express');
var App = Express();
var bodyParser = require('body-parser');

require('./routes')(App);

App.use(bodyParser.urlencoded());
App.use(Express.static(__dirname + '/public'));
App.listen(function() {
  console.log('Server up!')
});
