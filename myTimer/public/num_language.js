function singleDigit(number) {
    if (number === 1) {return "one";}
    if (number === 2) {return "two";}
    if (number === 3) {return "three";}
    if (number === 4) {return "four";}
    if (number === 5) {return "five";}
    if (number === 6) {return "six";}
    if (number === 7) {return "seven";}
    if (number === 8) {return "eight";}
    if (number === 9) {return "nine";} 
    else {return "invalid input";}
}

function twoDigit(number) {
    let digitS = "";
    
    if (number === 10) {
        return "ten";
    } else if (number === 11) {
        return "eleven";
    } else if (number === 12) {
        return "twelve";
    } else if (number === 13) {
        return "thir" + digitS;
    } else if (number === 15) {
        return "fif" + digitS;
    } else if (number === 18) {
        return "eigh" + digitS;
    } else if (number < 20) {
        var front = singleDigit(number % 10);
        return front + digitS;
    } else if (number < 30) {
        var front = "twenty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 40) {
        var front = "thirty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 50) {
        var front = "forty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 60) {
        var front = "fifty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 70) {
        var front = "sixty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 80) {
        var front = "seventy ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 90) {
        var front = "eighty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    } else if (number < 100) {
        var front = "ninty ";
        if (number % 10 === 0) {
            return front;
        } else {
            return front + singleDigit(number % 10);
        }
    }
}

function threeDigit(number) {
    const nHundred = Math.floor(number / 100);
    var front = singleDigit(nHundred) + " hundred";
    const two_digit = number - nHundred * 100;
    
    if (two_digit >= 10) {
        return front + " " + twoDigit(two_digit);
    } else if (two_digit < 10 && two_digit > 0) {
        return front + " " + singleDigit(two_digit);
    }
    
    return front;
}

function thousand(number) {
    const nThousand = Math.floor(number / 1000);
    const num_digits = String(nThousand).length;
    
    if (num_digits === 1) {
        var front = singleDigit(nThousand) + " thousand ";
    } else if (num_digits === 2) {
        var front = twoDigit(nThousand) + " thousand ";
    } else if (num_digits === 3) {
        var front = threeDigit(nThousand) + " thousand ";
    }
    
    var three_digit = number - nThousand * 1000;
    
    if (three_digit < 1000 && three_digit > 99) {
        return front + threeDigit(three_digit);
    } else if (three_digit < 100 && three_digit > 9) {
        return front + twoDigit(three_digit);
    } else if (three_digit < 10 && three_digit > 0) {
        return front + singleDigit(three_digit);
    } else {
        return front;
    }
}

function million(number) {
    const nMillion = Math.floor(number / 1000000);
    const num_digits = String(nMillion).length;
    
    if (num_digits === 1) {
        var front = singleDigit(nMillion) + " million ";
    } else if (num_digits === 2) {
        var front = twoDigit(nMillion) + " million ";
    } else if (num_digits === 3) {
        var front = threeDigit(nMillion) + " million ";
    } else if (num_digits >= 4 && num_digits <= 6) {
        var front = thousand(nMillion) + " million ";
    }
    
    const n_digit = number - nMillion * 1000000;
    
    if (n_digit < 1000000 && n_digit > 9999) {
        return front + thousand(n_digit);
    } else if (n_digit < 1000 && n_digit > 99) {
        return front + threeDigit(n_digit);
    } else if (n_digit < 100 && n_digit > 9) {
        return front + twoDigit(n_digit);
    } else if (n_digit < 10 && n_digit > 0) {
        return front + singleDigit(n_digit);
    } else {
        return front;
    }
}

function hasDecimal(inputValue){
    // Convert the input value to a string
    const stringValue = inputValue.toString();

    // Check if the string contains a period
    return stringValue.includes('.');
}

function run(digit, number) {	
    if (digit === 1) {
        return singleDigit(number);
    } else if (digit === 2) {
        return twoDigit(number);
    } else if (digit === 3) {
        return threeDigit(number);
    } else if (digit >= 4 && digit <= 6) {
        return thousand(number);
    } else if (digit >= 7 && digit <= 9) {
        return million(number);
    } else {
        return "Over Billion";
    }
}

function decimalF(number){
    var front = " Point ";
    var dec = String(parseFloat(number)).substring(2);
    const num_dec = dec.length;
    var array_num = dec.split('');
	var output = '';
    for (let i = 0; i < num_dec; i++) {
        if (array_num[i] == 0){
            output += "zero "
        } else {
            output += singleDigit(parseInt(array_num[i])) + " ";
        }
    }
    var result = front + output;
	output = '';
    return result;
}

function getDecimal(number){
    // Convert the input number to a string
    var numberString = String(number);

    // Check if the number has a decimal point
    if (numberString.indexOf('.') !== -1) {
        // Extract the decimal part using substring
        var decimalPart = numberString.split('.')[1];
        return parseFloat("0." + decimalPart);
    } else {
        // If there is no decimal point, return 0
        return 0;
    }
}

// button
function submitForm() {
    var userInputElement = document.getElementById('userInput');
    var resultElement = document.getElementById('result');
    var output = "";

    // Access the value of the input element
    var userInputValue = userInputElement.value;
    const num_digits = String(parseInt(userInputValue)).length;

    if (userInputValue < 0) {
        output = "Not Support Negative Number";
    } else if (userInputValue == ''){
        output = "Empty Input";
    } else if (userInputValue == 0) {
        output = "Zero";
    } else if (userInputValue < 1){
        let dOutput = decimalF(userInputValue);
        output = "Zero" + dOutput;
    } else {
		if (hasDecimal(userInputValue)){
			var decimal = getDecimal(userInputValue);
            let dOutput = decimalF(decimal);
			output = run(num_digits, parseInt(userInputValue)) + dOutput;
        } else {
		    output = run(num_digits, parseInt(userInputValue));
        }
    }
    // Update the result element
	output = specialNum(userInputValue, output);
    resultElement.textContent = userInputValue + ' <---> ' + output;
	document.getElementById('userInput').value = "";
}

function specialNum(number, output) {
    var pi = 3.14;
    var e = 2.71828;
    var gravity = 9.81;
    var c = 299792458; //Speed of Light (c):
	var sqrt2 = 1.414;
	var phi = 1.618;
	
    if (number == pi) {return '\u03C0: ' + output;}
    if (number == e) {return "Euler's e: " + output;}
    if (number == gravity) {return "Gravity: " + output;}
    if (number == c) {return "Speed of Light (c): " + output;}
	if (number == sqrt2) {return "square root of 2: " + output;}
	if (number == phi) {return "Golden-Ratio " + '\u03C6: ' + output;}
	return output;
}