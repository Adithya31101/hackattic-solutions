const express = require("express");
const app = express();

app.get("/12", (req, res) => {
	console.log(req.ip);
	console.log(req.ips);
	res.send("thanks");
});

app.listen(8083, () => {
	console.log("Listening on port 8083");
});
