const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const btnLogin = document.querySelector("#Btnlogin");
/* const password_input = document.getElementById("id_password1")
password_input.classList.add("hola")
password_input.setAttribute.oninput(comprobarPassword(this)); */
sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

