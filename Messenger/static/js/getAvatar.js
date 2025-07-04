function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + encodeURIComponent(value || "") + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i=0;i < ca.length;i++) {
        let c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length));
    }
    return null;
}

$(document).ready(function () {
    const avatar = getCookie("avatar");

    if (!avatar) {
        $.ajax({
            url: '/get_avatar/',
            method: 'GET',
            success: function (response) {
                setCookie('avatar', response.avatar, 7);
                $('#selfAvatar').attr('src', response.avatar);
            }
        });
    } else {
        $('#selfAvatar').attr('src', avatar);
    }
});
