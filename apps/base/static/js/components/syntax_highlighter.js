function format_python(line) {
	


	let result = line
		.replace(/(['"`])(.*?)\1/g, '{%STR_START%}$&{%STR_END%}')
		.replace(/(\b\d+(\.\d+)?|\b\d+)\b/g, '<span class="number">$1</span>')
		.replace(/(def|class|if|else|elif|for|while|try|except|finally|with|as|import|from|return)\b/g, '<span class="keyword">$1</span>');


	// Place strings inside span tags.
	result = result
		.replace(/{%STR_START%}['"`]/g, `<span class="string">$&`)
		.replace(/['"`]{%STR_END%}/g, `$&</span>`);
	// Remove the extra tags surrounding the span tag.
	result = result
		.replace(/[({%STR_START%})({%STR_END%})]/g, "");

	return result;
}

function format_javascript(line) { return line; }

function format_code(line, language) {
	if (language === "plaintext") { return line; }
	else if (language === "python") { return format_python(line); }
	else if (language === "javascript") { return format_javascript(line); }
	else { return "Unsupport syntax"; }
}


document.querySelectorAll("textarea.syntax-input").forEach((element) => {
	element.value = "";
	let display_id = element.getAttribute("for") || null;
	let display = document.querySelector(`#${display_id}`);
	if (!display) {
		console.warn("No display element found for", display_id, element);
		return;
	}
	element.addEventListener("input", (event) => {
		let language = element.getAttribute("syntax") || "plaintext";
		let display_value = "";
		
		let lines = element.value.split(/\r?\n/g);
		for (let i = 0; i < lines.length; i++) {
			let line = format_code(lines[i], language);
			display_value += `<span class="line">${line}</span><br>`;
		}
		display.innerHTML = display_value;
	});
})