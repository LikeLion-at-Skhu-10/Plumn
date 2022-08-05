// 커버 배경색 변경 js

const container = document.getElementById("container");
const colors = [
  "#ffafb0",
  "#f2cfa5",
  "#fdfa87",
  "#afffba",
  "#e2ffaf",
  "#c4f4fe",
  "#aee4ff",
  "#dfd4e4",
  "#caa6fe",
];

container.style.backgroundColor = "white";
// btn.addEventListener("click", colorChange); // function 뒤에 ()가 없다.

function colorChange() {
  const colorIdx = parseInt(Math.random() * colors.length); // 순서를 랜덤으로 만들기
  container.style.backgroundColor = colors[colorIdx]; // 랜덤으로 배열 안의 컬러를 선택한다.
}

// 커버 이미지 변경 js

const coverImageBtn = document.querySelector(".cover_image_btn");
const inputCover = document.querySelector("#input-cover");

coverImageBtn.addEventListener("click", () => {
  inputCover.click();
});
