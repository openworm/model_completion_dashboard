FROM beevelop/nodejs-python:latest

RUN apt-get update && apt-get install -y git libxml2-dev libxslt-dev zlib1g-dev

RUN git clone https://github.com/openworm/pyopenworm.git && cd pyopenworm && git checkout dev && python setup.py install

RUN git clone https://github.com/openworm/model_completion_dashboard.git && cd model_completion_dashboard && python setup.py install && python manage.py makemigrations && python manage.py migrate && python manage.py calculate_score && npm install && npm run webpack

CMD cd model_completion_dashboard && python manage.py runserver --nothreading --noreload