const header = document.querySelector("header");
const updateBtn = document.querySelector("#update_header");

updateBtn.addEventListener("click", () => {
    header.textContent = "New Header!!!";;
});