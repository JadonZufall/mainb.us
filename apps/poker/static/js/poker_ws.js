let url = `ws://${window.location.host}/ws/socket-server/`;
const ws = new WebSocket(url);

ws.onmessage = (event) => {
	let message = JSON.parse(event.data);
	console.log("data:", message);
}
