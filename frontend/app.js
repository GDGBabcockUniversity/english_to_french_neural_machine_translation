
const BACKEND_BASE_URL = "http://localhost:8000";

const inputText = document.getElementById("inputText");
const translateButton = document.getElementById("translateButton");
const inputError = document.getElementById("inputError");
const outputText = document.getElementById("outputText");

translateButton.addEventListener("click", async () => {
    const englishText = inputText.value.trim();

    // Keep the existing empty-input validation.
    if (!englishText) {
        inputError.textContent = "Please enter English text.";
        return;
    }

    inputError.textContent = "";

    try {
        const response = await fetch(`${BACKEND_BASE_URL}/translate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: englishText
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Translation failed.");
        }

        outputText.value = data.translation;
    } catch (error) {
        console.error("Translation error:", error);
        inputError.textContent =
            "Unable to translate right now. Please check the backend and try again.";
    }
});
