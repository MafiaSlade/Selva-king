function signIn() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Make AJAX call to backend
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/signin', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    alert('Sign in successful!'); // Redirect to chatbot or do something else
                } else {
                    alert('Invalid username or password.');
                }
            } else {
                alert('Error: ' + xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify({ username: username, password: password }));
}
