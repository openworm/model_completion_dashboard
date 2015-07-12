#!/bin/bash

cd ~/app-root/runtime/repo

rm -rf model_completion_dashboard

git clone https://github.com/joebowen/model_completion_dashboard.git

rm model_completion_dashboard/db.sqlite3

cp -r model_completion_dashboard/* ~/app-root/runtime/repo
cp -r model_completion_dashboard/.openshift/* ~/app-root/runtime/repo/.openshift

