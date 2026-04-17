//Source: https://www.w3schools.com/w3css/w3css_tabulators.asp
function openCode(codeName) {
  var i;
  var x = document.getElementsByClassName("code");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  document.getElementById(codeName).style.display = "block";  
}