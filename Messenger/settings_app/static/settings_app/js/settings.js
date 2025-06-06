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
            btnEditSave.value = "save"
            // // 
            // pChangeAvatar = document.createElement("p")
            // pChangeAvatar.className = "change-avatar"
            // // 
            // label = document.createElement("label")
            // label.setAttribute("for", document.getElementById("avatar"))
            // // 
            // div1 = document.createElement("div")
            // div2 = document.createElement("div")
            // img1 = 
            //
            console.log("working")
        }
        else if (this.value == "save") {
            btnEditSave.type = "submit"
        }
    }
)
