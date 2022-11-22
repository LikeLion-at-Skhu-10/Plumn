// function contentsView(objVlaue) {
//   if (objVlaue.value == "money1000") {
//     $(".fillinWrap1").css("display", "block");
//     $(".fillinWrap2").css("display", "none");
//     $(".fillinWrap3").css("display", "none");
//     $(".fillinWrap4").css("display", "none");
//     $(".fillinWrap5").css("display", "none");
//     return false;
//   }
//   if (objVlaue.value == "money2000") {
//     $(".fillinWrap1").css("display", "none");
//     $(".fillinWrap2").css("display", "block");
//     $(".fillinWrap3").css("display", "none");
//     $(".fillinWrap4").css("display", "none");
//     $(".fillinWrap5").css("display", "none");
//     return false;
//   }
//   if (objVlaue.value == "money3000") {
//     $(".fillinWrap1").css("display", "none");
//     $(".fillinWrap2").css("display", "none");
//     $(".fillinWrap3").css("display", "block");
//     $(".fillinWrap4").css("display", "none");
//     $(".fillinWrap5").css("display", "none");
//     return false;
//   }
//   if (objVlaue.value == "money5000") {
//     $(".fillinWrap1").css("display", "none");
//     $(".fillinWrap2").css("display", "none");
//     $(".fillinWrap3").css("display", "none");
//     $(".fillinWrap4").css("display", "block");
//     $(".fillinWrap5").css("display", "none");
//     return false;
//   }
//   if (objVlaue.value == "money10000") {
//     $(".fillinWrap1").css("display", "none");
//     $(".fillinWrap2").css("display", "none");
//     $(".fillinWrap3").css("display", "none");
//     $(".fillinWrap4").css("display", "none");
//     $(".fillinWrap5").css("display", "block");
//     return false;
//   }
// }

function setDisplay() {
  if ($("input:radio[id=r1]").is(":checked")) {
    $("#fillinWrap2").hide();
    $("#fillinWrap3").hide();
    $("#fillinWrap4").hide();
    $("#fillinWrap5").hide();
    $("#fillinWrap1").show();
  } else if ($("input:radio[id=r2]").is(":checked")) {
    $("#fillinWrap1").hide();
    $("#fillinWrap3").hide();
    $("#fillinWrap4").hide();
    $("#fillinWrap5").hide();
    $("#fillinWrap2").show();
  } else if ($("input:radio[id=r3]").is(":checked")) {
    $("#fillinWrap1").hide();
    $("#fillinWrap2").hide();
    $("#fillinWrap4").hide();
    $("#fillinWrap5").hide();
    $("#fillinWrap3").show();
  } else if ($("input:radio[id=r4]").is(":checked")) {
    $("#fillinWrap1").hide();
    $("#fillinWrap2").hide();
    $("#fillinWrap3").hide();
    $("#fillinWrap5").hide();
    $("#fillinWrap4").show();
  } else if ($("input:radio[id=r5]").is(":checked")) {
    $("#fillinWrap1").hide();
    $("#fillinWrap2").hide();
    $("#fillinWrap3").hide();
    $("#fillinWrap4").hide();
    $("#fillinWrap5").show();
  }
}
