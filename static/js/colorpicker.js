$(document).ready(function(){
    var colorButton = $(".colorList li");

    colorButton.on("click", function(){
        $(".colorList > li").removeClass("active-color");

        $(this).addClass("active-color");

        var newColor = $(this).attr("data-color");
        
        $(".mypage_banner").css("background-color", newColor);
    })
})