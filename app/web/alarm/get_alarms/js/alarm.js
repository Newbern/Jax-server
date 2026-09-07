const alarmsContainer = document.getElementById("alarms");
const addAlarmButton = document.getElementById("add-alarm");


// FORMAT TIME FOR DISPLAY
function formatTime(time) {

    if (typeof time === "number") {

        const totalSeconds = time;

        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);

        return formatTimeParts(hours, minutes);
    }

    if (typeof time === "string") {

        const parts = time.split(":");

        if (parts.length >= 2) {

            const hours = parseInt(parts[0], 10);
            const minutes = parseInt(parts[1], 10);

            return formatTimeParts(hours, minutes);
        }
    }

    return time;
}


// FORMAT TIME FOR EDIT INPUT
function formatTimeForInput(time) {

    if (typeof time === "number") {

        const hours = Math.floor(time / 3600);
        const minutes = Math.floor((time % 3600) / 60);

        return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}`;
    }

    if (typeof time === "string") {

        const parts = time.split(":");

        if (parts.length >= 2) {

            return `${parts[0].padStart(2, "0")}:${parts[1].padStart(2, "0")}`;
        }
    }

    return time;
}


// FORMAT TIME PARTS
function formatTimeParts(hours, minutes) {

    const period = hours >= 12 ? "PM" : "AM";

    let displayHour = hours % 12;

    if (displayHour === 0) {
        displayHour = 12;
    }

    return `${displayHour}:${String(minutes).padStart(2, "0")} ${period}`;
}


// LOAD ALARMS
async function loadAlarms() {

    try {

        const response = await fetch(
            "/alarm/get-alarm-data",
            {
                method: "GET",
                credentials: "include"
            }
        );

        if (!response.ok) {
            throw new Error("Failed to get alarms");
        }

        const alarms = await response.json();

        displayAlarms(alarms);

    } catch (error) {

        console.error(error);

        alarmsContainer.innerHTML = `
            <p class="error">
                Failed to load alarms.
            </p>
        `;
    }
}


// DISPLAY ALARMS
function displayAlarms(alarms) {

    alarmsContainer.innerHTML = "";

    if (!alarms || alarms.length === 0) {

        alarmsContainer.innerHTML = `
            <p class="no-alarms">
                No alarms found.
            </p>
        `;

        return;
    }


    alarms.forEach(alarm => {

        const alarmElement = document.createElement("div");

        alarmElement.classList.add("alarm-card");

        alarmElement.innerHTML = `

            <div class="alarm-info">

                <div class="alarm-top">

                    <div class="alarm-day">
                        ${alarm.day}
                    </div>

                    <label class="switch">

                        <input
                            type="checkbox"
                            class="alarm-toggle"
                            ${alarm.turn_on ? "checked" : ""}
                        >

                        <span class="slider"></span>

                    </label>

                </div>

                <div class="alarm-time">
                    ${formatTime(alarm.time)}
                </div>

                <div class="alarm-message">
                    ${alarm.message}
                </div>

            </div>

            <div class="alarm-buttons">

                <button class="edit-alarm">
                    Edit
                </button>

                <button class="delete-alarm">
                    Delete
                </button>

            </div>

            <p class="alarm-status"></p>
        `;


        alarmElement
            .querySelector(".edit-alarm")
            .addEventListener("click", () => {
                makeAlarmEditable(alarm, alarmElement);
            });


        alarmElement
            .querySelector(".delete-alarm")
            .addEventListener("click", () => {
                deleteAlarm(alarm.id);
            });


        alarmElement
            .querySelector(".alarm-toggle")
            .addEventListener("change", () => {
                toggleAlarm(alarm, alarmElement);
            });


        alarmsContainer.appendChild(alarmElement);
    });
}


// EDIT ALARM
function makeAlarmEditable(alarm, alarmElement) {

    const alarmInfo = alarmElement.querySelector(".alarm-info");

    alarmInfo.innerHTML = `

        <div class="edit-field">

            <label>
                Time
            </label>

            <input
                type="time"
                class="edit-time"
                value="${formatTimeForInput(alarm.time)}"
            >

        </div>


        <div class="edit-field">

            <label>
                Day
            </label>

            <select class="edit-day">

                <option value="Everyday">Everyday</option>
                <option value="Sunday">Sunday</option>
                <option value="Monday">Monday</option>
                <option value="Tuesday">Tuesday</option>
                <option value="Wednesday">Wednesday</option>
                <option value="Thursday">Thursday</option>
                <option value="Friday">Friday</option>
                <option value="Saturday">Saturday</option>

            </select>

        </div>


        <div class="edit-field">

            <label>
                Message
            </label>

            <input
                type="text"
                class="edit-message"
                value="${alarm.message}"
            >

        </div>
    `;


    alarmInfo.querySelector(".edit-day").value = alarm.day;


    const buttons = alarmElement.querySelector(".alarm-buttons");

    buttons.innerHTML = `

        <button class="save-alarm">
            Save
        </button>

        <button class="cancel-alarm">
            Cancel
        </button>

        <button class="delete-alarm">
            Delete
        </button>

    `;


    buttons
        .querySelector(".save-alarm")
        .addEventListener("click", () => {
            updateAlarm(alarm, alarmElement);
        });


    buttons
        .querySelector(".cancel-alarm")
        .addEventListener("click", () => {
            displaySingleAlarm(alarm, alarmElement);
        });


    buttons
        .querySelector(".delete-alarm")
        .addEventListener("click", () => {
            deleteAlarm(alarm.id);
        });
}


// DISPLAY SINGLE ALARM
function displaySingleAlarm(alarm, alarmElement) {

    alarmElement.innerHTML = `

        <div class="alarm-info">

            <div class="alarm-top">

                <div class="alarm-day">
                    ${alarm.day}
                </div>

                <label class="switch">

                    <input
                        type="checkbox"
                        class="alarm-toggle"
                        ${alarm.turn_on ? "checked" : ""}
                    >

                    <span class="slider"></span>

                </label>

            </div>

            <div class="alarm-time">
                ${formatTime(alarm.time)}
            </div>

            <div class="alarm-message">
                ${alarm.message}
            </div>

        </div>

        <div class="alarm-buttons">

            <button class="edit-alarm">
                Edit
            </button>

            <button class="delete-alarm">
                Delete
            </button>

        </div>

        <p class="alarm-status"></p>
    `;


    alarmElement
        .querySelector(".edit-alarm")
        .addEventListener("click", () => {
            makeAlarmEditable(alarm, alarmElement);
        });


    alarmElement
        .querySelector(".delete-alarm")
        .addEventListener("click", () => {
            deleteAlarm(alarm.id);
        });


    alarmElement
        .querySelector(".alarm-toggle")
        .addEventListener("change", () => {
            toggleAlarm(alarm, alarmElement);
        });
}


// TURN ALARM ON / OFF
async function toggleAlarm(alarm, alarmElement) {

    const toggle = alarmElement.querySelector(".alarm-toggle");

    const turnOn = toggle.checked;


    const updatedAlarm = {

        id: alarm.id,

        time: formatTimeForInput(alarm.time),

        day: alarm.day,

        message: alarm.message,

        is_repeat: alarm.is_repeat ?? false,

        turn_on: turnOn
    };


    try {

        const response = await fetch(
            "/alarm/updated-alarm-data",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                credentials: "include",

                body: JSON.stringify(updatedAlarm)
            }
        );


        if (!response.ok) {
            throw new Error("Failed to update alarm");
        }


        alarm.turn_on = turnOn;


    } catch (error) {

        console.error(
            "Error changing alarm state:",
            error
        );

        toggle.checked = !turnOn;

        alert("Failed to change alarm.");
    }
}


// UPDATE ALARM
async function updateAlarm(alarm, alarmElement) {

    const time = alarmElement
        .querySelector(".edit-time")
        .value;

    const day = alarmElement
        .querySelector(".edit-day")
        .value;

    const message = alarmElement
        .querySelector(".edit-message")
        .value;


    const updatedAlarm = {

        id: alarm.id,

        time: time,

        day: day,

        message: message,

        is_repeat: alarm.is_repeat ?? false,

        turn_on: alarm.turn_on ?? true
    };


    try {

        const response = await fetch(
            "/alarm/updated-alarm-data",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                credentials: "include",

                body: JSON.stringify(updatedAlarm)
            }
        );


        if (!response.ok) {
            throw new Error("Failed to update alarm");
        }


        alarm.time = time;

        alarm.day = day;

        alarm.message = message;


        displaySingleAlarm(
            alarm,
            alarmElement
        );


        const status =
            alarmElement.querySelector(".alarm-status");


        status.textContent =
            "✓ Alarm successfully updated";

        status.classList.add("success");


        setTimeout(() => {

            status.textContent = "";

            status.classList.remove("success");

        }, 3000);


    } catch (error) {

        console.error(
            "Error updating alarm:",
            error
        );

        alert("Failed to update alarm.");
    }
}


// DELETE ALARM
async function deleteAlarm(alarmId) {

    const existingPopup =
        document.querySelector(".delete-popup");

    if (existingPopup) {
        existingPopup.remove();
    }


    const popup =
        document.createElement("div");

    popup.classList.add("delete-popup");


    popup.innerHTML = `

        <div class="delete-popup-box">

            <h2>
                Delete Alarm?
            </h2>

            <p>
                Are you sure you want to delete this alarm?
            </p>

            <div class="delete-popup-buttons">

                <button class="cancel-delete">
                    Cancel
                </button>

                <button class="confirm-delete">
                    Delete
                </button>

            </div>

        </div>

    `;


    document.body.appendChild(popup);


    popup
        .querySelector(".cancel-delete")
        .addEventListener("click", () => {

            popup.remove();

        });


    popup
        .querySelector(".confirm-delete")
        .addEventListener(
            "click",
            async () => {

                try {

                    const response =
                        await fetch(
                            "/alarm/delete-alarm-data",
                            {
                                method: "POST",

                                headers: {
                                    "Content-Type":
                                        "application/json"
                                },

                                credentials: "include",

                                body: JSON.stringify({
                                    id: alarmId
                                })
                            }
                        );


                    if (!response.ok) {
                        throw new Error(
                            "Failed to delete alarm"
                        );
                    }


                    popup.remove();

                    await loadAlarms();


                } catch (error) {

                    console.error(
                        "Error deleting alarm:",
                        error
                    );


                    popup
                        .querySelector(
                            ".delete-popup-box"
                        )
                        .innerHTML = `

                            <h2>
                                Delete Failed
                            </h2>

                            <p>
                                Failed to delete the alarm.
                            </p>

                            <div
                                class="delete-popup-buttons"
                            >

                                <button
                                    class="cancel-delete"
                                >
                                    Close
                                </button>

                            </div>
                        `;


                    popup
                        .querySelector(
                            ".cancel-delete"
                        )
                        .addEventListener(
                            "click",
                            () => {
                                popup.remove();
                            }
                        );
                }
            }
        );
}


// ADD ALARM
addAlarmButton.addEventListener(
    "click",
    () => {

        window.location.href =
            "/alarm-web/create_alarm/";
    }
);


// START
loadAlarms();