let url = `ws://${window.location.host}/ws/socket-server/`;
const ws = new WebSocket(url);

ws.onmessage = (event) => {
	let message = JSON.parse(event.data);
	console.log("data:", message);
}


let form = document.getElementById("chat-form");
form.addEventListener(
	"submit", (event) => {
		event.preventDefault()
		let message = event.target.message.value;
		ws.send(JSON.stringify({
			'message': message
		}))
		form.reset();
	}
)

