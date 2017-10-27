# Capsoul Backend
A python based backend that uses Django to store memories.

## Running the server

To run the server follow the steps below.

Before you start you should have python 2.7 installed. You can download it [here](https://www.python.org/downloads/).

#### 1. Install Django
```
pip install django
```
#### 2. Get the project running
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### 3. Query endpoints
You can check that the server is running by navigating to [localhost:8000](http://localhost:8000). This will show the available routes.

For example [localhost:8000/user/<uname>](http://localhost:8000/users/rabery) would load the following when `uname` is “rabery”.
```
{
    "user_name": "rabery",
    "first": "Ryan",
    "last": "Rabello",
    "phone": "212-479-7990",
    "location": "Walla Walla, WA",
    "photo": "ryan.jpg",
    "email": "ryan.rabello@gmail.com",
    "birthdate": "1992-09-02"
}
```

## Other Notes
#### Running on a different port
You can run the server on a different port by running the following command.
```
python manage.py runserver <port>
```
Where `port` would be the number of the port you want to use.
