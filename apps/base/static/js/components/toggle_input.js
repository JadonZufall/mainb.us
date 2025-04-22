document.querySelectorAll("span[editable]").forEach((element) => {
	let span = element.querySelector("span");
	if (!span) {
		console.warn("Unable to locate span in span[editable], resolving by creating one.", element);
		span = document.createElement("span");
		element.appendChild(span);
	}
	let input = element.querySelector("input");
	if (!input) {
		console.warn("Unable to locate input in span[editable], resolving by creating one.", element);
		input = document.createElement("input");
		element.appendChild(input);
	}
	input.setAttribute("on-load-value", input.value);
	span.textContent = input.value;
});

document.querySelectorAll("span[editable] input").forEach((element) => {
	console.log("loading", element);
	element.addEventListener("input", (event) => {
		element.parentElement.querySelector("span").textContent = element.value;
	});
});



function toggleInputGroup(group) {
	console.log("Toggling group", group);
	document.querySelectorAll(`span[editable][group="${group}"]`).forEach((element) => {
		if (element.hasAttribute("toggle")) {
			element.removeAttribute("toggle");
		}
		else {
			element.setAttribute("toggle", true);
		}
	});
}