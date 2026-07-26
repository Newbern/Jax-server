# JAX Server

JAX is a personal self-hosted media and device server built with FastAPI.

The goal of JAX is to become a central server for:

- Movie streaming
- Device authentication
- Smart home control
- Watch connectivity
- Personal APIs
- Media tracking

---

# Current Features

## Authentication

JAX currently supports:

- User accounts
- Device registration
- API key authentication
- Session creation
- Cookie based web authentication
- Session expiration handling

Supported device types:

- Web
- Watch
- Authentication devices

---

## Movie Collection

JAX can scan a local movie library and store movie information.

Current scanner:

```
D:\Movie Collection
```

Expected structure:

```
Movie Collection
│
├── Action
│   ├── Movie1.mp4
│   └── Movie2.mp4
│
├── Comedy
│   ├── Movie3.mp4
│
└── Horror
    └── Movie4.mp4
```

The scanner currently saves:

- Movie title
- Genre
- Filename
- File path

---

## Movie Metadata

Connected to:

TMDB API

Currently planned:

- Movie posters
- Backdrops
- Runtime
- Ratings
- Descriptions
- Release year

---

# Project Structure

```
Jax-server

app
│
├── api
│   ├── auth.py
│   └── media.py
│
├── database
│   ├── database.py
│   ├── models.py
│   └── setup.sql
│
├── logs
│   └── JAX.log
│
├── schemas
│   └── auth.py
│
├── security
│   └── hashing.py
│
└── services
    ├── auth.py
    ├── movie_scanner.py
    ├── movie_data_collector.py
    └── session.py
```

---

# Running JAX

Start server:

```
python -m uvicorn app.main:app --reload
```

Server:

```
http://localhost:8000
```

---

# Database

Database:

```
jax_server
```

Current tables:

- users
- devices
- sessions
- movies
- media
- smart_plug

---

# Current Development Status

## Completed

[x] Server foundation

[x] Database connection

[x] User registration

[x] Device creation

[x] Session management

[x] Cookie authentication

[x] Movie folder scanner

[x] Movie database storage


## In Progress

[ ] Movie poster downloading

[ ] Movie metadata population

[ ] Movie streaming endpoint

[ ] Continue watching system

[ ] Web frontend

[ ] Device API

[ ] Smart home controls


---

# Future Goal

JAX will become a personal home server that connects:

- Computer
- Raspberry Pi
- ESP32 watch
- Smart devices
- Personal applications

Everything communicates through the JAX API.