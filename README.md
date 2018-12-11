##Flask Sample Application with SQLAlchemy

1. git clone
2. create virtual environment for project
	python3 -m venv venv
	. venv/bin/activate (activate virtual env)
3. install dependencies
	pip install flask, flask-sqlalchemy, mysql-connector-python
4. export Flask Env Variables
	export FLASK_APP=flaskr
	export FLASK_ENV=development
5. start application
	flask run

Notes:
- Flask-SQLAlchemy is an extension for SQLAlchemy, just provided better integration, you can also use SQLAlchemy directly
- Flask-RESTful doesn't have siginificant help for building restful API, so I just directly build it myself
- It’s preferable to create your extensions and app factories so that the extension object does not initially get bound to the application. see http://flask.pocoo.org/docs/1.0/patterns/appfactories/
