# Back end

## To make a POST and GET request

* Follow the example from request_example.py
* Make sure the data is properly formatted

## Format

You can use Postman to send this post request and write into the db

	data = {
		'bpm': 124.2,
		'bodyTemp': 45.23,
	}

## To run locally

1- Uncomment lines: basedir and app.config where the sqlalchemy dbs are setup
2- Run python shell > Heroku run python > from app import db ---> db.create_all() (This will create the db and allow you to work with it locally)

## To deploy on Heroku

1- git init
2- git heroku create <APPNAME>
3- git add .
4- git commit -am "MESSAGE FOR COMMIT"
5- Run python shell > Heroku run python > from app import db ---> db.create_all() (This will create the db and allow you to work with it locally)


