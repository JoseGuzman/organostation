//=========================================================================
// Function to hide/show the left side bar (menusidebar)
//=========================================================================

$('.mybtn').click(function () {
  $(this).toggleClass("click");
  $('.menusidebar').toggleClass("show");
});


$('.nav-link ul li a').click(function () {
  var id = $(this).attr('id');
  $('.nav-link ul li ul.item-show-' + id).toggleClass("show");
  $('.nav-link ul li #' + id + ' span').toggleClass("rotate");

});

$('.nav-link ul li').click(function () {
  $(this).addClass("active").siblings().removeClass("active");
});
