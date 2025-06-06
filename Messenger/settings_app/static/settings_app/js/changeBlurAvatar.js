const btnEditSave1 = document.getElementById("edit-avatar-btn")
const pEditSave1 = document.getElementById("edit-save-avatar-p")

const fileInput = document.getElementsByClassName('avatar')[0];
const avatar = document.getElementsByClassName('profile-card-img')[0];

fileInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();

        reader.addEventListener('load', function () {
            avatar.src = reader.result;
        });

        reader.readAsDataURL(file);
    }
});

  btnEditSave1.addEventListener(
    'click',
    function () {
        console.log(11)
        const p = document.getElementById("change-avatar")
        const label = document.getElementById("label-avatar")
        // 
        console.log(p, label)
        if (p.className === "notediting") {
            p.className = "change-avatar"
        }
        else {
            p.className = "notediting"
        }
        
        if (label.className === "notediting") {
            label.className = "label-avatar"
        }
        else {
            label.className = "notediting"
        }

        if (this.value == "change-avatar-edit") {
            pEditSave1.textContent = "Зберегти"
            btnEditSave1.value = "change-avatar-save"
        }
        else if (this.value == "change-avatar-save") {
            btnEditSave1.type = "submit"
        }
    }
)