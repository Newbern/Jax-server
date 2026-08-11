
document.getElementById("signupForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

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

        document.getElementById("message").innerText =
            `Status: ${response.status}\n${JSON.stringify(data)}`;

        if (response.ok) {
            // window.location.href = "/web/login.html";
        }

    } catch (error) {
        document.getElementById("message").innerText =
            `Error: ${error}`;
    }
});

