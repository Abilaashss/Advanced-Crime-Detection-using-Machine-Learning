function submitForm() {
  // Get the values of the input fields
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("error").value;

  // Create an object to store the user details
  const userDetails = {
    name: name,
    email: email,
    error: error,
  };

  // Store the user details in local storage
  localStorage.setItem("User details with Error info", JSON.stringify(userDetails));
}
