const buttonsDots = document.getElementsByClassName("dots")
const modalWindowsDelEdit = document.querySelectorAll("#modal-del-edit")
// console.log(buttonsDots)

for (let count = 0; count < buttonsDots.length; count++) {
    const button = buttonsDots[count]
    console.log(button)
    button.addEventListener(
        "click",
        (event) => {
            let modal = modalWindowsDelEdit[count]
            console.log(modal)
            if (modal.classList[0] == "modal-del-edit"){
                modal.classList.replace("modal-del-edit", "show-modal-del-edit")
            }
            else{
                modal.classList.replace("show-modal-del-edit", "modal-del-edit")
            }
        }
    )
}