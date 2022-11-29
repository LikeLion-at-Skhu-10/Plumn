var menu = document.getElementById("menu__container");
var toggle = document.getElementById("menu__box");
var checkbox = document.getElementById("checkbox");
var button = document.getElementById("notification_button");
var notif = document.getElementsByClassName("notif_container")[0];


function menutoggle(){
    document.getElementById("menu__box").classList.toggle("menu");
    menu.style.display = "block";
    if (document.getElementById("menu__box").className == ""){
        menu.style.display = "none";
    }
}

window.onclick = function(event) {
    if (event.target == menu) {
        menu.style.display = "none";
        toggle.className = "";
        checkbox.checked = false;
    }
}

function notification() {
    button.classList.toggle("toggle");
    notif.style.display = "inline";
    if (button.className == ""){
        notif.style.display = "none";
    }
}