# model_completion_dashboard
Model Completion Dashboard

http://pyopenworm-pyopenworm.rhcloud.com/

http://docs.openworm.org/en/latest/Projects/muscle-neuron-integration/#model-completion-dashboard

To install
----------

`python setup.py install`
`npm install`
`npm run webpack`

To run
------
`python manage.py runserver`

Docker commands
---------------

Run with command line (need to initiate run command from bash when it starts up:

```
docker run -it --rm --name my-running-script -p 8000:8000 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:2 bash
```

Run server:

```
docker run -it --rm --name my-running-script -p 8000:8000 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:2 bash -c "pip install django==1.8 && python setup.py install && ls && python manage.py runserver"
```
