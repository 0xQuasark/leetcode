document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("myForm");
  // const outputDiv = document.getElementById("output");

  form.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission behavior

    const nameInput = document.getElementById("name");
    const submittedText = nameInput.value;

    alert("Hello, " + submittedText);

    // outputDiv.textContent = "Submitted Text: " + submittedText;
  });
});
