#!/bin/bash

~/Python-Projects/DCI-Data/venv/bin/python /home/aggieed97/Python-Projects/DCI-Data/main.py &&

~/Python-Projects/DCI-Data/venv/bin/python /home/aggieed97/Python-Projects/DCI-Data/small-recap-scrape.py &&

~/Python-Projects/DCI-Data/venv/bin/python /home/aggieed97/Python-Projects/DCI-Data/large-recap-scrape.py &&

cd ~/R-Projects/DCI-R-Projects/ &&

/usr/lib/R/bin/Rscript -e 'renv::activate()' &&

/usr/lib/R/bin/Rscript ~/R-Projects/DCI-R-Projects/DCI-Max-Score-Table.R &&

/usr/lib/R/bin/Rscript ~/R-Projects/DCI-R-Projects/DCI-Max-Captions-Loop.R

#~/Python-Projects/DCI-Data/venv/bin/python /home/aggieed97/Python-Projects/DCI-Data/send_tweet.py