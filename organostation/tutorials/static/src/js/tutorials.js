//Get the button
let mybutton = document.getElementById("btn-back-to-toc");
var toc = document.getElementById("toc");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.getElementById('toc').scrollIntoView();
  //document.body.scrollTop = 0;
  //document.documentElement.scrollTop = 0;
}
