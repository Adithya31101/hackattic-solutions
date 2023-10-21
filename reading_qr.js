const jimp = require("jimp");
const axios = require("axios");
const QrCode = require("qrcode-reader");

const getImageURL = (url) => {
	return new Promise((resolve, reject) => {
		axios({
			method: "get",
			url,
		})
			.then((res) => {
				const url = res.data.image_url;
				console.log("Sucessfully requested image url", url);
				resolve(url);
			})
			.catch((err) => reject(err));
	});
};

const downloadAndCrop = (url) => {
	return new Promise((resolve, reject) => {
		jimp
			.read(url)
			.then((res) => {
				console.log("Image Reading successful");
				code = new QrCode();
				code.callback = (err, decodeRes) => {
					if (err) {
						console.error(err);
						return;
					}
					console.log("QR Code DECODED: ", decodeRes.result);
					resolve(decodeRes.result);
				};
				code.decode(res.bitmap);
			})
			.catch((err) => {
				reject(err);
			});
	});
};

const postData = (code, url) => {
	return new Promise((resolve, reject) => {
		axios({
			method: "post",
			url,
			data: { code },
		})
			.then((res) => {
				resolve(res.data);
			})
			.catch((err) => {
				reject(err);
			});
	});
};

const executor = async () => {
	const url = await getImageURL(
		"https://hackattic.com/challenges/reading_qr/problem?access_token=b53b9d130f72e759"
	);
	const code = await downloadAndCrop(url);
	const result = await postData(
		code,
		"https://hackattic.com/challenges/reading_qr/solve?access_token=b53b9d130f72e759"
	);
	console.log(result);
};

executor().then(() => console.log("DONE"));
