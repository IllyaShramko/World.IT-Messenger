btnEditSave = document.getElementById("edit-save-btn")
pEditSave = document.getElementById("edit-save-p")
blurInfo = document.getElementsByClassName("notedit")[0]
console.log(btnEditSave.value)

btnEditSave.addEventListener(
    'click',
    function () {
        if (this.value == "edit") {
            blurInfo.classList.toggle("edit")
            pEditSave.textContent = "Зберегти"
            console.log("working")
            btnEditSave.value = "save"
        }
        else if (this.value == "save") {
            btnEditSave.type = "submit"
        }
    }
)

