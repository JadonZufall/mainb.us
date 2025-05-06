


class MB_TextEditor extends HTMLElement {
	static observedAttributes = [];

	constructor() {
		super();
		this.header = document.createElement("div");
		this.appendChild(this.header);

		this.textarea = document.createElement("textarea");
		this.appendChild(this.textarea);

		
	}
}

customElements.define("mb-texteditor", MB_TextEditor);
