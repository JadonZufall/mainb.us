

document.querySelectorAll("button.media-button").forEach((button, index) => {
	button.addEventListener("click", (event) => {
		button.classList.toggle("is-active");
	});

	button.addEventListener("keydown", (event) => {
		if (event.key === "Enter") {
			button.classList.toggle("is-active");
		}
	});

});

document.querySelectorAll("button.media-button.play").forEach((button, index) => {
	button.addEventListener("click", (event) => {
		// Get media player and play it.
	});
});