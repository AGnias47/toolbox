module.exports = {
	print: function (str) {
		console.log(str);
	},
	promise: function () {
		return new Promise(function(resolve, reject) {
			resolve();
		})
	}
}
