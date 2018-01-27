var spawn = require('child_process').spawn,
py = spawn('python', ['neural_network/fitted_model.py']),
dataString = '';

var sendData = function(data) {
  py.stdout.on('data', function(data){
    dataString += data.toString();
  });
  py.stdout.on('data', function(data){
    dataString += data.toString();
  });
  py.stdout.on('end', function(){
    console.log('Drink Mix = ',dataString);
  });
  py.stdin.write(JSON.stringify(data));
  py.stdin.end();

  return dataString
};

module.exports = {
  sendData: sendData
};
