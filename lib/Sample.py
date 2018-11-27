from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

class Sample:

#
#   FONCTION D'INITIALISATION
#

    def __init__(self, T, data = []):
        # Variables brut
        self.data = data #Points de l'echantillon
        self.T = T # Duree de l'echantillon
        self.size = data.size # Nombre de point

        # Varibles pour la TFD
        self.tfd = None # Transformee de fourrier discrete
        self.freq = None # Fondamentale de la TFD
        self.amp = None # Amplitude de la fondamentale

        # Autres variables
        self.fe = self.size/self.T



#
#   FONCTION DE TRAITEMENT
#

    #   Calcul les caracteristiques -> (F et Amp)
    def calculCarac(self):
        amp, freq = self.getTFD() # Retourne la tfd entre 500Hz et 1200Hz
        i_max = 0
        f_max = 0
        for i in range(len(freq)):
            if amp[i] > i_max :
                i_max = amp[i]
                f_max = freq[i]
        self.freq = f_max
        self.amp = i_max
        return self



    #   Retourne la tfd
    def getTFD(self):
        if self.tfd != None:
            return self.tfd

        # Calcule la ftt
        tfd = np.fft.fft(self.data)
        amp = np.absolute(tfd)
        freq = np.arange(0,len(self.data))/self.T

        # Recupere la tfd entre 500Hz et 1600Hz et la stocke
        self.tfd = self.filtre((amp, freq), 1900, 6000)

        # Retourne la tfd
        return self.tfd



    #   Retourne les frequences de [ xHz ; yHz ]
    def filtre(self, tfd, x, y):
        amp, freq = tfd

        i = int(x*self.T)
        j = int(y*self.T)

        amp = amp[i:j]
        freq = freq[i:j]

        return (amp,freq)



#
#   FONTIONS D'INTERFACE
#

    #   Retourne la fondamentale
    def getFreq(self):
        if self.freq == None:
            self.calculCarac()

        return self.freq




    #   Retourne l'amplitude de la fondamentale
    def getAmp(self):
        if self.amp == None:
            self.calculCarac()

        return self.amp



    #   Retourne la frequence d'echantillon
    def getFe(self):
        return self.fe



    #   Defini la frequence
    def setFreq(self, freq):
        self.freq = freq



    #   Defini l'amplitude
    def setAmp(self,amp):
        self.amp = amp
        return self


    #   Defini la note en silence
    def setSilence(self):
        self.setFreq(0)
        return self
    
    def isSilence(self):
        return self.freq == 0



#
#   FONCTION D'AFFICHAGE
#

    #   Affiche le spectre
    def spectre(self):
        amp, freq = self.getTFD()
        plt.plot(freq,amp)
        plt.show()



    #   Retourne une string de description
    def __str__(self):
        return "Sample : F = " + str(self.getFreq()) + "Hz || I = " + str(self.getAmp()) + " || Fe = " + str(self.getFe()) + "Hz || N = " + str(len(self.data)) + " || T = " + str(self.T) + "s || Seuil = " + str(self.getSeuil())
