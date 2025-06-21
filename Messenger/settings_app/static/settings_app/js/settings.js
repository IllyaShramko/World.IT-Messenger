btnEditSave = document.getElementById("edit-save-btn")
pEditSave = document.getElementById("edit-save-p")
blurInfo = document.getElementsByClassName("notedit")[0]
console.log(btnEditSave.value)

btnEditSave.addEventListener(
    'click',
    function () {
        if (this.value == "editinfo") {
            blurInfo.classList.toggle("edit")
            pEditSave.textContent = "Зберегти"
            btnEditSave.value = "save"
            console.log("working")
        }
        else if (this.value == "save") {
            btnEditSave.type = "submit"
        }
    }
)
