const contentText = document.querySelector(".item_type_text");
const changeBold = document.querySelector(".js_change_boldtext");
const changeFont = document.querySelector(".js_change_font");
const fontColor = document.querySelector(".font_color");

document.querySelector(".js_change_boldtext").addEventListener("click", () => {
  contentText.classList.toggle("bold");
  changeBold.classList.toggle("bgcolor");
});

document.querySelector(".js_change_font").addEventListener("click", () => {
  contentText.classList.toggle("italic");
  changeFont.classList.toggle("bgcolor");
});

document.querySelector(".js_font_color").addEventListener("click", () => {
  fontColor.classList.toggle("reveal");
});

document.querySelector(".red").addEventListener("click", () => {
  contentText.classList.toggle("js_red");
});
document.querySelector(".blue").addEventListener("click", () => {
  contentText.classList.toggle("js_blue");
});
document.querySelector(".gray").addEventListener("click", () => {
  contentText.classList.toggle("js_gray");
});
