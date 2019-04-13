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

* Uncomment lines: basedir and app.config where the sqlalchemy dbs are setup
* Run python shell > Heroku run python > from app import db ---> db.create_all() (This will create the db and allow you to work with it locally)

## To deploy on Heroku

* git init
* git heroku create <APPNAME>
* git add .
* git commit -am "MESSAGE FOR COMMIT"
* Run python shell > Heroku run python > from app import db ---> db.create_all() (This will create the db and allow you to work with it locally)

## Resources

* https://dev.to/paultopia/the-easiest-possible-way-to-throw-a-webapp-online-flask--heroku--postgres-185o


