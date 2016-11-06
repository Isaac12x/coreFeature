

var info = {};
var selectId;

var carPicFront = document.getElementById("carPicFront");
var carPicBack = document.getElementById("carPicBack");

function whatClicked(evt) {
	selectId = evt.target.id;
	if(selectId != "imgFront" && selectId != "imgBack") {
		$('#setValue').modal('show');
	}
}

carPicFront.addEventListener("click", whatClicked, false);
carPicBack.addEventListener("click", whatClicked, false);

function saveData() {

	info[selectId] = Math.floor(parseFloat($('#rate').swidget().value()) * 10);

	$('#setValue').modal('hide');
}

function generateHTML(firstValue, secondValue) {
	return "<tr><td>" + firstValue + "</td><td>" + secondValue + "</td></tr>";
}

function insertItem(firstValue, secondValue) {
	return {"Damage Parts" : firstValue, "Damage Rating" : secondValue.toString() };
}
			
function addItem() {
	if(Object.keys(info).length < 1) {
		return false;
	}
	else {

		var data = [];
		// $("addItemList").empty();
		
		for(var item in info) {
			// var htmlText = generateHTML(item, info[item]);
			// $("addItemList").append(htmlText);
			data.push(insertItem(item, info[item] / 10.0));
		}

		$('#summarise').dataTable().fnClearTable();
		$('#summarise').dataTable().fnAddData(data);

		return true;
	}
}