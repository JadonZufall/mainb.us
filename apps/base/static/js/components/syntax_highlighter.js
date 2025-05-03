
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
 * 
 * @param {string} line 
 * @returns 
 */
function format_python(line) {
	let letters = line.split("");
	let tokens = [];
	for (let i = 0; i < letters.length; i++) {
		if (letters[i] === undefined) { continue; }

		if (letters[i] === '"' || letters[i] === "'") {
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

		else if (false) {//else if (isWhitespace(letters[i])) {
			// Combine whitespace tokens.
			let count_spaces = 0;
			let count_tabs = 0;
			for (let j = i; j < letters.length; j++) {
				if (letters[j] === " ") { count_spaces += 1; }
				else if (letters[j] === "\t") { count_tabs += 1; }
				console.log(count_tabs, count_spaces);

				if (letters[j] !== " " && letters[j] !== "\t") {
					tokens.push({
						type: "whitespace",
						value: count_spaces + (4 * count_tabs),
						spaces: count_spaces,
						tabs: count_tabs,
						start: i,
						end: j - 1,
						error: false,
					});
					i = j - 1;
					break;
				}
				else if (j === letters.length - 1) {
					tokens.push({
						type: "whitespace",
						value: count_spaces + (4 * count_tabs),
						spaces: count_spaces,
						tabs: count_tabs,
						start: i,
						end: letters.length,
						error: false
					});
					i = letters.length;
					break;
				}
				else {
					continue;
				}
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

		else if (letters[i] === "#") {
			let value = line.substring(i, letters.length);
			tokens.push({ type: "comment", value: value, start: i, end: letters.length - 1, error: false });
			i = letters.length;
			break;
		}

		else if (isNumeric(letters[i])) {
			for (let j= i; j < letters.length; j++) {
				if (letters[j] == ".") {
					tokens.push({
						type: "number",
						value: line.substring(i, j),
						start: i,
						end: j-1,
						error: false
					});
					tokens.push({
						type: "decimal",
						value: letters[j],
						start: j,
						end: j,
						error: false
					});
					i = j+1;
					continue;
				}
				else if (!isNumeric(letters[j])) {
					tokens.push({
						type: "number", 
						value: line.substring(i, j), 
						start: i,
						end: j-1,
						error: false
					});
					i = j-1;
					break;
				}
				else if (j == letters.length - 1) {
					tokens.push({
						type: "number",
						value: line.substring(i, letters.length),
						start: i,
						end: j,
						error: false
					});
					i = j;
					break;
				}
				else {
					continue;
				}
			}
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
		let token = tokens[i];
		let prev = tokens[i-1];
		if (token.type === "undefined" && prev.type === "undefined" && token.error === prev.error) {
			let merged_token = {
				type: "undefined",
				value: prev.value + token.value,
				error: token.error,
				start: prev.start,
				end: token.end,
				merges: token.merges + prev.merges + 1
			};
			tokens[i-1] = merged_token;							// Set previous token equal to the merged token.
			tokens.splice(i, 1);			// Remove token @ index i
			i = i - 1;											// Step i back one to account for the element removed from the array.
		}
		else if (token.type === "whitespace" && prev.type === "whitespace" && token.error === prev.error) {
			let merged_token = {
				type: "whitespace",
				value: prev.value + token.value,
				error: token.error,
				start: prev.start,
				end: token.end,
				merges: token.merges + prev.merges + 1
			};
			tokens[i-1] = merged_token;							// Set previous token equal to the merged token.
			tokens.splice(i, 1);			// Remove token @ index i
			i = i - 1;											// Step i back one to account for the element removed from the array.
		}
	}

	let result = "";
	for (let i = 0; i < tokens.length; i++) {
		let token = tokens[i];
		if (token.type === "undefined") { 
			result += `<span class='undefined' error=${token.error}>${token.value}</span>`; 
		}
		else if (token.type === "string") { 
			result += `<span class='string' error="${token.error}">${token.value}</span>`; 
		}
		else if (token.type === "whitespace") { 
			result += `<span class='whitespace' start='${token.start}' end='${token.end}' value='${token.value}' error='${token.error}'>${''.padStart(token.value, '.')}</span>`; 
		}
		else if (token.type === "operator") { 
			result += `<span class='operator' error=${token.error} value='${value}'>${token.value}</span>`; 
		}
		else if (token.type === "number") { 
			result += `<span class='number' error=${token.error} value='${value}'>${token.value}</span>`; 
		}
		else if (token.type === "decimal") { 
			result += `<span class='decimal' error=${token.error} value='${value}'>${token.value}</span>`;
		}
		else { 
			result += `<span class="${token.type} error" error='${true}' value='${value}'>${token.value}</span>`; 
		}
	}
	
	console.log(tokens);

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