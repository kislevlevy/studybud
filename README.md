# Studybud

## Project Overview

### Project Description

A fully responsive forum application for programmers to discuss different subjects, create rooms, browse rooms and topics, and message a room. Users can view profiles and track associated activities. The site is accessible via API endpoints and includes an admin panel with full CRUD operations.

## Technologies Used

| Frontend                                                                                                                                                                                                                                                                                                            | Backend                                                                                                                                                                                                                                                                                                                                                                                                                             | Deployment                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) | ![Render](https://img.shields.io/badge/Render-0466C8?style=for-the-badge&logo=render&logoColor=white) |

## Features

1. **User Features**
   - Create rooms and message within rooms.
   - Browse rooms and topics.
   - View and interact with user profiles and activity.
2. **Responsiveness**
   - Optimized for both phones and desktops.
3. **API Integration**
   - Full API access for developers with the following endpoints:
     ```
     "GET /api",
     "GET /api/rooms",
     "GET /api/rooms/:id",
     "GET /api/topics",
     "GET /api/topics/:id",
     "GET /api/messages",
     "GET /api/messages/:id",
     ```
   - Built with `api_view` for an enhanced developer experience.
4. **Admin Panel**
   - Comprehensive CRUD operations for all models.
5. **Deployment**
   - Ready for deployment on Render with pre-configured `build.sh` and `render.yaml` files.

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kislevlevy/studybud
   cd studybud
   ```

2. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   - API Base URL: `http://localhost:8000/api`
   - Admin Panel: `http://localhost:8000/admin`
   - Site: `http://localhost:8000`

## API Documentation

### Endpoints

```plaintext
/api
├── GET /api                       - Get API information
├── /rooms
│   ├── GET /api/rooms             - Get all rooms
│   ├── GET /api/rooms/:id         - Get room by ID
│
├── /topics
│   ├── GET /api/topics            - Get all topics
│   ├── GET /api/topics/:id        - Get topic by ID
│
├── /messages
│   ├── GET /api/messages          - Get all messages
│   ├── GET /api/messages/:id      - Get message by ID

```
