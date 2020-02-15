# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](http://helloflask.com/en/book)* (《[Flask Web 开发实战](http://helloflask.com/book)》).

Demo: http://albumy.helloflask.com

![Screenshot](http://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt  # use `pip3` for Python3 on Linux & macOS
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).