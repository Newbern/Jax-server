
async function loadAlarms() {
    const alarmsContainer = document.getElementById("alarms");

    try {
        const response = await fetch("/alarms", {
            method: "GET",
            credentials: "include"
        });

        if (!response.ok) {
            throw new Error("Failed to retrieve alarms");
        }

        const data = await response.json();

        alarmsContainer.innerHTML = "";

        if (!data.success || data.alarms.length === 0) {
            alarmsContainer.innerHTML = `
                <div class="no-alarms">
                    <h2>No Alarms</h2>
                    <p>You don't have any alarms set.</p>
                </div>
            `;
            return;
        }

        data.alarms.forEach(alarm => {
            const alarmElement = document.createElement("div");

            alarmElement.classList.add("alarm");

            alarmElement.innerHTML = `
                <div class="alarm-info">
                    <div class="alarm-time">${alarm.time}</div>

                    <div class="alarm-details">
                        <h2>${alarm.message}</h2>
                        <p>${alarm.repeat ? "Repeating" : "One time"}</p>
                    </div>
                </div>

                <div class="alarm-actions">
                    <button class="edit-button" data-id="${alarm.id}">
                        Edit
                    </button>

                    <button class="delete-button" data-id="${alarm.id}">
                        Delete
                    </button>
                </div>
            `;

            alarmsContainer.appendChild(alarmElement);
        });

    } catch (error) {
        console.error(error);

        alarmsContainer.innerHTML = `
            <div class="error">
                <h2>Unable to load alarms</h2>
                <p>Please try again.</p>
            </div>
        `;
    }
}


document.addEventListener("DOMContentLoaded", loadAlarms);


document.getElementById("add-alarm").addEventListener("click", () => {
    console.log("Add alarm clicked");
});
