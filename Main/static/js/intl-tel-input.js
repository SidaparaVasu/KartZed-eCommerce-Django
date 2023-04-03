
// Initialize the intl-tel-input plugin

function getIp(callback) {
    fetch('https://ipinfo.io/json?token=<your token>', { headers: { 'Accept': 'application/json' }})
    .then((resp) => resp.json())
    .catch(() => {
        return {
            // The plugin defaults to the INDIA,
            country: 'in',
    };
    })
    .then((resp) => callback(resp.country));
}


const phoneInputField1 = document.querySelector(".login-input");
const phoneInputField2 = document.querySelector(".signup-input");

const phoneInput1 = window.intlTelInput(phoneInputField1, {
    initialCountry: "auto",
    geoIpLookup: getIp,
    preferredCountries: ["in"],
    utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

const phoneInput2 = window.intlTelInput(phoneInputField2, {
    initialCountry: "auto",
    geoIpLookup: getIp,
    preferredCountries: ["in"],
    utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});