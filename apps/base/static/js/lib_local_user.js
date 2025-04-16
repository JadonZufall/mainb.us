const LOCAL_USER = {
	username: null,
	_updateStatusInterval: null,
}


// Resolve the username of the current user.
function _resolveUsername() {
	console.log('Attempting to resolve LOCAL_USER.username...');
	fetch('/api/v1/u/resolve/', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': CSRF_TOKEN
		}
	})
	.then(response => {
		if (!response.ok) {
			return response.json().then(error => {
				LOCAL_USER.username = null;
				console.log('Set LOCAL_USER.username to', LOCAL_USER.username)
				throw new Error(error.message || 'Request failed, response returned an error code.');
			});
		}
		return response.json()
	})
	.then(data => { 
		LOCAL_USER.username = data.data.username;
		console.log('Set LOCAL_USER.username to', LOCAL_USER.username);
	})
	.then(() => {
		_startUpdateUserStatusInterval();
	})
	.catch(error => console.error("Request failed:", error));
}


// Start an interval function that updates the user status every 5 minutes.
function _startUpdateUserStatusInterval() {
	if (LOCAL_USER._updateStatusInterval === null) {
		LOCAL_USER._updateStatusInterval = setInterval(() => {
			fetch(`/api/v1/u/status/${LOCAL_USER.username}/`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': CSRF_TOKEN
				}
			})
				.catch(error => console.error("Status update failed:", error));
		}, 300000); // 300,000 ms = 5 minutes
		return true;
	}
	console.error("Failed to start UpdateUserStatusInterval, as it is already running.");
	return false;
}

// Stop the interval function that updates the user status every 5 minutes.
function _stopUpdateUserStatusInterval() {
	if (LOCAL_USER._updateStatusInterval !== null) {
		clearInterval(LOCAL_USER._updateStatusInterval);
		LOCAL_USER._updateStatusInterval = null;
		return true;
	}
	console.error("Failed to stop UpdateUserStatusInterval, as it is not running.");
	return false;
}



_resolveUsername();