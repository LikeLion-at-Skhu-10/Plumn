function changebtnName() {
  const btnElement = document.getElementById("follow_btn");

  if (btnElement.innerText == "구독") {
    btnElement.innerText = "구독중";
  } else {
    btnElement.innerText = "구독";
  }
}

// function changebtnName() {
//   const btnElement = document.getElementById("follow_btn");
//   btnElement.innerText = "구독중";
// }
