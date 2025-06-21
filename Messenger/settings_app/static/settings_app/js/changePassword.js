const btnEditSavePass = document.getElementById("edit-save-btn-pass")
const pEditSavePass = document.getElementById("edit-save-pass-p")

const containerInputsPass = document.getElementById('editpassdiv')
const blurInfopass = document.getElementsByClassName("notedit")[1]


// const blurInfopass

btnEditSavePass.addEventListener(
    'click',
    function () {
        if (this.value == "editpass") {
            blurInfopass.classList.toggle("edit")
            pEditSavePass.textContent = "Зберегти"
            btnEditSavePass.value = "savepass"
            console.log("working")  
            containerInputsPass.insertAdjacentHTML(
                'beforeend',
                `
                <div class="profile-password-edit input-edit">
                    <p>Повтори пароль</p>
                    <div>
                        <input type="password" name="passwordconfirm" id="pass22" required>
                        <button type="button" class="changevisibilitypass" id="pass2">
                            <img src="/static/settings_app/images/eye.svg">
                        </button>
                    </div>
                </div>
                `
            )
            const input1 = document.getElementById("pass11")
            const button1 = document.getElementById("pass1")
            const input2 = document.getElementById("pass22")
            const button2 = document.getElementById("pass2")
            button1.addEventListener(
                'click',
                function() {
                    if (input1.type == 'password') {
                        input1.type = "text"                   
                    }
                    else {
                        input1.type = "password"
                    }
                }
            )
            button2.addEventListener(
                'click',
                function() {
                    if (input2.type == 'password') {
                        input2.type = "text"                   
                    }
                    else {
                        input2.type = "password"
                    }
                }
                
            )
        }
        else if (this.value == "savepass") {
            btnEditSavePass.type = "submit"
        }
    }
)



