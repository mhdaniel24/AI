from util import *

'''
Use this space to explain the algorithm with words
'''

'''
training is a list of tuples that contain the feature vector (phi) as a dictionary, output (y). Example: [(phi1, y1), (phi2, y2), ...., (phin, yn)]
'''
def lms(training, w, n, fetureExtractor):
    
    for example in training:
