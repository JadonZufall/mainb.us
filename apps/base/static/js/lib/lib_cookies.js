/* Library for parsing browser cookies. */
const Cookies = {
	set: (key, value, options = {}) => {
		let cookieString = `${encodeURIComponent(key)}=${encodeURIComponent(value)}`;
		if (options.expires) {
			cookieString += `; expires=${options.expires.toUTCString()}`;
		}
		if (options.path) {
			cookieString += `; path=${options.path}`;
		}
		if (options.domain) {
			cookieString += `; domain=${options.domain}`;
		}
		if (options.secure) {
			cookieString += `; secure`;
		}
		document.cookie = cookieString;
	},
	get: (key) => {
		const cookies = document.cookie.split(";").map(cookie => cookie.trim());
		for (let cookie of cookies) {
			const [k, v] = cookie.split("=");
			if (decodeURIComponent(k) === key) {
				return decodeURIComponent(v);
			}
		}
		return null;
	},
	del: (key, options = {}) => {
		Cookies.set(key, "", { ...options, expires: new Date(0) });
	},
	pop: (key) => {
		let result = Cookies.get(key);
		Cookies.del(key);
		return result;
	},
	setdefault: (key, value, options = {}) => {
		if (!Cookies.exists(key)) {
			Cookies.set(key, value, options);
		}
	},
	iter: function* () {
		for (let cookie of document.cookie.split(";")) {
			yield cookie.trim();
		}
	},
	exists: (key) => {
		return Cookies.get(key) !== null;
	},
	keys: function* () {
		for (let cookie of document.cookie.split(";")) {
			yield decodeURIComponent(cookie.trim().split("=")[0]);
		}
	},
	values: function* () {
		for (let cookie of document.cookie.split(";")) {
			yield decodeURIComponent(cookie.trim().split("=")[1]);
		}
	},
	items: function* () {
		for (let cookie of document.cookie.split(";")) {
			const [key, value] = cookie.trim().split("=");
			yield [decodeURIComponent(key), decodeURIComponent(value)];
		}
	}
};