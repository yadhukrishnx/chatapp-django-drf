
// Login

document.getElementById("loginform").addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = {
        username: username,
        password: password,
    };

    console.log(data)
    
    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            window.location.href = data.chat_url; 
            console.log(data.chat_url)
        } else {
            // Show error message
            document.getElementById('message').innerHTML = "Invalid credentials";
        }
    })
    .catch(error => {
        const messageDiv = document.getElementById('message');
        messageDiv.innerText = 'An error occurred: ' + error;
        messageDiv.classList.remove('alert-success');
        messageDiv.classList.add('alert-danger');
    });
});