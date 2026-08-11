
document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

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

        document.getElementById("message").innerText =
            `Status: ${response.status}\n${JSON.stringify(data)}`;

        if (response.ok) {
            // window.location.href = "/";
        }

    } catch (error) {
        document.getElementById("message").innerText =
            `Error: ${error}`;
    }
});
