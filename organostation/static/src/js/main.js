//=========================================================================
// Function to hide/show the left side bar (menusidebar)
//=========================================================================

$('.mybtn').click(function () {
  $(this).toggleClass("click");
  $('.menusidebar').toggleClass("show");
});


$('.menusidebar ul li a').click(function () {
  var id = $(this).attr('id');
  $('.menusidebar ul li ul.item-show-' + id).toggleClass("show");
  $('.menusidebar ul li #' + id + ' span').toggleClass("rotate");

});

$('.menusidebar ul li').click(function () {
  $(this).addClass("active").siblings().removeClass("active");
});
