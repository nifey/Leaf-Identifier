# Leaf identifier
This is a leaf identifier that performs multiclass classification. It is written in python and uses the [UCI One-hundered plant species data set](https://archive.ics.uci.edu/ml/datasets/One-hundred+plant+species+leaves+data+set). 
The code was written by following [this tutorial blogpost](https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/).

Frameworks used are 
* Keras for machine learning
* Flask for creating a simple web interface

### Instructions
To automatically download and train the model simply run the shell script
```
sh train.sh
```
After running the script a model named hundred will be created. Now run
```
python app.py
```
and open http://127.0.0.1:5000/upload in your browser.
