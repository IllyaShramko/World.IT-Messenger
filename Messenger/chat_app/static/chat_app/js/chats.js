
const groupPk = document.getElementById("groupPk").value;
//
const webSocket = new WebSocket(`ws://${window.location.host}/chat/${groupPk}`);

webSocket.onmessage = function(event) {
    let data = JSON.parse(event.data)
    
    if (data.type === 'chat'){
        let message = data.message;
        console.log(message.message);
        let messagesDiv = document.getElementById("messages");
        messagesDiv.innerHTML += `<div><p><b>${message.username}: </b>${message.message}</p>`;
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
        webSocket.send(JSON.stringify({
            'message': dataMessage
        }))
    }
    
)