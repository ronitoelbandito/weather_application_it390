// JavaScript Document

document.addEventListener('DOMContentLoaded', (event) => {
  const signUpButtons = document.querySelectorAll('#sign-up, #sign-up-bottom');
  signUpButtons.forEach(button => {
    button.addEventListener('click', function() {
      alert('Thank you for signing up!');
      // Here you would probably open a sign-up modal or redirect to a sign-up page.
    });
  });
});


let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');
window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');
        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
};

var flexContainer = null;
    
var flexContainers = {}; // Object to hold flex containers

function toggleFlexbox(containerId) {
  var flexContainer = flexContainers[containerId];
  if (flexContainer) {
    // If flex container exists, remove it
    document.body.removeChild(flexContainer);
    flexContainers[containerId] = null;
  } else {
    // If flex container doesn't exist, create it
    createFlexbox(containerId);
  }
}

function createFlexbox(containerId) {
  // Create a div element for the flex container
  var flexContainer = document.createElement("div");
  flexContainer.classList.add("report-cards");
  flexContainers[containerId] = flexContainer;

  // Create sample text items
  for (var i = 0; i < 4; i++) {
    var flexItem = document.createElement("div");
    flexItem.classList.add("report-card");
    flexItem.textContent = "Sample Text " + (i + 1);
    flexContainer.appendChild(flexItem);
  }

  // Append the flex container to the body
  document.body.appendChild(flexContainer);
}