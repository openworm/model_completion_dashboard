FROM debian:unstable-slim

RUN apt-get update && \
    apt-get install -y git \
                       libxml2-dev \
                       libxslt-dev \
                       zlib1g-dev \
                       python3.6 \
                       python3-pip # Includes setuptools, needed for install of PyOpenWorm and others

ENV PYTHON=python3.6

RUN git clone https://github.com/openworm/pyopenworm.git && \
    cd pyopenworm && \
    git checkout dev && \
    $PYTHON setup.py install && \
    pow clone https://github.com/openworm/OpenWormData.git

RUN git clone https://github.com/mwatts15/model_completion_dashboard.git && \
    cd model_completion_dashboard && \
    git checkout mwatts/pow-reintegration && \
    $PYTHON setup.py install && \
    $PYTHON manage.py makemigrations && \
    $PYTHON manage.py migrate && \
    $PYTHON manage.py calculate_score && \
    npm install && \
    npm run webpack

CMD cd model_completion_dashboard && \
    $PYTHON manage.py runserver --nothreading --noreload 0.0.0.0:8000
