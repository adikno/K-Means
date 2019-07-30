# K-Means
An implementation of the K_Means algorithm for image compression.
The program was written in python using numpy, matplotlib and scipy libraries, as a part of my Learning Machine course during my second year at Bar-Ilan University.

The idea was to classify each pixel in the original picture to the closest randomly-initialized centroid.
After this first match, each one of the centroid will be reset to be the average of all the pixels that was classified to it.
The algorithm repeated these two steps until convergence.
At the end, the algorithm set all of the pixels from the original picture to their classified centroid.
