
document.getElementById("loginForm").addEventListener("submit", async (event) => {

    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    try {

        const response = await fetch("/auth/login", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            credentials: "include",

            body: JSON.stringify({
                email: email,
                password: password,
                device_type: "web"
            })
        });

        const data = await response.json();

        if (!response.ok) {
            message.textContent =
                data.detail || "Login failed.";

            return;
        }

        message.textContent = "Login successful!";

        // Change this later to your actual home/dashboard
        window.location.href = "/";

    } catch (error) {

        console.error(error);

        message.textContent =
            "Unable to connect to Jax server.";
    }
});
