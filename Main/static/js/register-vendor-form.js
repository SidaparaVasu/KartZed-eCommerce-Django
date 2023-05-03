const form = document.getElementById('register-vendor-form');
const submitButton = document.getElementById('submit-btn');
const displayNameInput = document.getElementById('displayname');
const mobileNumberInput = document.getElementById('mobileno');
const emailAddressInput = document.getElementById('emailid');
const companyNameInput = document.getElementById('companyname');
const companyAddressInput = document.getElementById('companyaddr');
const companyContactInput = document.getElementById('companymobileno');
const gstinInput = document.getElementById('gstinno');
const pickupPincodeInput = document.getElementById('pickuppincode');
const pickupAddressInput = document.getElementById('pickupaddr');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent default form submission behavior
  if (validateForm()) {
    form.reset();
  }
});

// Validate the form inputs
function validateForm() {
  let isValid = true;
  const mobileNumberRegex = /^[6-9][0-9]{9}$/; // Regex for Indian mobile numbers
  // 24 AABCU 9603 R 1 ZT
  // const gstinRegex = /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z]{2}$/; // Regex for GSTIN

  // Validate display name
  if (displayNameInput.value.trim() === '') {
    displayNameInput.setCustomValidity('Please enter a display name');
    isValid = false;
  } else {
    displayNameInput.setCustomValidity('');
  }

  // Validate mobile number
  if (!mobileNumberRegex.test(mobileNumberInput.value)) {
    mobileNumberInput.setCustomValidity('Please enter a valid Indian mobile number');
    isValid = false;
  } else {
    mobileNumberInput.setCustomValidity('');
  }

  // Validate email address
  if (emailAddressInput.value.trim() === '') {
    emailAddressInput.setCustomValidity('Please enter an email address');
    isValid = false;
  } else {
    emailAddressInput.setCustomValidity('');
  }

  // Validate company name
  if (companyNameInput.value.trim() === '') {
    companyNameInput.setCustomValidity('Please enter a company name');
    isValid = false;
  } else {
    companyNameInput.setCustomValidity('');
  }

  // Validate company address
  if (companyAddressInput.value.trim() === '') {
    companyAddressInput.setCustomValidity('Please enter a company address');
    isValid = false;
  } else {
    companyAddressInput.setCustomValidity('');
  }

  // Validate company contact
  if (companyContactInput.value.trim() === '') {
    companyContactInput.setCustomValidity('Please enter a company contact');
    isValid = false;
  } else {
    companyContactInput.setCustomValidity('');
  }

  // Validate GSTIN
  if (!gstinRegex.test(gstinInput.value)) {
    gstinInput.setCustomValidity('Please enter a valid GSTIN');
    isValid = false;
  } else {
    gstinInput.setCustomValidity('');
  }

  // Validate pickup pincode
  if (pickupPincodeInput.value.trim() === '') {
    pickupPincodeInput.setCustomValidity('Please enter a pickup pincode');
    isValid = false;
  } else {
    pickupPincodeInput.setCustomValidity('');
  }

  // Validate pickup address
  if (pickupAddressInput.value.trim() === '') {
    pickupAddressInput.setCustomValidity('Please enter a pickup address');
    isValid = false;
  } else {
    pickupAddressInput.setCustomValidity('');
  }

  return isValid;
}
