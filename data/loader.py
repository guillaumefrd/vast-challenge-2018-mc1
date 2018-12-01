import os
import pandas as pd
import numpy as np

from bokeh.palettes import Category20

from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile

#
# Parameters
#

data_path = os.path.dirname(os.path.abspath(__file__))

obs_path = os.path.join(data_path, "obs.pickle")
songs_path = os.path.join(data_path,"ALL BIRDS/")

obs_kasios_path = os.path.join(data_path, "obs_kasios.pickle")
songs_kasios_path = os.path.join(data_path,"Test Birds from Kasios/")

map_path = "https://raw.githubusercontent.com/guillaumefrd/vast-challenge-2018-mc1/master/data/map.jpg"





#
# Utilities
#

def load_songs(folder_path):
    songs = {}
    print("Loading wav files...")
    for file in os.listdir(folder_path):
        file_name, file_extension = os.path.splitext(file)
        file_path = os.path.join(folder_path, file)
        if file_extension == ".mp3":
            # Extract parameters
            params = file_name.split("-")
            song_id = params[len(params) - 1]
            wav_path = file_path.replace(".mp3", ".wav")

            # Convert mp3 to wav if necessary
            if not(os.path.isfile(wav_path)):
                # log because it can be heavy
                log_str = "\tConverting " + file + "..."
                print(log_str, end = "\r")
                # Convert sound to wav and save
                sound = AudioSegment.from_mp3(file_path)
                sound = sound.set_channels(1) # stereo to mono
                sound.export(wav_path, format='wav')  
                print(" "*(len(log_str)), end = "\r")         

            songs[song_id] = wav_path

    songs = pd.Series(songs).rename("song")
    songs.index = songs.index.astype(np.int)
    print("Done.")
    
    return songs



#
# Functions to preproc and get observations
#

def preproc_obs():
    df = pd.read_csv(os.path.join(data_path, "AllBirdsv4.csv"))
    df = df.set_index("File ID")
    df.index = df.index.astype(np.int)

    df["Y"] = df["Y"].map(lambda y: y.replace("?",""))
    df["Y"] = df["Y"].astype('int64')

    # Add a specific color for each specie according to Category20
    birds_types = df['English_name'].sort_values().unique()
    n_birds_types = len(birds_types)
    birds_types_colors = pd.Series(Category20[n_birds_types], index = birds_types).rename('color')
    df = df.join(birds_types_colors, on = "English_name")        

    # Convert date string to datetime
    a = pd.to_datetime(df['Date'], errors = 'coerce', format = "%m/%d/%Y").dropna()
    b = pd.to_datetime(df['Date'], errors = 'coerce', format = "%Y-%m-%d").dropna()
    c = pd.to_datetime(df['Date'], errors = 'coerce', format = "%Y-%m-00").dropna()
    df['T'] = pd.concat([a,b,c], axis = 0)

    # Only keep valid date
    df = df.loc[~df['T'].isna()].copy()
    
    # Save preprocessing
    df.to_pickle(obs_path)
    
    return df



def get_obs(songs = True):
    if not(os.path.isfile(obs_path)):
        df = preproc_obs()
    else:
        df = pd.read_pickle(obs_path)
        
    if songs:
        songs = load_songs(songs_path)
        df = df.join(songs)
        
    return df



#
# Functions to preproc and get KASIOS observations
#

def preproc_kasios_obs():
    df = pd.read_csv(os.path.join(data_path, "Test Birds Location.csv"))
    df.columns = ["ID", "X", "Y"]
    df = df.set_index("ID")
    
    df.to_pickle(obs_kasios_path)
    return df

def get_kasios_obs(songs = True):
    if not(os.path.isfile(obs_kasios_path)):
        df = preproc_kasios_obs()
    else:
        df = pd.read_pickle(obs_kasios_path)
        
    if songs:
        songs = load_songs(songs_kasios_path)
        df = df.join(songs)
        
    return df
