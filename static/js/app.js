function copyToClipboard() {
  var input = document.getElementById("generated-password").textContent;
  input = input.trim();
  navigator.clipboard.writeText(input);
}

