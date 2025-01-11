document.getElementById("signupform").addEventListener('submit',function(event){
    event.preventDefault();
    const username = document.getElementById('id_username').value;
    const password1 = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;
    if(password1 != password2){
        event.preventDefault();
        document.getElementById('message').innerText =
    }
})