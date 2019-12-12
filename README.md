# coffeechart
Share your coffee inspiration and recipes!

-------------------------------------------

### creates venv in the directory
python3 -m venv venv

### activate venv env
. venv/bin/activate

### turn off venv env
deactivate

-------------------------------------------

### install Flask inside venv
pip install Flask

-------------------------------------------

### run flask app

export FLASK_APP=hello.py
python3 -m flask run

-------------------------------------------

### dev mode - auto reloads everytime code change takes place
export FLASK_ENV=development
python3 -m flask run

-------------------------------------------

### set debugger - please turn it off in prod
export FLASK_DEBUG=1

-------------------------------------------

### Reference
http://flask.palletsprojects.com/en/1.1.x/
http://flask.palletsprojects.com/en/1.1.x/quickstart/
http://flask.palletsprojects.com/en/1.1.x/deploying/#deployment
http://flask.palletsprojects.com/en/1.1.x/cli/#cli