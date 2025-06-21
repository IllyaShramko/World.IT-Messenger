window.onload = function () {
    const allMessages = document.querySelector('.content');
    if (allMessages) {
        allMessages.scrollTop = allMessages.scrollHeight;
    }
};