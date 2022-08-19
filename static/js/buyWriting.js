var modal = document.getElementById("charged_modal");
var modal2 = document.getElementById("buyCheck_modal");
var btn = document.getElementById("charged_writing");
var btn2 = document.getElementById("realBuy_btn");
var span = document.getElementsByClassName("closebtn")[0];
var span2 = document.getElementsByClassName("closebtn2")[0];

btn.onclick = function () {
  modal.style.display = "block";
};

btn2.onclick = function () {
  modal2.style.display = "block";
};

span.onclick = function () {
  modal.style.display = "none";
};

span2.onclick = function () {
  modal2.style.display = "none";
  modal.style.display = "none";
};

window.addEventListener("click", function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  } else if (event.target == modal2) {
    modal2.style.display = "none";
    modal.style.display = "none";
  }
});
