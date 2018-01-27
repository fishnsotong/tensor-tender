var db = require('./database');
var getFlavours = require('./getFlavours');
var pythonComm = require('./python-comm');

module.exports = function(app) {
  app.get('/', function(req, res) {
    res.sendFile(__dirname + '/views/main.html');
  });

  app.post('/brew', function(req, res) {
    console.log(req.body);
    var dish = JSON.stringify(req.body.dishes);
    console.log(getFlavours.getIngredientFlavours(dish));
  });
};
