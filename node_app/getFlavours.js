var csv = require('csv-parser');
var fs = require('fs');

var dishIngredients = require('./data/dishIngredients.json');
var ingredientFlavours = require('./data/ingredientFlavours.json');

var flavourArray = ["alcoholic beverage", "animal product", "cereal/crop", "dairy", "fish/seafood", "flower", "fruit", "herb", "meat", "nut/seed/pulse", "plant", "plant derivative", "spice", "vegetable"];

var getIngredientFlavours = function(dish) {
  var flavourProfile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (i=0; i < dishIngredients.dishes.length; i++) { //check what dish was selected
    var dishNameCheck = JSON.stringify(dishIngredients.dishes[i].name);
    var dishIngredientsCheck = dishIngredients.dishes[i].ingredients;
    console.log('Checking ' + dishNameCheck);
    if (dish == dishNameCheck) {
      console.log(dish + " matches " + dishNameCheck);
      console.log(dishIngredientsCheck.length);
      for (var x=0; x < dishIngredientsCheck.length; x++) { //loop through each ingredient
        console.log('Checking ' + dishIngredientsCheck[x]);
        var flavourIndex = findFlavour(dishIngredientsCheck[x], ingredientFlavours);
        if(flavourIndex != -1) {
          flavourProfile[flavourIndex] += 1
        };
      };
    };
  };
  return flavourProfile
};

function findFlavour(ingredient, ingredientFlavours) {
  var flavourIndex = -1;
  ingredientFormatted = ingredient.split(' ').join('_');
  console.log(ingredientFormatted);
  for (var n=0; n < ingredientFlavours.length; n++) {
    if (ingredientFormatted == ingredientFlavours[n].ingredient.toString()) {
      console.log('Ingredient matched!');
      console.log(flavourArray);
      for (var m=0; m<flavourArray.length; m++) {
        console.log('Checking ' + ingredientFlavours[n].flavour.toString() + ' against ' + flavourArray[m]);
        if (ingredientFlavours[n].flavour.toString() == flavourArray[m]) {
          console.log('Match found!');
          flavourIndex = m;
        };
      };
    };
  };
  return flavourIndex;
};

module.exports = {
  getIngredientFlavours: getIngredientFlavours
}
