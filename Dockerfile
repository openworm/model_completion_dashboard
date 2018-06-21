FROM debian:unstable-slim

RUN apt-get update && \
    apt-get install -y git \
                       libxml2-dev \
                       libxslt-dev \
                       zlib1g-dev \
                       python-pip \
                       python3.6

RUN pip install --upgrade pip

RUN git clone https://github.com/openworm/pyopenworm.git && \
    cd pyopenworm && \
    git checkout dev && \
    python setup.py install && \
    pow clone https://github.com/openworm/OpenWormData.git

RUN git clone https://github.com/openworm/model_completion_dashboard.git && \
    cd model_completion_dashboard && \
    python setup.py install && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py calculate_score && \
    npm install && \
    npm run webpack

CMD cd model_completion_dashboard && \
    python manage.py runserver --nothreading --noreload 0.0.0.0:8000
