$(document).ready(function () {
  $("#feedback").on("keyup", function () {
    $("#feedback_cnt").html("(" + $(this).val().length + " / 1000)");

    if ($(this).val().length > 1000) {
      $(this).val($(this).val().substring(0, 1000));
      $("#feedback_cnt").html("(1000 / 1000)");
    }
  });
});
