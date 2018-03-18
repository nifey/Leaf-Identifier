#!bin/sh
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00241/100%20leaves%20plant%20species.zip
unzip 100\ leaves\ plant\ species.zip
pip install -r requirements.txt
mv 100\ leaves\ plant\ species/data/ .
python trainleaf.py -d data/ -m hundred
