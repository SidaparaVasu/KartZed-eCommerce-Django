function popupLoginBox() {
    var element = document.getElementById("login-popup");
    element.classList.toggle("active-login-popup");
    document.body.style.overflowY = 'hidden';
}

function closeLoginBox() {
    var element = document.getElementById("login-popup");
    element.classList.remove("active-login-popup");
    document.body.style.overflowY = 'visible';
}