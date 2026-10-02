<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Chatbox</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="chat-container">

        <div class="chat-header">
            <div>
                <h2>Mi Chatbox</h2>
                <span> En línea</span>
            </div>
        </div>
 
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <p> Hola Cómo puedo ayudarte</p>
            </div>
        </div>

        <div class="chat-input">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Escribe un mensaje..."
                autocomplete="off"
            >

            <button id="sendButton">
                Enviar
            </button>
        </div>

    </div>

    <script src="script.js"></script>
</body>
</html>
2. style.css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f0f2f5;
}

.chat-container {
    width: 400px;
    height: 600px;
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
}

.chat-header {
    background: #24292f;
    color: white;
    padding: 20px;
}

.chat-header h2 {
    margin-bottom: 5px;
}

.chat-header span {
    color: #7ee787;
    font-size: 14px;
}

.chat-messages {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    background: #f6f8fa;
}

.message {
    max-width: 75%;
    margin-bottom: 15px;
    padding: 12px 15px;
    border-radius: 15px;
    word-wrap: break-word;
}

.message p {
    margin: 0;
}

.bot {
    background: #e1e4e8;
    color: #24292f;
    align-self: flex-start;
    border-bottom-left-radius: 3px;
}

.user {
    background: #0969da;
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 3px;
}

.chat-input {
    display: flex;
    padding: 15px;
    background: white;
    border-top: 1px solid #ddd;
    gap: 10px;
}

.chat-input input {
    flex: 1;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 8px;
    outline: none;
}

.chat-input input:focus {
    border-color: #0969da;
}

.chat-input button {
    border: none;
    background: #0969da;
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
    cursor: pointer;
}

.chat-input button:hover {
    background: #055bb5;
}

@media (max-width: 500px) {
    .chat-container {
        width: 95%;
        height: 90vh;
    }
}
3. script.js
const input = document.getElementById("messageInput");
const button = document.getElementById("sendButton");
const messages = document.getElementById("chatMessages");

function enviarMensaje() {

    const texto = input.value.trim();

    if (texto === "") {
        return;
    }

    // Mensaje del usuario
    const mensajeUsuario = document.createElement("div");
    mensajeUsuario.classList.add("message", "user");

    mensajeUsuario.innerHTML = `<p>${texto}</p>`;

    messages.appendChild(mensajeUsuario);

    input.value = "";

    messages.scrollTop = messages.scrollHeight;

    // Respuesta automática
    setTimeout(() => {

        const respuesta = document.createElement("div");
        respuesta.classList.add("message", "bot");

        respuesta.innerHTML = `
            <p>Gracias por tu mensaje. 😊</p>
        `;

        messages.appendChild(respuesta);

        messages.scrollTop = messages.scrollHeight;

    }, 700);
}

button.addEventListener("click", enviarMensaje);

input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        enviarMensaje();
    }

});
Estructura del proyecto
chatbox/
│
├── index.html
├── style.css
└── script.js
