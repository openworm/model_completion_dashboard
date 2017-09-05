# Model Completion Dashboard

#### Overview

Efforts have been made to model C.elegans, and data has been collected from research papers and various sources to do so. Now it has become important to record and track progress.
Model Completion Dashboard does exactly this, using PyOpenWorm as a data resource, this application represents the current state of affairs for C.elegans modelling. The user can now know at a glance how far we have come in modelling the worm and how far we still have to go.

http://docs.openworm.org/en/latest/Projects/muscle-neuron-integration/#model-completion-dashboard

#### Flow

![home_page](https://user-images.githubusercontent.com/15982349/30006225-441afc3c-9111-11e7-813c-2d9c6df545c0.png)

This is the home page, where the cells are represented as part of a matrix. The color associated with each of the cell, denotes the level of completion of that particular cell.
Clicking on any one of those cells would take the user to the details pane of that cell.

![details1](https://user-images.githubusercontent.com/15982349/30006223-441141c4-9111-11e7-9b60-a1eef3553c60.png)

The details pane would list down essential details about the cell as well as the ion channels associated with that cell.
Here we also have the ion channel matrix, in which each cell represents an associated ion channel, clicking on anyone of the cell, would take the user to the details pane of that ion channel


![details2](https://user-images.githubusercontent.com/15982349/30006413-61eb268e-9115-11e7-95cc-3076ee9eb5a7.png)

The Dashboard also supports search functionality to search for a particular cell or ion channel.

![search](https://user-images.githubusercontent.com/15982349/30006226-443a6888-9111-11e7-9dc5-84ca7a6af4b5.png)


To install
----------

(recommended) use node version 6.11.0

`python setup.py install`
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py calculate_score`
`npm install`
`npm run webpack`

To run
------
`python manage.py runserver --nothreading --noreload`

Run with Docker 
---------------

Install Docker

`run.sh`
