function getCSRFToken() {
	for (let cookie of document.cookie.split(";")) {
		if (cookie.trim().startsWith('csrftoken=')) {
			return decodeURIComponent(cookie.substring('csrftoken='.length));
		}
	}
	return null;
}

const CSRF_TOKEN = getCSRFToken();