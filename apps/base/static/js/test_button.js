function onTestButton(){
	document.querySelectorAll(".user-chip").forEach((element) => {
		if (element.getAttribute("state") == "minimal") {
			element.setAttribute("state", "expanded");
		}
		else {
			element.setAttribute("state", "minimal");
		}
	})
}