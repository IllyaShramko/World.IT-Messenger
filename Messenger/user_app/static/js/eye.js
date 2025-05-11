let eyeButtonPassword = document.getElementById("password-eye")
let eyeInputPassword = document.getElementById("password-input")

let eyeButtonPasswordConfirm = document.getElementById("password-confirm-eye-button")
let eyeInputPasswordConfirm = document.getElementById("password-confirm-input")

eyeButtonPasswordConfirm.addEventListener('click', () => {
    if (eyeInputPasswordConfirm.type === 'password') {
        eyeInputPasswordConfirm.type = 'text';
    } else {
        eyeInputPasswordConfirm.type = 'password';
    }
})

eyeButtonPassword.addEventListener('click', () => {
    if (eyeInputPassword.type === 'password') {
        eyeInputPassword.type = 'text';
    } else {
        eyeInputPassword.type = 'password';
    }
})

