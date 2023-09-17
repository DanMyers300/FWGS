// script.js

document.addEventListener("DOMContentLoaded", function () {
    const chatMessages = document.getElementById("chat-messages");
    const userMessageInput = document.getElementById("user-message");
    const sendButton = document.getElementById("send-button");
    const saveButton = document.getElementById("save-button");

    let chatHistory = [];

    sendButton.addEventListener("click", () => {
        const userMessage = userMessageInput.value;
        addUserMessage(userMessage);

        // Simulate a bot response (replace with your actual bot logic)
        setTimeout(() => {
            const botResponse = "You said: " + userMessage;
            addBotMessage(botResponse);
            chatHistory.push({ user: "Bot", bot: botResponse });
        }, 1000);

        userMessageInput.value = "";
    });

    function addUserMessage(message) {
        const userMessageElement = document.createElement("p");
        userMessageElement.classList.add("user-message");
        userMessageElement.textContent = message;
        chatMessages.appendChild(userMessageElement);
    }

    function addBotMessage(message) {
        const botMessageElement = document.createElement("p");
        botMessageElement.classList.add("bot-message");
        botMessageElement.textContent = message;
        chatMessages.appendChild(botMessageElement);
    }

    function saveChatAsTextFile() {
        const textContent = chatHistory.map(entry => `${entry.user}\n${entry.bot}`).join("\n\n");
        const blob = new Blob([textContent], { type: "text/plain" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.style.display = "none";
        a.href = url;
        a.download = "chat_history.txt";
        document.body.appendChild(a);

        a.click();

        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    saveButton.addEventListener("click", saveChatAsTextFile);
});
