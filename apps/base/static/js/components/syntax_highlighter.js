




/**
 * @function
 * @summary Returns if the provided value is considered to be a digit (1-9)
 * @description Function that is used to check if a string is considered to be a digit, much like isDigit method in python.  This function checks if the provided value is a digit with regex.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` when `value` is a digit and `false` when `value` is not considered a digit.
 */
function isDigit(value) { return /^\d+$/.test(value); }


/**
 * @function
 * @summary Return if the provided value is considered to be a decmil point (. or ,)
 * @description Function that is used to check if a string is considered to be the seperator between a number and the fractional section of a number.
 * @author Jadon Zufall
 * @param {string}
 * @returns {boolean} `true` when `value` is a decimal point `false` when `value` is not a decimal point.
 */
function isDecimal(value) { return value === "."; }

/** 
 * @function
 * @summary Returns if the provided value is considered to be numeric (meaning 1-9 or .)
 * @description Function that is used to check if a string is considered to be numeric, much like the isNumeric method in python strings.  This function checks to see if the provided value is a string, then ensures that it is not NaN and then ensures that `parseFloat(value)` does not return NaN.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` when `value` is considered numeric and `false` when `value` is not considered numeric.
 */
function isNumeric(value) { return typeof(value) === "string" && !isNaN(value) && !isNaN(parseFloat(value)); }

/** 
 * @function
 * @summary Returns if the provided value is considered to be part of an operator.
 * @description Function that is used to check if a string is considered to be an operator.  This function checks to see if the provided value is one of many different operators contained in an array.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` when `value` is considered an operator and `false` when `value` is not considered an operator.
 * @example if (isOperator("+")) { ... }
 */
function isOperator(value) { return !isNaN(value) && (value === "=" || value === "+" || value === "-" || value === "*" || value === "/" || value === "%" || value === ">" || value === "<" || value === "!" || value === "&" || value === "|" || value === "^"); }

/**
 * @function
 * @summary Returns if the provided value is considerd to be whitespace.
 * @description Function that is used to check if a string is considered to be whitespace.  This function checks every character in the string and ensures its a whitespace character, it also ensures the string is not empty or NaN.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` when `value` is considered to only consist of whitespace and is not blank and `false` when `value` is either blank, or contains non whitespace characters.
 */
function isWhitespace(value) {
	if (typeof(value) !== "string") { return false; }
	return /^\s*$/.test(value);
}


/**
 * @function
 * @summary Checks if a value is a quote symbol.
 * @description A function that checks if a value is a quote symbol, such as " or ' for use in various parsing functions.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` if `value` is a quote symbol `false` if `value` is not a quote symbol.
 */
function isQuotes(value) {
	if (typeof(value) !== "string") { return false; }
	return value === '"' || value === "'";
}


/**
 * @function
 * @summary Checks if a value is a line comment symbol.
 * @description A function that checks if a value is a line comment symbol for use in various parsing functions.
 * @author Jadon Zufall
 * @param {string} value The target value.
 * @returns {boolean} `true` if `value` is a line comment symbol `false` if `value` is not a line comment symbol.
 */
function isLineComment(value) {
	if (typeof(value) !== "string") { return false; }
	return value === "#";
}


/**
 * @function
 * @summary Cleans up a line of code.
 * @description Cleans up a line of code by replacing values like &, < and > with the values HTML uses to display them.
 * @author Jadon Zufall
 * @param {string} value The line you wish to clean.
 * @returns {string} The clean line of code.
 */
function cleanLine(value) {
	return value.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;");
}


/**
 * @function
 * @summary Formats code in python.
 * @description Formats code in python via tokenization. In reality this function is the overly complicated way of doing it I should have just used an abstract syntax tree.
 * @author Jadon Zufall
 * @param {string} line The line of code that you wish to format.
 * @returns {string} The formatted python code.
 */
function format_python(line) {
	line = cleanLine(line);
	let letters = line.split("");
	let tokens = [];
	for (let i = 0; i < letters.length; i++) {
		if (letters[i] === undefined) { continue; }

		else if (i + 1 < letters.length && letters[i] === 'f' && isQuotes(letters[i+1])) {
			tokens.push({ type: "f-string-prefix", value: letters[i], start: i, end: i, error: false });
		}

		else if (i + 2 < letters.length && isQuotes(letters[i]) && letters[i] === letters[i+1] && letters[i] === letters[i+2]) {
			tokens.push({ type: "blockquote-flag", value: ''.padEnd(3, letters[i]), start: i, end: i+2, error: false });
			i = i + 3;
			
			// Search for end of block quotes
			let is_closed = false;
			for (let j = i; j < letters.length - 2; j++) {
				if (letters[i-1] === letters[j] && letters[j] === letters[j+1] && letters[j] === letters[j+2]) {
					is_closed = true;
					// Push the contents of the block quote, if the closing block quotes does not come immedietly after.
					if (j !== i) {
						tokens.push({ type: "blockquote-text", value: line.substring(i, j), start: i, end: j-1, error: false });
					}
					// Push the closing blockquotes.
					tokens.push({ type: "blockquote-flag", value: ''.padEnd(3, letters[j]), start: j, end: j+2, error: false });
					i = j + 2;
					break;
				}
			}
			
			// If the blockquote was not closed on this line then make it take up the entire rest of the line.
			if (!is_closed) {
				tokens.push({ type: "blockquote-text", value: line.substring(i, letters.length), start: i, end: letters.length, error: false });
				i = letters.length;
				break;
			}
			
		}

		else if (isQuotes(letters[i])) {
			is_closed = false;
			for (let j = i+1; j < letters.length; j++) {
				if (letters[j] === letters[i]) {
					tokens.push({
						type: "string", 
						value: line.substring(i, j+1),
						start: i,
						end: j,
						error: false
					});
					is_closed = true;
					i = j;
					break;
				}
			}
			if (!is_closed) {
				tokens.push({
					type: "string", 
					value: line.substring(i, letters.length),
					start: i,
					end: letters.length - 1,
					error: true
				});
				break;
			}
		}

		else if (isWhitespace(letters[i])) {
			let value = 0;
			if (letters[i] === " ") { value = 1; }
			else if (letters[i] === "\t") { value = 4; }
			tokens.push({ type: "whitespace", value: value, start: i, end: i, error: false });
		}

		else if (isOperator(letters[i])) {
			tokens.push({ type: "operator", value: letters[i], start: i, end: i, error: false });
		}

		else if (isLineComment(letters[i])) {
			let value = line.substring(i, letters.length);
			tokens.push({ type: "comment", value: value, start: i, end: letters.length - 1, error: false });
			i = letters.length;
			break;
		}

		else if (isDigit(letters[i])) {
			tokens.push({ type: "number", value: letters[i], start: i, end: i, error: false });
		}

		else if (isDecimal(letters[i])) {
			tokens.push({ type: "decimal", value: letters[i], start: i, end: i, error: false });
		}

		else {
			tokens.push({ type: "undefined", value: letters[i], start: i, end: i, error: false });
		}
	}


	// Validate tokens.
	for (let i = 0; i < tokens.length; i++) {
		let token = tokens[i];
		if (!Object.hasOwn(token, "type")) { 
			console.warn("Token does not have required type value, resolving it by defaulting it to undefined.", token);
			token.type = "undefined"; 
		}
		if (!Object.hasOwn(token, "error")) {
			console.warn("Token does not have required error value, resolving it by defaulting it to false.", token);
			token.error = false;
		}
		if (!Object.hasOwn(token, "value")) {
			console.warn("Token does not have required value value, resolving it by defaulting it to null.", token);
			token.value = null;
		}
		if (!Object.hasOwn(token, "merges")) {
			// No value should have this at this point so we assign the default number of merges (0), this is used in the next step for debugging purposes.
			token.merges = 0;
		}
	}

	// Merge like tokens
	for (let i = 1; i < tokens.length; i++) {
		let prev = tokens[i-1];
		let token = tokens[i];
		if (token.type === "undefined" && prev.type === "undefined" && token.error === prev.error) {
			let merged_token = { type: "undefined", value: prev.value + token.value, error: token.error, start: prev.start, end: token.end, merges: token.merges + prev.merges + 1 };
			tokens[i-1] = merged_token;							// Set previous token equal to the merged token.
			tokens.splice(i, 1);			// Remove token @ index i
			i = i - 1;											// Step i back one to account for the element removed from the array.
		}
		else if (token.type === "whitespace" && prev.type === "whitespace" && token.error === prev.error) {
			let merged_token = { type: "whitespace", value: prev.value + token.value, error: token.error, start: prev.start, end: token.end, merges: token.merges + prev.merges + 1 };
			tokens[i-1] = merged_token;							// Set previous token equal to the merged token.
			tokens.splice(i, 1);			// Remove token @ index i
			i = i - 1;											// Step i back one to account for the element removed from the array.
		}
		else if (token.type === "number" && prev.type === "number" && token.error === prev.error) {
			let merged_token = { type: "number", value: prev.value + token.value, error: token.error, start: prev.start, end: token.end, merges: token.merges + prev.merges + 1 };
			tokens[i-1] = merged_token;							// Set previous token equal to the merged token.
			tokens.splice(i, 1);			// Remove token @ index i
			i = i - 1;											// Step i back one to account for the element removed from the array.
		}
		else if (token.type === "blockquote-flag" && prev.type === "blockquote-flag" && token.error === prev.error) {
			// Merge blockquote flags only if they have no blockquote-text inbetween them.
			let merged_token = { type: "blockquote", value: prev.value + token.value, error: token.error, start: prev.start, end: token.end, merges: token.merges + prev.merges + 1 };
			tokens[i-1] = merged_token;
			tokens.split(i, 1);
			i = i - 1;
		}
	}

	// Merge string => fstring
	for (let i = 1; i < tokens.length; i++) {
		let prev = tokens[i-1];
		let token = tokens[i];
		if (prev.type === "f-string-prefix" && token.type === "string") {
			let merged_token = { type: "f-string", value: prev.value + token.value, error: token.error, start: prev.start, end: token.end, merges: token.merges + prev.merges + 1 };
			tokens[i-1] = merged_token;
			tokens.splice(i, 1);
			i = i - 1;
		}
	}

	// Merge 3 group values.
	for (let i = 1; i < tokens.length - 1; i++) {
		let prev = tokens[i-1];
		let token = tokens[i];
		let next = tokens[i+1];
		if (prev.type === "number" && next.type === "number" && token.type === "decimal" && token.error === prev.error && token.error === next.error) {
			let merged_token = { type: "float", value: prev.value + token.value + next.value, error: token.error, start: prev.start, end: next.end, merges: token.merges + prev.merges + next.merges + 1 };
			tokens[i-1] = merged_token;
			tokens.splice(i, 2);
			i = i - 1;
		}
		else if (prev.type === "blockquote-flag" && token.type === "blockquote-text" && next.type === "blockquote-flag" && token.error === prev.error && token.error === next.error) {
			let merged_token = { type: "blockquote", value: prev.value + token.value + next.value, error: token.error, start: prev.start, end: next.end, merges: token.merges + prev.merges + next.merges + 1 };
			tokens[i-1] = merged_token;
			tokens.splice(i, 2);
			i = i - 1;
		}
	}


	let result = "";
	for (let i = 0; i < tokens.length; i++) {
		let token = tokens[i];
		if (token.type === "undefined") {
			result += `<span class='undefined' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`; 
		}
		else if (token.type === "comment") {
			result += `<span class='comment' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`;
		}
		else if (token.type === "blockquote-flag") {
			result += `<span class='blockquote-flag' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`;
		}
		else if (token.type === "blockquote-text") {
			result += `<span class='blockquote-text' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`;
		}
		else if (token.type === "blockquote") {
			let value;
			if (!token.error) {
				value = `<span class='quote open'>${token.value.substring(0, 3)}</span>`
				value += `<span class='quote text'>${token.value.substring(3, token.value.length - 3)}</span>`
				value += `<span class='quote close'>${token.value.substring(token.value.length - 3, token.value.length)}</span>`
			}
			else {
				value = `<span class='quote text'>${token.value}</span>`
			}
			result += `<span class='blockquote' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${value}</span>`
			
		}
		else if (token.type === "f-string") {
			let value;
			if (!token.error) {
				value = `<span class='quote prefix'>${token.value[0]}</span>`;
				value += `<span class='quote open'>${token.value[1]}</span>`;
				value += `<span class='quote value'>${token.value.substring(2, token.value.length - 1)}</span>`;
				value += `<span class='quote close'>${token.value[token.value.length-1]}</span>`;
			}
			else {
				value = `<span class='quote value'>${token.value}</span>`
			}
			result += `<span class='f-string' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${value}</span>`; 
		}
		else if (token.type === "string") {
			let value;
			if (!token.error) {
				value = `<span class='quote open'>${token.value[0]}</span>`;
				value += `<span class='quote value'>${token.value.substring(1, token.value.length - 1)}</span>`;
				value += `<span class='quote close'>${token.value[token.value.length-1]}</span>`;
			}
			else {
				value = `<span class='quote value'>${token.value}</span>`
			}
			result += `<span class='string' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${value}</span>`; 
		}
		else if (token.type === "whitespace") { 
			result += `<span class='whitespace' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${''.padStart(token.value, '.')}</span>`; 
		}
		else if (token.type === "operator") { 
			result += `<span class='operator' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`; 
		}
		else if (token.type === "number") { 
			result += `<span class='number' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`; 
		}
		else if (token.type === "decimal") { 
			result += `<span class='decimal' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`;
		}
		else if (token.type === "float") {
			result += `<span class='float' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${token.value}</span>`
		}
		else { 
			result += `<span class='${token.type} error' start='${token.start}' end='${token.end}' value='${token.value}' error='${true}' errorType='INVALID_TYPE'>${token.value}</span>`; 
		}
	}
	
	console.log(tokens);

	return result;
}


/**
 * @function
 * @summary Formats code in javascript.
 * @description Formats code in javascript via tokenization. In reality this function is the overly complicated way of doing it I should have just used an abstract syntax tree.
 * @author Jadon Zufall
 * @param {string} line The line of code that you wish to format.
 * @returns {string} The formatted javascript code.
 */
function format_javascript(line) { 
	throw new Error("Not implemented error.  Javascript formatter has not been created.");
}


/**
 * @function
 * @summary Format a line of code based on the language provided.
 * @description Formats a line of code for the language provided. Checks the language with what is basically a switch and calls the coorisponding function for formatting that language.  Returns Unsupported syntax when invalid language is provided.
 * @author Jadon Zufall
 * @param {string} line The line of code you wish to format.
 * @param {string} language The language you wish to format this code for.
 * @returns {string} The formatted code.
 */
function format_code(line, language) {
	if (language === "plaintext") { return line; }
	else if (language === "python") { return format_python(line); }
	else if (language === "javascript") { return format_javascript(line); }
	else { return "Unsupport syntax"; }
}


// Auto update the paragraph (<p>) that is connected to the text area (<textarea>).
document.querySelectorAll("textarea.syntax-input").forEach((element) => {
	// Clear the textarea
	element.value = "";
	
	// Check for a bound paragraph for this textarea.
	let display_id = element.getAttribute("for") || null;
	if (!display_id) {
		console.warn("Unbound display element for", element);
	}
	
	// Get the bound paragraph for this textarea.
	let display = document.querySelector(`#${display_id}`);
	if (!display) {
		console.warn("No display element found for", display_id, element);
		return;
	}

	// Add an event listener to listen for input provided to the text area.
	element.addEventListener("input", (event) => {
		// Get the language of the syntax highlighter.
		let language = element.getAttribute("syntax") || "plaintext";

		// Initialize an empty string for storing the final display value of the paragraph.
		let display_value = "";
		
		// Seperate out the lines.
		let lines = element.value.split(/\r?\n/g);
		for (let i = 0; i < lines.length; i++) {
			// Format each line one by line then add line breaks.
			let line = format_code(lines[i], language);
			display_value += `<span class="line">${line}</span><br>`;
		}

		// Set the innerHTML of the bound paragraph to the final display_value.
		display.innerHTML = display_value;
	});
})