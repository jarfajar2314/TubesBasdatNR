(function($) {

	"use strict";

	$(".toggle-password").click(function() {

  $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
      input.attr("type", "text");
    } else {
      input.attr("type", "password");
    }
  });

  if ($("#check").attr("value") == 1) {
    $("#authWarn").removeClass("d-none");
  }
  else if ($("#check").attr("value") == 2) {
    $("#authWarn2").removeClass("d-none");
  }

  $("#loginBtn").click(function () { 
    $(this).text('Logging in..');
  });

  $("#btnD").click(function () { 
    $(this).removeClass("btn-outline-primary");
    $(this).addClass("btn-primary");
    $("#btnU").removeClass();
    $("#btnU").addClass("btn btn-outline-primary");
    $("#btnM").removeClass();
    $("#btnM").addClass("btn btn-outline-primary");
    $("#btnP").removeClass();
    $("#btnP").addClass("btn btn-outline-primary");
    $("#formDriver").removeClass("d-none");
    $("#formUser").addClass("d-none");
    $("#formMerchant").addClass("d-none");
    $("#formPromo").addClass("d-none");
  });
  $("#btnU").click(function () { 
    $(this).removeClass("btn-outline-primary");
    $(this).addClass("btn-primary");
    $("#btnD").removeClass();
    $("#btnD").addClass("btn btn-outline-primary");
    $("#btnM").removeClass();
    $("#btnM").addClass("btn btn-outline-primary");
    $("#btnP").removeClass();
    $("#btnP").addClass("btn btn-outline-primary");
    $("#formDriver").addClass("d-none");
    $("#formUser").removeClass("d-none");
    $("#formMerchant").addClass("d-none");
    $("#formPromo").addClass("d-none");
  });

  $("#btnM").click(function () {
    $(this).removeClass("btn-outline-primary");
    $(this).addClass("btn-primary");
    $("#btnU").removeClass();
    $("#btnU").addClass("btn btn-outline-primary");
    $("#btnD").removeClass();
    $("#btnD").addClass("btn btn-outline-primary");
    $("#btnP").removeClass();
    $("#btnP").addClass("btn btn-outline-primary");
    $("#formDriver").addClass("d-none");
    $("#formUser").addClass("d-none");
    $("#formMerchant").removeClass("d-none");
    $("#formPromo").addClass("d-none");
  });
  $("#btnP").click(function () {
    $(this).removeClass("btn-outline-primary");
    $(this).addClass("btn-primary");
    $("#btnU").removeClass();
    $("#btnU").addClass("btn btn-outline-primary");
    $("#btnD").removeClass();
    $("#btnD").addClass("btn btn-outline-primary");
    $("#btnM").removeClass();
    $("#btnM").addClass("btn btn-outline-primary");
    $("#formDriver").addClass("d-none");
    $("#formUser").addClass("d-none");
    $("#formMerchant").addClass("d-none");
    $("#formPromo").removeClass("d-none");
  });

})(jQuery);
