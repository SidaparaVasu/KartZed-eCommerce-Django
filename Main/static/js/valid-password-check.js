// Check if the entered password meets the requirements
function checkPassword(event) {
    const password = document.getElementById('password').value;
    const uppercaseRegex = /[A-Z]/;
    const lowercaseRegex = /[a-z]/;
    const digitsRegex = /[0-9]/;
    const passwordInput = document.getElementById('password');
    const passwordMessage = document.getElementById('password-message');

    if (password.length < 8 || password.length > 12) {
        passwordMessage.innerHTML = 'Password must be between 8 and 12 characters.';
        passwordMessage.style.color = '#f70500';
        event.preventDefault(); // Prevent form submission
    } else if (!password) {
        passwordMessage.innerHTML = 'Password cannot be blank.';
        passwordMessage.style.color = '#f70500';
        event.preventDefault(); // Prevent form submission
    } else if (!uppercaseRegex.test(password) || !lowercaseRegex.test(password) || !digitsRegex.test(password)) {
        passwordMessage.innerHTML = 'Password must contain at least one uppercase letter, one lowercase letter, and one digit.';
        passwordMessage.style.color = '#f70500';
        event.preventDefault(); // Prevent form submission
    } else {
        passwordMessage.innerHTML = 'Password is valid.';
        passwordMessage.style.color = '#f70500';
    }
}

// Attach the submit event to the form
document.getElementById('register-vendor-form').addEventListener('submit', checkPassword);