document.getElementById("signupform").addEventListener('submit',function(event){
    event.preventDefault();
    const username = document.getElementById('id_username').value;
    const password = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;
    if(password != password2){
        event.preventDefault();
        document.getElementById('message').innerText = "Passwords do not match. Please try again.";
        document.getElementById('message').classList.remove('alert-success');
        document.getElementById('message').classList.add('alert-danger');
        return;
    }else{
        document.getElementById('message').innerText = "";
    }

    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordPattern.test(password)) {
        document.getElementById('message').innerText = "Password must be at least 8 characters long and contain both letters and numbers.";
        document.getElementById('message').classList.remove('alert-success');
        document.getElementById('message').classList.add('alert-danger');
        return;
    }
    document.getElementById('message').innerText = "";

    const data = {
        username : username,
        password : password,
    };

    fetch('/api/register/' , {
        method:'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if(data.message){
            document.getElementById('message').innerText = data.message;
            document.getElementById('message').classList.remove('alert-danger');
            document.getElementById('message').classList.add('alert-success');

            const loginLink = document.createElement('a');
            loginLink.href =  loginUrl;
            loginLink.innerText = "Login Now";
            document.getElementById('message').appendChild(loginLink);
        }
        else if (data.username || data.password) {
            let errorMessage = '';
            if (data.username) {
                errorMessage += data.username.join(', ') + '. ';
            }
            if (data.password) {
                errorMessage += data.password.join(', ') + '.';
            }
            document.getElementById('message').innerText = errorMessage;
            document.getElementById('message').innerText = errorMessage;
            document.getElementById('message').classList.remove('alert-success');
            document.getElementById('message').classList.add('alert-danger');
        } else {
            document.getElementById('message').innerHTML = 'Error: ' + JSON.stringify(data);
            document.getElementById('message').innerHTML = 'Error: ' + JSON.stringify(data);
            document.getElementById('message').classList.remove('alert-success');
            document.getElementById('message').classList.add('alert-danger');
        }
    })
    .catch(error => {
        document.getElementById('message').innerText = 'An error occurred: ' + error;
    });
});