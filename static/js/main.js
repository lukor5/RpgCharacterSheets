function dropCharacters(){
	document.getElementById("dropdownContent").classList.toggle("show");
}

window.onclick = function(e){
	if (!e.target.matches('#myCharacters')) {
		var dropdown = document.getElementById("dropdownContent");
			if(dropdown.classList.contains('show')) {
				dropdown.classList.remove('show');
			}
	}
}