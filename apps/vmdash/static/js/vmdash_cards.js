


function vmdash_card_btn_delete(pk) {

}

function vmdash_card_btn_done(pk) {

}

function vmdash_card_btn_edit(pk) {
	let inputVIN = document.getElementById(`input-vin-${pk}`);
	let spanVIN = document.getElementById(`span-vin-${pk}`);
	inputVIN.removeAttribute("hidden");
	spanVIN.setAttribute("hidden", true);
	inputVIN.setAttribute("value", spanVIN.textContent);
	if (inputVIN.getAttribute("value") === "None") {
		inputVIN.setAttribute("value", "");
	}
	
	let inputPlate = document.getElementById(`input-plate-${pk}`);
	let spanPlate = document.getElementById(`span-plate-${pk}`);
	inputPlate.removeAttribute("hidden");
	spanPlate.setAttribute("hidden", true);
	inputPlate.setAttribute("value", spanPlate.textContent);
	if (inputPlate.getAttribute("value") === "None") {
		inputVIN.setAttribute("value", "");
	}

	let inputMiles = document.getElementById(`input-miles-${pk}`);
	let spanMiles = document.getElementById(`span-miles-${pk}`);
	inputMiles.setAttribute("value", spanMiles.textContent);
	inputMiles.removeAttribute("hidden");
	spanMiles.setAttribute("hidden", true);

	let editButton = document.getElementById(`button-edit-${pk}`);
	editButton.setAttribute("hidden", true);

	let doneButton = document.getElementById(`button-done-${pk}`);
	doneButton.removeAttribute("hidden");
}