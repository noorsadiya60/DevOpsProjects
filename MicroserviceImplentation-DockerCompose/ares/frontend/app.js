var express = require('express');
var app = express();

app.set('view engine', 'ejs');

const URL =  process.env.BACKEND_URL || "http://localhost:8000/api";

const fetch = (...args) => {
  return import('node-fetch').then(({default: fetch}) => fetch(...args));
};

app.get('/', async function(req, res) {
  const options = {
    method: 'GET'
  };
  fetch(URL, options)
    .then(res => res.json())
    .then(json => console.log(json))
    .catch(err => console.error('error:' + err));
  try {
    let response = await fetch(URL);
    response = await response.json();
    res.render('index', response);    
  } catch (error) {
    console.error('Error rendering index:', error);
    res.status(500).send('Internal Server Error');
  }
}); 

app.listen(3000, function() {
  console.log('Server is running on http://localhost:3000');
}); 
