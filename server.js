const express = require("express");
const app = express();
const axios = require("axios");
const jwt = require("jsonwebtoken");

let secret = null;
let ans = "";
app.use(function (req, res, next) {
	req.text = "";
	req.on("data", function (chunk) {
		req.text += chunk;
	});
	req.on("end", next);
});
const getJWTSecret = async () => {
	const res = await axios({
		method: "get",
		url: "https://hackattic.com/challenges/jotting_jwts/problem?access_token=b53b9d130f72e759",
	});
	secret = res.data.jwt_secret;
};

app.post("/", (req, res) => {
	jwt.verify(req.text, secret, (err, decoded) => {
		if (err) {
			console.error(err.message);
			return res.json({});
		}
		if (decoded && decoded["append"]) {
			ans += decoded["append"];
			return res.json({});
		}
		if (decoded) {
			res.json({ solution: ans });
			axios({
				method: "post",
				url: "https://hackattic.com/challenges/jotting_jwts/solve?access_token=b53b9d130f72e759",
				data: {
					solution: ans,
				},
			}).then((sad) => {
				console.log("Submitted APP solution", ans, sad.data);
			});
		}
	});
});
app.listen(8083, () => {
	getJWTSecret().then(() => {
		console.log("Recieved Secret", secret);
		axios({
			method: "post",
			url: "https://hackattic.com/challenges/jotting_jwts/solve?access_token=b53b9d130f72e759",
			data: {
				app_url: "https://d475-124-40-247-86.ngrok-free.app",
			},
		}).then((res) => {
			console.log("Submitted APP URL", res.data);
		});
	});
});
