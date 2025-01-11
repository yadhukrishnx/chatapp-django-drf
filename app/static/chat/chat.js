

    document.getElementById("chat-form").addEventListener("submit", function(e) {
        e.preventDefault();
        const token = document.getElementById("token").value; 
        console.log(token);
        var userMessage = document.getElementById("user-message").value;
        if (!userMessage.trim()) return;

        appendUserMessage(userMessage);

        document.getElementById("user-message").value = '';
        
        sendMessageToAPI(userMessage, token);
    });

    function appendUserMessage(message) {
        // Create user message HTML element
        
        var userMessageDiv = document.createElement("div");
        
        userMessageDiv.classList.add("chat-message-right", "pb-4");
        userMessageDiv.innerHTML = `
            <div class="d-flex justify-content-end align-items-start">
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
                    <div class="font-weight-bold mb-1">You</div>
                    ${message}
                </div>
                <div>
                    <img id="userimg" src="https://cdn-icons-png.flaticon.com/512/3177/3177440.png" class="rounded-circle mr-1"  width="35" height="35">
                    <div class="text-muted small text-nowrap mt-2">Just now</div>
                </div>
            </div>
        `;
        document.getElementById("chat-history").appendChild(userMessageDiv);
        scrollToBottom();
    }

    function appendBotReply(response) {
        // Create bot reply HTML element
        var botReplyDiv = document.createElement("div");
        botReplyDiv.classList.add("chat-message-left", "pb-4");
        botReplyDiv.innerHTML = `
            <div class="d-flex">
                <div>
                    <img id="botimg" src="https://cdn-icons-png.flaticon.com/512/924/924915.png" class="rounded-circle mr-1"  width="35" height="35">
                    <div class="text-muted small text-nowrap mt-2">Just now</div>
                </div>
                <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                    <div class="font-weight-bold mb-1">Sharon Lessman</div>
                    ${response}
                </div>
            </div>
        `;
        document.getElementById("chat-history").appendChild(botReplyDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        var chatHistory = document.getElementById("chat-history");
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
    
    function sendMessageToAPI(userMessage, token) {
        console.log(token);
        
        fetch('http://127.0.0.1:8000/api/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token,
              
                
            },
            body: JSON.stringify({
                "message": userMessage
            })
        })
        .then(response => response.json())
        .then(data => {
            // Handle the AI response
            if (data.response) {
                appendBotReply(data.response);
            } else {
                appendBotReply("Sorry, there was an issue with your request.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            appendBotReply("An error occurred. Please try again.");
        });
    }
