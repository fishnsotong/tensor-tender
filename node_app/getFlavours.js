var csv = require('csv-parser');
var fs = require('fs');

var dishIngredients = require('./data/dishIngredients.json');

var flavourArray = ["Alcoholic beverage", "Animal product", "cereal/crop", "Dairy", "fish/seafood", "Flower", "Fruit", "Herb", "Meat", "Nut/seed", "Plant", "Plant derivative", "Spice", "Vegetable"];

var getIngredientFlavours = function(dish) {
  var ingredientFlavours = [];
  var stream = csv(['ingredient', 'flavour']);
  fs.createReadStream('data/ingredientFlavours.csv')
    .pipe(stream)
    .on('data', function (data, err) {
      ingredientFlavours.push(data);
    }); //parses ingredientFlavours data from csv
  var flavourProfile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (i=0; i < dishIngredients.dishes.length; i++) { //check what dish was selected
    var dishNameCheck = JSON.stringify(dishIngredients.dishes[i].name);
    var dishIngredientsCheck = JSON.stringify(dishIngredients.dishes[i].ingredients);
    console.log("Check 2: " + ingredientFlavours);
    console.log('Checking ' + dishNameCheck);
    if (dish == dishNameCheck) {
      for (i=0; i < dishIngredientsCheck.length; i++) { //loop through each ingredient
        var flavourIndex = findFlavour(dishIngredientsCheck[i], ingredientFlavours)
        flavourProfile[flavourIndex] += 1
      };
    };
  };
  return flavourProfile
};

function findFlavour(ingredient, ingredientFlavours) {
  var flavourIndex;
  for (i=0; i < ingredientFlavours.length; i++) {
    if (ingredient == ingredientFlavours[i].ingredient) {
      for (i=0; i<flavourArray.length; i++) {
        if (ingredientFlavours[i].flavour == flavourArray[i]) {
          flavourIndex = i
        };
      };
    };
  };
  return flavourIndex;
};

module.exports = {
  getIngredientFlavours: getIngredientFlavours
}
