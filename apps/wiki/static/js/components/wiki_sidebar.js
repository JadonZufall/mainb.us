const WikiSidebar = {}

WikiSidebar.close = () => {
	let sidebar = document.getElementById("wiki-sidebar");
	if (!sidebar) {
		console.error("Unable to locate wiki sidebar element.");
		return;
	}

	sidebar.setAttribute("state", "closed");
	console.log("WikiSidebar.close");
}

WikiSidebar.open = () => {
	let sidebar = document.getElementById("wiki-sidebar");
	if (!sidebar) {
		console.error("Unable to locate wiki sidebar element.");
		return;
	}
	sidebar.setAttribute("state", "open");
	console.log("WikiSidebar.open");
}