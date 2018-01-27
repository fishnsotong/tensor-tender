var csv = require('csv-parser');
var fs = require('fs');

var dishIngredients = require('./data/dishIngredients.json');
var ingredientFlavours = require('./data/ingredientFlavours.json');

var flavourArray = ["Alcoholic beverage", "Animal product", "cereal/crop", "Dairy", "fish/seafood", "Flower", "Fruit", "Herb", "Meat", "Nut/seed", "Plant", "Plant derivative", "Spice", "Vegetable"];

var getIngredientFlavours = function(dish) {
  var flavourProfile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (i=0; i < dishIngredients.dishes.length; i++) { //check what dish was selected
    var dishNameCheck = JSON.stringify(dishIngredients.dishes[i].name);
    var dishIngredientsCheck = dishIngredients.dishes[i].ingredients;
    console.log('Checking ' + dishNameCheck);
    if (dish == dishNameCheck) {
      console.log(dish + " matches " + dishNameCheck);
      console.log(dishIngredientsCheck[1]);
      for (i=0; i < dishIngredientsCheck.length; i++) { //loop through each ingredient
        console.log('Checking ' + dishIngredientsCheck[i]);
        var flavourIndex = findFlavour(dishIngredientsCheck[i], ingredientFlavours)
        flavourProfile[flavourIndex] += 1
      };
    };
  };
  return flavourProfile
};

function findFlavour(ingredient, ingredientFlavours) {
  var flavourIndex;
  ingredientFormatted = ingredient.split(' ').join('_');
  for (i=0; i < ingredientFlavours.length; i++) {
    console.log('Checking ' + ingredientFormatted + ' against ' + JSON.stringify(ingredientFlavours[i].ingredient));
    if (ingredientFormatted == JSON.stringify(ingredientFlavours[i].ingredient)) {
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
