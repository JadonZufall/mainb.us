/* Library for parsing browser cookies. */
const Cookies = {
	set: (key, value) => {
		
	},
	get: (key) => {

	},
	del: (key) => {

	},
	pop: (key) => {
		let result = Cookies.get(key);
		Cookies.del(key);
		return result;
	},
	setdefault: (key, value) => {

	},
	iter: () => {
		for (let cookie of document.cookie.split(";")) {
			yield cookie.trim();
		}
		return null;
	},
	exists: (key) => {
		for (let k of Cookies.keys()) {
			if (key === k) { return true; }
		}
		return false;
	},
	keys: () => {
		for (let cookie of document.cookie.split(";")) {
			yield cookie.trim().split("=", 1)[0];
		}
	},
	values: () => {
		for (let cookie of document.cookie.split(";")) {
			yield cookie.trim().split("=", 1)[1];
		}
	},
	items: () => {
		for (let cookie of document.cookie.split(";")) {
			let cookie = cookie.trim.split("=", 1);
			yield cookie[0], cookie[1];
		}
	}


}