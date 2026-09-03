
const alarmForm = document.getElementById("alarmForm");
const status = document.getElementById("status");

alarmForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const alarm = {
        time: document.getElementById("time").value,
        day: document.getElementById("day").value,
        message: document.getElementById("message").value,
        is_repeat: document.getElementById("is_repeat").checked
    };

    try {

        const response = await fetch("/alarm/create-alarm", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            credentials: "include",

            body: JSON.stringify(alarm)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Failed to create alarm");
        }

        status.textContent = "Alarm created successfully!";

        alarmForm.reset();

    } catch (error) {

        console.error(error);

        status.textContent = error.message;
    }
});
