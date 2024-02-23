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
