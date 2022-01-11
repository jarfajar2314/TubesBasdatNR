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

  $.urlParam = function (name) {
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results == null) {
      return null;
    }
    return decodeURI(results[1]) || 0;
  }

  $.urlParam('coll')

  if ($.urlParam('coll') == "driver") {
    $("#formUser").remove();
    $("#formMerchant").remove();
    $("#formPromo").remove();
  }
  if ($.urlParam('coll') == "user") {
    $("#formDriver").remove();
    $("#formMerchant").remove();
    $("#formPromo").remove();
  }
  if ($.urlParam('coll') == "merchant") {
    $("#formUser").remove();
    $("#formDriver").remove();
    $("#formPromo").remove();
  }
  if ($.urlParam('coll') == "promo") {
    $("#formUser").remove();
    $("#formMerchant").remove();
    $("#formDriver").remove();
  }

})(jQuery);

var getUrlParameter = function getUrlParameter(sParam) {
  var sPageURL = window.location.search.substring(1),
    sURLVariables = sPageURL.split('&'),
    sParameterName,
    i;

  for (i = 0; i < sURLVariables.length; i++) {
    sParameterName = sURLVariables[i].split('=');

    if (sParameterName[0] === sParam) {
      return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
    }
  }
  return false;
};
