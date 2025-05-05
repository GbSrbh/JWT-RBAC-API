JWT-RBAC-API

A RESTful API that implements user authentication with JWT (JSON Web Token) and 
Role-Based Access Control (RBAC). The API manages users with different roles and 
restrict access to certain endpoints based on the user’s role. 
Built on FastAPI + PostgreSQL with SQLModel layer.

## Features

- User Registration
- Role-based Authorization (Admin/Standard User)
- JWT Authentication for secure routes



Watch the walkthrough: https://drive.google.com/file/d/1_Gfp9xdw2Wt-ggibPJG5YnX7qJPPGr82/view?usp=sharing

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/GbSrbh/JWT-RBAC-API
cd JWT-RBAC-API
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate the dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure the Environment

Create a `.env` file in the root directory to configure environment variables. Here's an example env file:

```bash
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
TOKEN_EXPIRY_TIME_IN_MINUTES=15  # Expiry time for the JWT tokens (in minutes)
DATABASE_URL=postgresql://username:password@localhost:port/dbname
```
Update the Database URL with your db server's username, password and the name of your database. 

### 5. Setup PostgreSQL

PostgreSQL should be installed and running.

Create a new database in PostgreSQL:

```bash
psql -U postgres
CREATE DATABASE your_database_name;
```

### 7. Run the Application

Start the FastAPI application with the below command:

```bash
python server.py 
```
Make sure you're in the root directory (where server.py exists)

The server will start on `http://127.0.0.1:5000`. You can change the port by updating PORT field in env file.

---

## Extras

I'm using Bcrypt for password hashing with 12 salt rounds.

The JWT library used for token encoding is PYJWT.

This is symmetric token generation (single key for encoding and decoding) with HS256 algorithm (you can change the algorithm in env file).

