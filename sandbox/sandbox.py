#http://ml.sun.ac.za/wordpress/wp-content/uploads/2011/08/HReikeras-SciPy-2010.pdf
#https://scikits.appspot.com/talkbox
#https://scikits.appspot.com/audiolab

from scikits.audiolab import wavread
from scikits.talkbox.features import mfcc
# data: raw audio data
# fs: sample rate
data, fs = wavread('sample.wav')[:2]
# ceps: cepstral cofficients
ceps = mfcc(input, fs=fs)[0]
