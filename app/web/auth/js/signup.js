
document.getElementById("signupForm").addEventListener("submit", async (event) => {

    event.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const message = document.getElementById("message");

    try {

        const response = await fetch("/auth/signup", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            credentials: "include",

            body: JSON.stringify({
                username: username,
                email: email,
                password: password,
                device_type: "web"
            })
        });

        const data = await response.json();

        if (!response.ok) {

            message.textContent =
                data.detail || "Signup failed.";

            return;
        }

        message.textContent =
            "Account created successfully!";

        // Send them to login
        setTimeout(() => {
            window.location.href = "/web/auth/login.html";
        }, 1000);

    } catch (error) {

        console.error(error);

        message.textContent =
            "Unable to connect to Jax server.";
    }
});
