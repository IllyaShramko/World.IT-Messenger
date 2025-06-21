
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
        else {
            messagesDiv.insertAdjacentHTML(
                `beforeend`,
                `
                <div class="all-messages-message messa">
                    <div>
                        <div class="companion-message-outside">
                            <img src="${message.avatar}">
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
        const allMessages = document.querySelector('.content');
        if (allMessages) {
            allMessages.scrollTop = allMessages.scrollHeight;
        }
    }
};
// 
let messageForm = document.getElementById("message");
// 

messageForm.addEventListener(
    type = "submit",
    function (event) {
        event.preventDefault();
        
        let dataMessage =document.getElementById("messageInput").value;
        if (dataMessage != "") {
            document.getElementById("messageInput").value = ""
            webSocket.send(JSON.stringify({
                'message': dataMessage
            }))
        }
    }
    
)