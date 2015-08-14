Nina [![Build Status](https://snap-ci.com/NinaDaPraia/Nina/branch/master/build_image)](https://snap-ci.com/NinaDaPraia/Nina/branch/master)
===

[![Join the chat at https://gitter.im/NinaDaPraia/Nina](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/NinaDaPraia/Nina?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Description

A project to help you learn more about influential figures involved with social justice initiatives.

### Project requirements

#### Python version
  
  The project was tested using version 3.4

#### System dependencies
  
  The application needs some Python packages: Django, Django REST and psycopg2.
  You can install them by running the command ```pip install -r requirements.txt```

  You'll also need to install PostgreSQL 9.4.

#### Configuration
  
  You can change some configuration options using environment variables.

##### Database connection settings
    
  The following variables are available if you need to adjust the database connection settings according to your needs:

    | Variable          | Default value |
    | --------------------------------- |
    | DATABASE_NAME     | nina          |
    | DATABASE_USERNAME | nina          |
    | DATABASE_PASSWORD | nina          |
    | DATABASE_HOST     | localhost     |

#### Database creation
  
  You should manually create the database for your application on PostgreSQL.

#### Database initialization

  Once you created the database and set up the connection settings for your database, you should run the command:
  ```python manage.py migrate```

  You can also run the command ```python manage.py createsuperuser``` to create a user to access the admin area of the application.

#### How to run the test suite
  You can run the tests using the command:
  ```python manage.py test```
  
  or using paver to run the tasks:
  ```paver test_all```

  To run the contract tests using a local server, you use the command:
  ```bundle exec rake spec```

  You can also set the host of the API by setting the environment variable API_HOST with the value you want. For example:
  ```API_HOST=http://example.com bundle exec rake spec```

##### Deployment instructions
  Once you publish your commits, the deploy will be made by SnapCI once all the tests are green. You can interact with the API at http://nina.herokuapp.com

##### How to contribute: 
We are using Waffle to track the issues: 
[![Stories in Ready](https://badge.waffle.io/NinaDaPraia/nina.svg?label=ready&title=Ready)](http://waffle.io/NinaDaPraia/nina)
[![Throughput Graph](https://graphs.waffle.io/NinaDaPraia/nina/throughput.svg)](https://waffle.io/NinaDaPraia/nina/metrics)
