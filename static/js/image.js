// 커버 배경색 변경 js

const container = document.getElementById("container");
// const textArea = documnet.getElementById("title_write");

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
  // textArea.style.backgroundColor = colors[colorIdx];
}

// 커버 이미지 변경 js
document.querySelector(".cover_image_btn").addEventListener("click", () => {
  const realUpload = document.querySelector(".js-image");
  realUpload.click();
});

const imageInput = document.querySelector("#input-cover");
imageInput.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploadImage = reader.result;
    document.querySelector(
      ".title_img"
    ).style.backgroundImage = `url(${uploadImage})`;
  });
  reader.readAsDataURL(this.files[0]);
});
