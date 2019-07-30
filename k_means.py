import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import os

def init_centroids(K):
    """
    Initializes K centroids that are to be used in K-Means on the dataset X.

    Parameters
    ----------
    X : ndarray, shape (n_samples, n_features)
        Samples, where n_samples is the number of samples and n_features is the number of features.
    K : int
        The number of centroids.

    Returns
    -------
    centroids : ndarray, shape (K, n_features)
    """
    if K == 2:
        return np.asarray([[0.        , 0.        , 0.        ],
                            [0.07843137, 0.06666667, 0.09411765]])
    elif K == 4:
        return np.asarray([[0.72156863, 0.64313725, 0.54901961],
                            [0.49019608, 0.41960784, 0.33333333],
                            [0.02745098, 0.        , 0.        ],
                            [0.17254902, 0.16862745, 0.18823529]])
    elif K == 8:
        return np.asarray([[0.01568627, 0.01176471, 0.03529412],
                            [0.14509804, 0.12156863, 0.12941176],
                            [0.4745098 , 0.40784314, 0.32941176],
                            [0.00784314, 0.00392157, 0.02745098],
                            [0.50588235, 0.43529412, 0.34117647],
                            [0.09411765, 0.09019608, 0.11372549],
                            [0.54509804, 0.45882353, 0.36470588],
                            [0.44705882, 0.37647059, 0.29019608]])
    elif K == 16:
        return np.asarray([[0.61568627, 0.56078431, 0.45882353],
                            [0.4745098 , 0.38039216, 0.33333333],
                            [0.65882353, 0.57647059, 0.49411765],
                            [0.08235294, 0.07843137, 0.10196078],
                            [0.06666667, 0.03529412, 0.02352941],
                            [0.08235294, 0.07843137, 0.09803922],
                            [0.0745098 , 0.07058824, 0.09411765],
                            [0.01960784, 0.01960784, 0.02745098],
                            [0.00784314, 0.00784314, 0.01568627],
                            [0.8627451 , 0.78039216, 0.69803922],
                            [0.60784314, 0.52156863, 0.42745098],
                            [0.01960784, 0.01176471, 0.02352941],
                            [0.78431373, 0.69803922, 0.60392157],
                            [0.30196078, 0.21568627, 0.1254902 ],
                            [0.30588235, 0.2627451 , 0.24705882],
                            [0.65490196, 0.61176471, 0.50196078]])
    else:
        print('This value of K is not supported.')
        return None

# data preperation (loading, normalizing, reshaping)
def loading():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/dog.jpeg'
    A = imread(path)
    return A.astype(float) / 255.

def calcDistance(img_size, pixle, centroid):
    distance = 0
    for RGB in range(img_size):
        distance = distance + pow(abs(pixle[RGB] - centroid[RGB]), 2)
    return distance

def printCentroids(iter, cent):
    print("iter {}: ".format(iter), end='')
    if type(cent) == list:
        cent = np.asarray(cent)
    if len(cent.shape) == 1:
        print(' '.join(str(np.floor(100 * cent) / 100).split()).replace('[ ', '[').replace('\n', ' ').replace(' ]', ']').replace(' ', ', '))
    else:
        print(' '.join(str(np.floor(100 * cent) / 100).split()).replace('[ ', '[').replace('\n', ' ').replace(' ]', ']').replace(' ', ', ')[1:-1])

def findMin(distanceArray):
    minDis = 255
    minIndex = 0
    for i in range(len(distanceArray)):
        if(distanceArray[i] < minDis):
            minDis = distanceArray[i]
            minIndex = i
    return minIndex

def updateCentroids(k, i, img_size, centroids):
    countArray = [0] * k
    sumArray = [0] * k
    for height in range(img_size[0]):
        for width in range(img_size[1]):
            distanceArray = []
            for centroid in range(k):
                distanceArray.append(calcDistance(img_size[2], A_norm[height][width], centroids[centroid]))
            min = findMin(distanceArray)
            countArray[min] = countArray[min] + 1
            sumArray[min] = sumArray[min] + A_norm[height][width]
            if (i == 10):
                A_norm[height][width] = centroids[min]
    for centroid in range(k):
        if (countArray[centroid] != 0):
            centroids[centroid] = sumArray[centroid] / countArray[centroid]
    printCentroids(i, centroids)

def iteration(k, centroids, img_size):
    print("k={}:".format(k))
    printCentroids(0, centroids)
    for i in range(1, 11):
        updateCentroids(k, i, img_size, centroids)

i = 2
while (i <= 16):
    A_norm = loading()
    img_size = A_norm.shape

    centroids = init_centroids(i)
    iteration(i, centroids, img_size)

    i = i * 2