/**
Author: Michael Hawes
Date: 2 March 2017
*/

var api = {
  getData() {
    var url = 'https://alergyidentifier.com';
    return fetch(url).then((res) => res.json());
  }
};

module.exports = api;
