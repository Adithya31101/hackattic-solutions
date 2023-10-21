const axios = require("axios");

const getData = async (url) => {
	const res = await axios({
		method: "get",
		url,
	});
	return res.data;
};

const executor = async () => {
	// const {bytes} = await getData(
	// 	"https://hackattic.com/challenges/help_me_unpack/problem?access_token=b53b9d130f72e759"
	// );
	// bytes =
};

executor().then(() => console.log("DONE"));
