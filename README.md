# CF Sample Flask SQLAlchemy application

A sample [Flask](http://flask.pocoo.org/) and SQLAlchemy application to deploy to Cloud Foundry which works out of the box.

## Run locally

1. Install [Python](http://docs.python-guide.org/en/latest/starting/installation/)
1. Install Setuptools and pip (see guide above)
1. Install Virtualenv (acconplish this by running `pip install virtualenv`)
1. Run `virtualenv venv`
1. Run `source venv/bin/activate` on Mac OS X/Linux or`venv\Scripts\activate.bat` on windows
1. Run `pip install -r requirements.txt`
1. Run `source env.sh`
1. Run `python app.py`
1. Visit [http://localhost:5000](http://localhost:5000)

## Deploy on Cloud Foundry

1. Install the [cf CLI](https://github.com/cloudfoundry/cli#downloads)
1. Create database service instance (in this example using [VMWare Tanzu MySQL Broker](https://docs.pivotal.io/p-mysql/2-10/)), run `cf create-service p.mysql db-small database` and wait for the service instance to be deployed (`cf services` or `cf service database`)
1. Run `cf push` 
1. Visit the given URL

## References

- [cf-sample-app-python](https://github.com/swisscom/cf-sample-app-python)
- [Flask SQLAlchemy Tutorial](https://www.kite.com/blog/python/flask-sqlalchemy-tutorial/), [GitHub](https://github.com/kiteco/kite-python-blog-post-code/tree/master/flask-tutorial/flask-and-sqlalchemy)