function updateTextInput(val) {
          document.getElementById('textInput').value=val; 
        }

function updateRangeInput(val) {
          document.getElementById('rangeInput').value=val; 
        }

function hideElem(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}