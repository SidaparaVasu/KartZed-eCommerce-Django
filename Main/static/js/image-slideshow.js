// Get the DOM elements for the slider
var slides = document.querySelectorAll(".slides img");
var dots = document.querySelectorAll(".image-dots");
var prevBtn = document.querySelector(".prev");
var nextBtn = document.querySelector(".next");

// Set up variables to keep track of the current slide index
var slideIndex = 1;

// Function to show the slide with the given index and hide all others
function showSlide(index) {
  // If index is greater than the number of slides, loop back to the beginning
  if (index > slides.length) {
    slideIndex = 1;
  }
  // If index is less than 1, loop to the end
  if (index < 1) {
    slideIndex = slides.length;
  }
  // Hide all slides and dots
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (var i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  // Show the current slide and dot
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// Function to advance to the next slide and show it
function nextSlide() {
  showSlide(slideIndex += 1);
}

// Function to go back to the previous slide and show it
function prevSlide() {
  showSlide(slideIndex -= 1);
}

// Add event listeners for the prev and next buttons
prevBtn.addEventListener("click", prevSlide);
nextBtn.addEventListener("click", nextSlide);

// Show the first slide
showSlide(slideIndex);
