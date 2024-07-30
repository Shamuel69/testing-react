const fs = require('fs');

// JSON data to write to file
const jsonData = {
  name: 'John',
  age: 30,
  city: 'New York'
};

// Convert JSON data to string
const jsonString = JSON.stringify(jsonData);

// Write JSON string to file
fs.writeFile('JStoPy.json', jsonString, (err) => {
  if (err) throw err;
  console.log('Data has been written to file');
});