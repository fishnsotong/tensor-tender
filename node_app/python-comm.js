var request = require('request');

var sendData = function(data) {
  var res;
  request({
    uri: 'http://127.0.0.1:5000/pred',
    method: 'POST',
    json: data
  }, function(error, response, body) {
    console.log("response" + response);
    res = body;
    if (error) {
      console.log('Error: ' + error);
    }
  });
  return res;
};

module.exports = {
  sendData: sendData
};
