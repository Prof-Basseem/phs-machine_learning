// when screen size is mobile, the navbar is hidden
// when screen size is desktop, the navbar is shown
// create a function to toggle the navbar
var btn_navbar = document.getElementById("btn-open");
var btn_close = document.getElementById("btn-close");
function toggleNavbar() {
    if (document.body.clientWidth < 768) {
        document.getElementById("navbar").style.display = "none";
        // hide btn_close   
        btn_close.style.display = "none";
    } else {
        document.getElementById("navbar").style.display = "block";
        btn_navbar.style.display = "none";
    }
}
// call the function when the window is resized
window.onresize = toggleNavbar;
// call the function when the page is loaded
window.onload = toggleNavbar;
// when the navbar button is clicked, toggle the navbar
btn_navbar.onclick = function () {
    document.getElementById("navbar").style.display = "block";
    document
    btn_navbar.style.display = "none";
    btn_close.style.display = "block";   
}
btn_close.onclick = function() {
    document.getElementById("navbar").style.display = "none";
    btn_navbar.style.display = "block";
    btn_close.style.display = "none";
}
////////////////////////////////////////////////////////
///////////move btn to up//////////
// create button move to top and hidden in top  of page when scroll down
var btn = document.createElement("button");
btn.innerHTML = "&#x25B2";
btn.style.position = "fixed";
btn.style.bottom = "20px";
btn.style.right = "20px";
btn.style.fontSize = "14px";
btn.style.border = "2px solid #ffffff";
btn.style.zIndex = "2";
btn.style.backgroundColor = "#007BFF";
btn.style.color = "white";
btn.style.padding = "5px";
btn.style.borderRadius = "50%";
btn.style.cursor = "pointer";
btn.style.fontFamily = "tahoma";
// create event click for button dissaper if in top and appear if scroll down
btn.onclick = function() {
    window.scrollTo(0, 0);
    }
document.body.appendChild(btn);
window.onscroll = function() {
    if (window.pageYOffset > 70) {
        btn.style.display = "block";
    } else {
        btn.style.display = "none";
    }
}
