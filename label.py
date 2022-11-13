import matplotlib.pyplot as plt
import os
from PIL import Image
from numpy import asarray
import numpy as np
import pickle


train_images = np.zeros(shape=(1000, 300, 300, 3))
train_labels = np.zeros(shape=(1000, 1))

data = os.listdir("Data")
label = 0
count = 0

for i in data:
    images = os.listdir("Data/" + i)
    for image in images:
        img = Image.open("Data/" + i + "/" + image)
        npdata = asarray(img)
        train_images[count] = npdata
        train_labels[count] = np.array(label)
    label += 1
        
train_images = train_images / 255.0

with open("train_images.pickle", "wb") as ofile:
    pickle.dump(train_images, ofile)
with open("train_labels.pickle", "wb") as ofile:
    pickle.dump(train_labels, ofile)
