document.addEventListener("DOMContentLoaded", function () {
    const socket = new WebSocket('ws://localhost:8000/ws/poker/');

    socket.onopen = function () {
        console.log("WebSocket connected");
        socket.send(JSON.stringify({ 'message': 'Hello, Server!' }));
    };

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log("Received from server: ", data.message);
    };

    socket.onclose = function () {
        console.log("WebSocket disconnected");
    };
});