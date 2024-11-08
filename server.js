// server.js
//Imports and Setup
const express = require("express");
const path = require("path"); 
const app = express();
const port = 3000;


// Mock function to simulate fetching data from a database
function getLatestUpdates() {
  return "Latest data from the database at " + new Date().toLocaleTimeString();
}

app.use(express.static(path.join(__dirname)));

// Define an endpoint that sends updates to the client
app.get("/get-updates", (req, res) => {
  const updates = getLatestUpdates();
  res.send(updates);
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});