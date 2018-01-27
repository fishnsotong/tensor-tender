var Express = require('express');
var App = Express();
var bodyParser = require('body-parser');

App.use(bodyParser.urlencoded());
App.use(Express.static(__dirname + '/public'));

require('./routes')(App);

App.listen(3000, function() {
  console.log('Server up!')
});
