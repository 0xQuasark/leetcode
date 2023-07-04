document.addEventListener("DOMContentLoaded", function() {
  // const button = document.querySelector("button[type='submit']") // this is less efficient according to gpt
  const button = document.getElementById("myButton")
  const bgColor = document.getElementById("myParagraph")
  let isRedBackground = false


  button.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default form submission behavior

    let currentColor = bgColor.style.backgroundColor

    if (currentColor === "red") {
      bgColor.style.backgroundColor = "black";
    } else {
      bgColor.style.backgroundColor = "red";
    }

    // LESS EFFICIENT
    // if (isRedBackground) {
    //   isRedBackground = false;
    //   bgColor.style.backgroundColor = "red";
    // } else {
    //   isRedBackground = true;
    //   bgColor.style.backgroundColor = "black";
    // }

  });
});
