#http://ml.sun.ac.za/wordpress/wp-content/uploads/2011/08/HReikeras-SciPy-2010.pdf
#https://scikits.appspot.com/talkbox
#https://scikits.appspot.com/audiolab
#http://stackoverflow.com/questions/32304432/python-audio-signal-classification-mfcc-features-neural-network
'''
Requirements
pip2 install numpy
pip2 install scikits.audiolab
pip2 install scikits.talkbox
brew install libsndfile
brew link --overwrite libsndfile
sudo pip2 install scipy
'''

'''
Parameters
    ----------
    input: ndarray
        input from which the coefficients are computed

    Returns
    -------
    ceps: ndarray
        Mel-cepstrum coefficients
    mspec: ndarray
        Log-spectrum in the mel-domain.

    Notes
    -----
    MFCC are computed as follows:
        * Pre-processing in time-domain (pre-emphasizing)
        * Compute the spectrum amplitude by windowing with a Hamming window
        * Filter the signal in the spectral domain with a triangular
        filter-bank, whose filters are approximatively linearly spaced on the
        mel scale, and have equal bandwith in the mel scale
        * Compute the DCT of the log-spectrum

    References
    ----------
    .. [1] S.B. Davis and P. Mermelstein, "Comparison of parametric
           representations for monosyllabic word recognition in continuously
           spoken sentences", IEEE Trans. Acoustics. Speech, Signal Proc.
           ASSP-28 (4): 357-366, August 1980."""

    https://www.researchgate.net/publication/261914482_Feature_Extraction_Methods_LPC_PLP_and_MFCC_In_Speech_Recognition

    Source Code
    -----------
    https://github.com/cournape/talkbox
'''

from scipy.io.wavfile import read as wavread
from scikits.talkbox.features import mfcc
from scikits.talkbox.linpred.levinson_lpc import *
# data: raw audio data
# fs: sample rate
sr, signal =  wavread('../recordings/obama.wav')
# ceps: cepstral cofficients
coeffs=13
ceps, mspec, spec = mfcc(signal, nwin=2048, nfft=2048, fs=sr, nceps=coeffs)
print ("************************ MFCC ************************")
print (ceps)

# https://github.com/cournape/talkbox/blob/ee0ec30a6a6d483eb9284f72bdaf26bd99765f80/scikits/talkbox/linpred/levinson_lpc.py
lpcResult = lpc(signal,1)
print ("************************ LPC ************************")
print (lpcResult)