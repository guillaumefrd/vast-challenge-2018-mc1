from __future__ import division
import scipy.io.wavfile as wave
from lib.Sample import Sample
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt


class File:

#
#   FONCTION D'INITIALISATION
#

    def __init__(self, file, tc = 0.1):

        fe,data = wave.read(file)

        # Gere la stereo
        if len(data.shape) == 1:
            self.data = data # On prend l'unique voie
        else:
            self.data = data[:, 0] # On ne prend que la voix de droite

        # Variables Principales
        self.fe = fe #Frequence d'echantillonage
        self.tc = tc # Duree des samples
        self.ns = int(tc * fe) # Nombre de point par sample
        self.size = int((self.data.size + 1)/self.ns) # Nombre d'echantillon
        self.samples = [None] * self.size # Tableau de stockage des samples (iniatialement vide)
        self.i_cut = 0 # Valeur de cut de l'intensite

        # Variable d'iteration
        self.n_iter = -1
        self.n_calculed = 0
        
        self.cut_low_sound()




    #   Defini les silences
    def cut_low_sound(self):
        I = np.zeros(self.size)
        for i, e in enumerate(self):
           I[i] = e.getAmp()
        #self.i_cut = np.quantile(I, 0.3)*3
        self.i_cut = np.mean(I) + 1.5*np.std(I)
        
        
##        # Calcul intensite moyenne
##        sum = 0
##        for e in self:
##            sum += e.getAmp()
##        self.i_cut = sum/self.getSize()

        # Calcul intesite moyenne des minimums
#        n_min = 0
#        sum_min = 0
#        for i in range(1, self.getSize() - 1):
#            back_i = self[i-1].getAmp()
#            sample_i = self[i].getAmp()
#            next_i = self[i+1].getAmp()
#            if (sample_i < back_i and sample_i < next_i ): #si minimum
#                n_min += 1
#                sum_min += sample_i
#        self.i_cut = min(int(sum_min/n_min),1000000) #Mix i_min et i_moy_on_min

        # Defini les silences
        for e in self:
            if e.getAmp() < self.i_cut:
                e.setSilence()

        return self



#
#   FONCTION D'INTERFACE
#

    #   Retourne le x ieme echantillon
    def __getitem__(self,x):
        # Gestion des index trop grand
        max_x = self.getSize()
        if max_x <= x :
            if self.n_iter != -1: # Stop iteration boucle for
                self.n_iter = -1
                raise StopIteration
            else: # Raise error for array request
                raise ValueError("Index '" + str(x) + "' hors du fichier ! ( Size = " + str(self.getSize()) + " )")


        # Creation du sample s'il n'existe pas
        if self.samples[x] == None:
            i = self.ns * x
            j = self.ns * (x + 1) - 1
            self.samples[x] = Sample(self.tc, self.data[i:j])
            #self.show_progress()

        return self.samples[x]


    # Retourne le nombre d'echantillon
    def getSize(self):
        return self.size

    def getTimeSample(self):
        return self.tc
    
    
    def getNormalizedSpectre(self):
        sum_amps = None
        N_used = 0
        for sample in self:
            if sample.isSilence():
                continue
            amp, freq = sample.getTFD()
            sum_amps = amp if sum_amps is None else (sum_amps + amp)
            N_used += 1
        if sum_amps is None:
            return None, None
        else:
            amps_normed = sqrt(N_used) * (sum_amps - np.mean(sum_amps))/np.std(sum_amps) # Normalizing
            return amps_normed, freq



#
#   FONCTION D'AFFICHAGE
#
    def plotFreq(self, name="Frequence"):
        x = range(self.getSize())
        F= []
        for e in self:
            F.append(e.getFreq())

        plt.figure(name)
        plt.plot(x,F)
        plt.suptitle(name)

        plt.ylabel("Frequence")
        plt.xlabel("Echantillon")
        plt.axis([0,self.getSize()-1,0,max(max(F), 1400)])
        return self



    def plotAmp(self, name="Amplitude"):
        x = range(self.getSize())
        A = []
        for e in self:
            A.append(e.getAmp())

        plt.figure(name)
        plt.plot(x,A)
        plt.plot(x,[self.i_cut] * self.getSize()) # Plot la ligne de cut
        plt.suptitle(name)

        plt.ylabel("Amplitude")
        plt.xlabel("Echantillon")
        plt.axis([0,self.getSize()-1,0,max(A)])
        return self



    def plotNotes(self, name="Notes"):
        x = range(self.getSize())
        f = []
        for e in self:
            f.append(e.getNote().getFreq())

        plt.figure(name)
        plt.plot(x,f)
        plt.suptitle(name)

        plt.ylabel("Frequence")
        plt.xlabel("Echantillon")
        plt.axis([0,self.getSize()-1,100,1600])
        return self



    def plotAll(self):
      self.plotFreq().plotAmp().plotNotes()
      return self


    # Affiche les 4 graphiques caracteristiques (F, Fex, I, A)
    def show(self):

        # Recuperation des valeurs pour les graphiques
        x = range(self.getSize())
        I, F, A, Fex = [], [], [], []
        for e in self:
            F.append(e.getFreq())
            A.append(e.getAmp())


        # Affichage des graphiques
        plt.figure("Fichier")

        # Affichage fondamentale TFD
        plt.subplot(221)
        plt.plot(x,F)
        plt.ylabel('Fondamentale')
        plt.xlabel("Echantillon")

        # Affiche fondamentale Note
        plt.subplot(222)
        plt.plot(x,Fex)
        plt.axis([0,self.getSize()-1,100,1600])
        plt.ylabel('Fondamentale Exact')
        plt.xlabel("Echantillon")

        # Affichage Spectre
        plt.subplot(223)
        plt.plot(x,A)
        plt.ylabel('Amplitude Fondamentale')
        plt.xlabel("Echantillon")

        # Affichage de la fenetre
        plt.show()

        return self


    # Retourne une string de description
    def __str__(self):
        return "File de " + str(self.getSize()) + " echantillons de " + str(self.tc) + "s"



#
#   FONCTION D'ITERATION
#

    def __iter__(self):
    	# Initialision Variable d'iteration
    	self.n_iter = -1
    	return self


    def __next__(self):
        self.n_iter += 1
        return self.__getitem__(self.n_iter)



#
#   FONCTION CUSTOM
#

    def show_progress(self):
        self.n_calculed += 1

        if (self.n_calculed % (round(0.1*self.getSize())) == 0):
            print(str(round(self.n_calculed / self.getSize() * 100)) + "%")

        return self