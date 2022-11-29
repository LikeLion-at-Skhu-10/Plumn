let commentInput = document.getElementsByClassName("chat_comment")[0];
let commentBtn = document.getElementsByClassName("chat_button")[0];

function submit() {
  const box = document.getElementsByClassName("main_comment")[0];

  const comments = document.createElement("div");
  const userName = document.createElement("span");
  const mainText = document.createElement("p");
  const userImage = document.createElement("img");

  comments.classList.add("user_comment");
  userName.classList.add("chat_profile_name");
  userImage.classList.add("chat_profileImage");
  mainText.classList.add("commenting");

  userImage.setAttribute("src", "{% 'img/mylover.jpg' %}");

  userName.innerHTML = "PIKI";
  mainText.innertText = commentInput.value;

  comments.appendChild(userImage);
  comments.appendChild(userName);
  comments.appendChild(mainText);

  box.appendChild(comments);
}

commentBtn.addEventListener("click", () => {
  submit();
  commentInput.value = "";
});

commentInput.addEventListener("keydown", (event) => {
  if (event.code === "Enter") {
    submit();
    commentInput.value = "";
  }
});
