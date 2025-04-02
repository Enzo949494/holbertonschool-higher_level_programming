// Select the element with id "red_header" and the header element
const redHeaderButton = document.getElementById('red_header');
const header = document.querySelector('header');

// Add a click event listener to the red_header element
redHeaderButton.addEventListener('click', function() {
  // Change the header's text color to red (#FF0000)
  header.style.color = '#FF0000';
});
