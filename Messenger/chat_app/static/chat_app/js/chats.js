
const groupPk = document.getElementById("groupPk").value;
//
const webSocket = new WebSocket(`ws://${window.location.host}/chats/${groupPk}`);

let user = document.getElementById("user").value

console.log(user)

webSocket.onmessage = function(event) {
    let data = JSON.parse(event.data)
    
    if (data.type === 'chat'){
        let message = data.message;
        let author = message.author
        console.log(author)
        // console.log();
        let messagesDiv = document.getElementById("messeges");
        if (user == author) {
            if (message.attached_image) {
                messagesDiv.insertAdjacentHTML(
                    "beforeend",
                    `
                        <div class="all-messages-message-my messa">
                            <div>
                                <div class="my-message">
                                    <h2>${message.message}</h2>
                                    <img src="${message.attached_image}">
                                    <div class = "check-message">
                                        <p>10:01</p>
                                        <img src="{% static 'chat_app/images/arrow.png' %}">
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                );
            }
            else {
                messagesDiv.insertAdjacentHTML(
                    "beforeend",
                    `
                        <div class="all-messages-message-my messa">
                            <div>
                                <div class="my-message">
                                    <h2>${message.message}</h2>
                                    <div class = "check-message">
                                        <p>10:01</p>
                                        <img src="{% static 'chat_app/images/arrow.png' %}">
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                );
            }
        }
        else {
            if (message.attached_image) {
                messagesDiv.insertAdjacentHTML(
                    `beforeend`,
                    `
                    <div class="all-messages-message messa">
                        <div>
                            <div class="companion-message-outside">
                                <img src="${message.avatar}"  class="avatar-companion">
                                <div class="companion-message">
                                    <div class="all-message-message-content">
                                        <h2 class="">${message.authorname}</h2>
                                        <p>${message.message}</p>
                                        <img src="${message.attached_image}">
                                    </div>
                                    <div class="all-message-message-info">
                                        <p>
                                            10:30
                                        </p>
                                        <img src="{% static 'chat_app/images/arrow.png' %}">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    `
                )   
            }
            else {
                messagesDiv.insertAdjacentHTML(
                    `beforeend`,
                    `
                    <div class="all-messages-message messa">
                        <div>
                            <div class="companion-message-outside">
                                <img src="${message.avatar}" class="avatar-companion">
                                <div class="companion-message">
                                    <div class="all-message-message-content">
                                        <h2 class="">${message.authorname}</h2>
                                        <p>${message.message}</p>
                                    </div>
                                    <div class="all-message-message-info">
                                        <p>
                                            10:30
                                        </p>
                                        <img src="{% static 'chat_app/images/arrow.png' %}">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    `
                )   
            }
        }
        const allMessages = document.querySelector('.content');
        if (allMessages) {
            allMessages.scrollTop = allMessages.scrollHeight;
        }
    }
};
// 
let messageForm = document.getElementById("message");
// 
// const messageForm = document.getElementById("messageForm");
const fileInput = document.getElementById("attachedImg");
const messageInput = document.getElementById("messageInput");
const blockImages = document.querySelector(".attached_images");

messageForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const messageText = messageInput.value.trim();
    const file = fileInput.files[0];
    if (file){
        const reader = new FileReader();
        reader.onload = function(event){
            webSocket.send(JSON.stringify({
                'message': messageText,
                'img':reader.result.split(',')[1],
                'imgType':file.type.split('/')[1]
            }))
            document.getElementById("attaImg").src = ''
        }
        reader.readAsDataURL(file)  
    }
    else{

        webSocket.send(JSON.stringify({
            'message': messageText
        }))
    }

    messageInput.value = "";
    fileInput.value = "";
    blockImages.innerHTML = "";
});

fileInput.addEventListener("change", function (event) {
    const files = event.target.files;
    blockImages.innerHTML = "";

    for (let i = 0; i < files.length; i++) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imageDiv = document.createElement("div");
            const imageElement = document.createElement("img");

            imageDiv.className = "attached-img";
            imageElement.src = e.target.result;

            imageDiv.appendChild(imageElement);
            blockImages.appendChild(imageDiv);
        };
        reader.readAsDataURL(files[i]);
    }
});
function getCSRFToken() {
    const name = "csrftoken";
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + "=")) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return "";
}
