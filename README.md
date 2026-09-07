# Jax Server

Jax is a personal backend server built with **Python, FastAPI, and MySQL**.

The goal of Jax is to build a real-world backend system with authentication, session management, device authentication, and an alarm system that can be accessed through a web interface and eventually connected to physical devices.

---

## Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **MySQL**
* **JavaScript**
* **HTML**
* **CSS**
* **REST API**
* **Git**

---

## Project Structure

```text
Jax-server/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   └── alarm.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   └── alarm.py
│   │
│   ├── services/
│   │   ├── auth.py
│   │   └── alarm.py
│   │
│   ├── database/
│   │   ├── setup.sql
│   │   ├── connection.py
│   │   ├── users.py
│   │   ├── devices.py
│   │   ├── sessions.py
│   │   └── alarm.py
│   │
│   ├── security/
│   │   ├── session.py
│   │   └── hashing.py
│   │
│   ├── logs/
│   │   └── log.py
│   │
│   ├── utils/
│   │   └── auth.py
│   │
│   └── web/
│       │
│       ├── auth/
│       │   ├── login.html
│       │   ├── signup.html
│       │   ├── js/
│       │   │   ├── login.js
│       │   │   └── signup.js
│       │   └── css/
│       │       └── auth.css
│       │
│       └── alarm/
│           ├── get_alarms/
│           │   ├── index.html
│           │   ├── js/
│           │   │   └── alarm.js
│           │   └── css/
│           │       └── alarm.css
│           │
│           └── create_alarm/
│               ├── index.html
│               ├── js/
│               │   └── alarm.js
│               └── css/
│                   └── alarm.css
│
├── .env
├── .gitignore
├── ideas.md
└── README.md
```

---

## Authentication

Jax includes an authentication system for users and devices.

### Current functionality

* User registration
* User login
* Password hashing
* API key authentication
* Session creation
* Session validation
* Device authentication
* Protected API requests

Passwords are stored as **hashed passwords**, rather than plain-text passwords.

---

## Session System

Authenticated users receive a session token that can be used to access protected endpoints.

The general authentication flow is:

```text
User
 │
 ▼
Login
 │
 ▼
FastAPI
 │
 ▼
Authenticate User
 │
 ▼
Create Session
 │
 ▼
Session Token
 │
 ▼
Protected Requests
```

The session functionality is separated into the security, service, and database layers.

---

## Alarm System

The alarm system is currently one of the main features of Jax.

Users can manage alarms through the web interface.

### Alarm functionality

* Create alarms
* Retrieve alarms
* Edit alarms
* Delete alarms
* Turn alarms on/off
* Set alarm time
* Set alarm message
* Manage multiple alarms

An alarm can contain information such as:

```json
{
    "time": "05:05",
    "message": "Wakeup",
    "turn_on": true
}
```

---

## Alarm CRUD

The alarm system follows standard CRUD operations.

```text
CREATE
POST /set-alarm

READ
GET /get-alarms

UPDATE
PUT /update-alarm

DELETE
DELETE /delete-alarm
```

The web application communicates with the FastAPI backend using JavaScript.

The alarm interface also includes:

* Edit controls
* Save changes
* On/off switch
* Delete controls
* Delete confirmation popup
* Responsive alarm cards

---

## Backend Architecture

Jax separates the backend into multiple layers.

```text
API
 │
 ▼
Services
 │
 ▼
Database
```

### API

The API layer handles HTTP requests and responses.

```text
app/api/
```

### Schemas

Pydantic schemas define and validate incoming data.

```text
app/schemas/
```

### Services

Business logic is handled by the service layer.

```text
app/services/
```

### Database

Database operations are separated into their own modules.

```text
app/database/
```

### Security

Authentication-related security functionality is separated into:

```text
app/security/
```

This structure keeps HTTP handling, business logic, database operations, and security concerns separated from each other.

---

## Web Interface

Jax contains a web interface for interacting with the backend.

### Authentication

```text
app/web/auth/
```

Includes:

* Login
* Signup
* Authentication JavaScript
* Authentication styling

### Alarms

```text
app/web/alarm/
```

Includes:

* Alarm creation
* Alarm management
* Alarm editing
* Alarm deletion
* Alarm status controls

---

## Database

Jax uses **MySQL** for persistent data storage.

Database functionality is separated into individual modules for:

* Users
* Devices
* Sessions
* Alarms

The database schema can be found at:

```text
app/database/setup.sql
```

---

## Logging

Jax includes a logging system for tracking server activity and errors.

```text
app/logs/
```

The logging system is used to help debug authentication, database operations, API requests, and other backend problems.

---

## Running Jax

Clone the repository:

```bash
git clone https://github.com/Newbern/Jax-server.git
cd Jax-server
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in:

```text
.env
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## Development Goals

Jax is being developed as a practical backend engineering project.

The project is being used to build experience with:

* HTTP
* REST APIs
* FastAPI
* Pydantic
* Authentication
* Session management
* Password hashing
* API keys
* MySQL
* Database architecture
* CRUD operations
* Error handling
* Logging
* JavaScript API communication
* Git
* Linux
* Docker
* Deployment
* Backend architecture

---

## Future Development

Planned functionality includes expanding Jax into a central backend capable of communicating with multiple clients and physical devices.

The long-term concept is:

```text
                    ┌──────────────┐
                    │  JAX SERVER  │
                    │   FastAPI    │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           Website       Watch       Devices
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                      ┌──────────┐
                      │  MySQL   │
                      └──────────┘
```

Jax is intended to become a central server for managing users, devices, and services through a single backend.

---

## Project Status

**Active Development**

The current focus is building and improving the authentication and alarm systems while continuing to develop the backend architecture.

---

## Author

**Steven Newbern**

GitHub: **Newbern**

---

Jax is a personal backend development project built to learn, experiment, and develop real-world backend engineering skills.
