const btnEditSavePass = document.getElementById("edit-save-btn-pass")
const pEditSavePass = document.getElementById("edit-save-pass-p")

// const blurInfopass

btnEditSavePass.addEventListener(
    'click',
    function () {
        if (this.value == "edit") {
            blurInfopass.classList.toggle("edit")
            pEditSavePass.textContent = "Зберегти"
            btnEditSavePass.value = "savepass"
            console.log("working")
        }
        else if (this.value == "save") {
            btnEditSavePass.type = "submit"
        }
    }
)
