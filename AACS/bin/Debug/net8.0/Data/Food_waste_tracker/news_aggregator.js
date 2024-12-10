const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

const newsApiKey = 'YOUR_NEWS_API_KEY';

app.get('/', async (req, res) => {
  const query = req.query.q;
  const response = await axios.get(`https://newsapi.org/v2/everything?q=${query}&apiKey=${newsApiKey}`);
  res.json(response.data.articles);
});

app.listen(port, () => {
  console.log(`News aggregator listening at http://localhost:${port}`);
});