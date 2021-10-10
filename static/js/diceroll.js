function getDiceRoll(min, max) {
	document.getElementById('total').innerHTML = "Total: ";
	document.getElementById('rolls').innerHTML = "All rolls: ";
	min = Math.ceil(min);
	max = Math.floor(max);
	var count = document.getElementById('diceCount').value;
	const results = [];
	var i;
	var total = 0;
	for (i = 0; i < count; i++) {
		results.push(Math.floor(Math.random() * (max - min + 1)) + min);
	}
	results.forEach(printDiceRoll);
	function printDiceRoll(diceRoll, index, arr) {
		if (index < arr.length - 1) {
			document.getElementById('rolls').append(diceRoll, ", ");
			console.log(diceRoll);
			total += diceRoll;
		} else {
			document.getElementById('rolls').append(diceRoll);
			console.log(diceRoll);
			total += diceRoll;
		}
	}
	document.getElementById('total').append(total);
}

function checkNumberRange(number) {
	var id = number.id;
	var value = number.value;
	if (number.value > 10) {
		document.getElementById(id).value = 10;
		alert("Max range exceded - pick a number between 1 and 10")
	}
}