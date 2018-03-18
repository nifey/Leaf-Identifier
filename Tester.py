# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import os
import cv2
class Tester:
    @staticmethod
    def test(imagepath,model,dataset):
        # load the image
        image = cv2.imread(imagepath)
        orig = image.copy()

        # pre-process the image for classifihumanion
        image = cv2.resize(image, (64, 64))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
    
        # load the trained convolutional neural network
        print("[INFO] loading network...")
        model = load_model(model)

        # classify the input image
        predictions = model.predict(image)[0]
        labellist = os.listdir(dataset)
        labellist.sort()
        sortList = list(predictions)
        sortList.sort()
        label = ""
        label +=labellist[list(predictions).index(sortList[-1])]+" : "+ str(sortList[-1]*100)+" %\n";
        label +=labellist[list(predictions).index(sortList[-2])]+" : "+ str(sortList[-2]*100)+" %\n";
        label +=labellist[list(predictions).index(sortList[-3])]+" : "+ str(sortList[-3]*100)+" %\n";

        # show the output image
        return label

#print(Tester.test('data/Acer_Platanoids/Acer_Platanoids_09.ab.jpg','hundred','data'))
