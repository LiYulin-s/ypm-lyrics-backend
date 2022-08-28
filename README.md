# Introduction
This is the backend of the Plasmoid `org.kde.plasma.ypm-lyrics`.
Please run it before use the addon.
# Usage
```sh
$ git clone https://github.com/LiYulin-s/ypm-lyrics-backend.git
$ cd ypm-lyrics-backend
$ pip install -r requirements.txt
$ python -m flask run &
```
And if you do not want to use the built-in server of the Flask, you can change it.
```sh
$ pip install gunicorn
$ python -m gunicorn -b localhost:5000 app:app -D
```