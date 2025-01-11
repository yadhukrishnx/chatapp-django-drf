# AI Chat System - Django REST APIs  
A RESTful API system built with Django for an AI-powered chatbot. This project provides secure user management, token-based authentication, and a tokenized chat interaction mechanism

⬇️ API Documentation



## Getting Started

### Prerequisites  
- Python 3.11.2
- Django 5.1.4
- Django REST Framework  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yadhukrishnx/chatapp-django-drf
   cd chatapp-django-drf
   ```  

2. Install dependencies:  
   ```bash
   python -m venv virtualenv (Create Virtual Environment - Optional)
   pip install -r requirements.txt
   ```  

3. Run migrations:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```  

4. Start the server:  
   ```bash
   python manage.py runserver
   ```  

5. Access the API at `http://127.0.0.1:8000/`.  

---

# AI Chat System - API Documentation


---

## API Endpoints

### 1. User Registration API
- **Endpoint:** `api/register/`
- **Method:** `POST`
- **Description:** Register a new user. Assigns 4000 tokens to the user by default.
- **Request Body:**
  ```json
  {
      "username": "example_user",
      "password": "example_password"
  }

### 2. Login API
- **Endpoint:** `api/login/`
- **Method:** `POST`
- **Description:** Log in an existing user and receive an authentication token.
- **Request Body:**
  ```json
  {
      "username": "example_user",
      "password": "example_password"
  }

- **Response :**
   ```json
   {
    "message": "Login Successful",
    "token": "example_auth_token",
    "chat_url": "http://<your-server-domain>/api/chat/"
   }

### 3. Chat API
- **Endpoint:** `api/chat/`
- **Method:** `POST`
- **Description:** Send a message to the chatbot and receive a response. Deducts 100 tokens per question.
- **Request Body:**
  ```json
  {
      "message": "What is AI?"
  }
- **Header:**
   ```json
   {
    "Authorization": "Token example_auth_token"
   }

- **Response:**
   ```json
   {
    "message": "Question asked successfully.",
    "response": "This is a dummy AI response to your question.",
    "tokens_left": 3900
   }


### 4. Token Balance API
- **Endpoint:** `api/token-balance/`
- **Method:** `GET`
- **Description:**  Check the current token balance for the API Token Given.
- **Request Body:**
  ```json
  {
      "token" : "Your API Token"
  }
- **Header:**
   ```json
   {
    "Authorization": "Token example_auth_token"
   }

- **Response:**
   ```json
   {
    "tokens": 3900
   }


# Challenges Encountered
- secure token-based authentication and handling login requests(Conflict between session auth and token auth).
- Increased Time for Response through js


# Suggestions for Improvement
- Improve user management
- Functionality to recharge tokens
- Scalability