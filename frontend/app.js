
const inputText = document.getElementById("inputText");
const translateButton = document.getElementById("translateButton");
const inputError = document.getElementById("inputError");

translateButton.addEventListener("click", () => {
    const englishText = inputText.value.trim();

    if (!englishText) {
        inputError.textContent = "Please enter English text.";
        return;
    }

    inputError.textContent = "";
});
