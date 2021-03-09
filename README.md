# NLP_SERVICE

Test flask project with SQLalchemy migrations and neural networks

## Run dev server as is:
```sh
# Clone repo
$ git clone git@github.com:powersemmi/nlp_service.git && cd nlp_service
# Install requarements
$ pip install -r req.txt
# Edit configure file
$ vim .env
# Up postgres and adminer docker containers
$ cd docker/postgres && docker-compose up -d && cd ../../
# Run tests
$ cd tests && pytest && ../
# Run migration init, migrate, upgrade
$ ./nlp_service db init && ./nlp_service db migrate && ./nlp_service upgrade 
# Run app
$ flask run
 * Running on http://127.0.0.1:5000/
```

## Requirements
* Python 3.8
* PyTest
* Alembic
* SqlAlchemy
* Flask
* Flask-Migration
* Flask-Script
* Flask-SqlAlchemy
* docker
* docker-compose
* Pandas
* PyTorch
* Tensorflow
* Keras
* python-dotenv

*For Windows recommended wsl2* 

