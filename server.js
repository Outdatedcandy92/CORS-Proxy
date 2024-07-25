const express = require('express');
const app = express();
const cors = require('cors');



app.use(cors());

app.get("/", async (req, res) => {
    const fetch = (await import('node-fetch')).default;
    const response = await fetch('URL');;
    console.log(response);
    res.json(await response);   
});


app.listen(3000, () => {
  console.log('server started');
})