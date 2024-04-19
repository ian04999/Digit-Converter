const express = require('express');
const app = express();
const port = 3000;

// Set 'views' directory for any views, and set the view engine to Pug
app.set('views', './views');
app.set('view engine', 'pug');

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Define a route to render the Pug template
app.get('/', (req, res) => {
  res.render('index');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});