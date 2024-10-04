# Blog

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Virtualenv (optional but recommended)
- Postgres 


### Installation
1. ***Configure Database in .env***:
```.env
    DATABASE_NAME=
    DATABASE_PASS=
    DATABASE_USER=
    DATABASE_HOST=
    DATABASE_PORT=
```

2. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/mydjangoproject.git
   ```
3. **Create virtual env and activate**:
    ```sh
    python3 -m venv env_name
    ```
    - On Linux/macOS:
        ```sh
        source myenv/bin/activate
        ```
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
4. **install rquirement packages**:
    - On virtua env:
    ```sh
    pip install -r requirements.txt
    ```
    - without virtual env:
    ```sh
    pip3 install -r requirements.txt
    ```
5. **migrate database**:
    ```sh
    python manage.py migrate
    ```

6. **Create User**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Start Project**:
    ```sh
    python manage.py runserver
    ```

