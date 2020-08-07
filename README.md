# Mele's Attendance Project

## Getting Started

1. Clone this repository with the `git clone` command
1. Make sure you have `Python 3.8` and the `pip` package installed.
1. Create a **virtual environment** (if you don't rememember how to do it, check this [page][python-venv]!). I created one called `.venv`:

```bash
$ python -m venv .venv  
```

1. Activate the virtual environment. For example, if your virtual environment is named `.venv`, type :

```bash
$ source .venv/bin/activate  // on MacOs and Linux
$ .venv\Scripts\activate.bat  // on Widows
```
You can `deactivate` it before leaving your workspace by typing `deactivate` in your terminal :)

1. Install dependencies with `pip`. But first, let's make sure we have the latest version of `pip` :

```bash
$ python -m pip install --upgrade pip
```

And now install every package with this command :

```bash
$ pip install -r requirements.txt
```

## Run the Server

Start by making migrations :

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

And then run the backend server with:

```bash
$ python manage.py runserver
```

[python-venv]: http://pacific-coding.commoncode.io/python-intro/create-a-venv/
