function changebtnName() {
  const btnElement = document.getElementById("follow_btn");

  if (btnElement.innerText == "구독") {
    btnElement.style.background = '#FC9595';
    btnElement.style.color = '#fff';
    btnElement.innerText = "구독중";
  } else {
    btnElement.style.background = '#fff';
    btnElement.style.color = '#FC9595';
    btnElement.innerText = "구독";
  }
}
