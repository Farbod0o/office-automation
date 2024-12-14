// main.js

document.getElementById("dep-registration-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: "POST",
            body: formData,
        });

        const result = await response.json();

        if (result.status) {
            showToast("success", "Department submitted successfully!");
        } else {
            showToast("error", "Failed to submit department: " + result.message);
        }
    } catch (error) {
        showToast("error", "An error occurred while submitting the form.");
    }
});
