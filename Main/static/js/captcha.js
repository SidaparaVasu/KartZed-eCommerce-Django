// Generate a random alphanumeric string for the captcha
function generateCaptcha() {
    const chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let captcha = '';
    let length = 6;
    for (let i = 0; i < length; i++) {
        captcha += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return captcha;
}

// Display the captcha on the page
function displayCaptcha() {
    const captcha = generateCaptcha();
    document.getElementById('input-captcha').value = '';
    document.getElementById('captcha-message').innerHTML = '';
    document.getElementById('show-captcha').innerHTML = captcha;
}

// Check if the entered captcha is correct
function checkCaptcha() {
    const enteredCaptcha = document.getElementById('input-captcha').value;
    const captchaImage = document.getElementById('show-captcha').innerHTML;
    let submitBtn = document.getElementById('submit-btn');

    if (enteredCaptcha === captchaImage && enteredCaptcha == 111111) {
        document.getElementById('captcha-message').innerHTML = 'Captcha is correct.';
        document.getElementById('captcha-message').style.color = '#5D87FF';
        submitBtn.disabled = false;
    } else {
        displayCaptcha();
        document.getElementById('captcha-message').innerHTML = 'Captcha is incorrect. Please try again.';
        document.getElementById('captcha-message').style.color = '#f70500';
        submitBtn.disabled = true;
    }
}

// Display a new captcha on page load
window.onload = displayCaptcha;
