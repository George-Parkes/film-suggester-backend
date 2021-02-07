# film-suggester-backend

To run this project download the dependencies (requires homebrew)
```
# Download python3
brew install python

# Confirm python3 is downloaded
python3 --version

# Download Django
pip3 install Django==3.1.6

# Confirm Django is downloaded
python3 -m django --version

```
Note you can also [download pyenv](https://opensource.com/article/19/5/python-3-default-mac) to control the python version you're using locally (so you don't have to use `python3`, you can just set the local version to 3 and use `python`).

The first time you run the project you'll need to run migrations.
```
python3 manage.py migrate

```

To run the project:
```
python3 manage.py runserver
```
