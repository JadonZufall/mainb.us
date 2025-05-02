class MainbusCheckboxElement {
	constructor() {
		super();

	}

	connectedCallback() {
		// Called when the element is added to the DOM

	}

	disconnectedCallback() {
		// Called when the element is removed from the DOM

	}

	attributeChangedCallback(name, oldValue, newValue) {
		
	}

	handleClick(event) {
		// Handle the click event

	}

	static get observedAttributes() {
		// Return an array of attributes to observe for changes

		return ["checked", "disabled"];
	}

}


customElements.define("mb-checkbox", MainbusCheckboxElement);