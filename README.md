# vast-challenge-2018-mc1

Visualizations for the [VAST mini-challenge 1 (2018)](http://www.vacommunity.org/VAST+Challenge+2018+MC1).


### Demo

![demo_gif](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/docs/demo.gif)


### Requirement

To run our repository, you need to create the environement "vast" from the 'environement.yml' file.
```
conda env create -f environment.yml
```

The birds songs are not included. You need to download them and put them in the appropriate folder : 'data/ALL BIRDS' and 'data/Test Birds from Kasios'.

The software 'ffmpeg' is needed to convert the mp3 files to wav files.

```
sudo apt-get install ffmpeg
```


### Map visualizations

The repository includes two Jupyter notebooks : [basic_visualizations.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/basic_visualizations.ipynb) and [interactive_map.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/interactive_map.ipynb). You can take a look at the first one on [this](https://guillaumefrd.github.io/vast-challenge-2018-mc1/basic_visualizations.html) webpage. The second one has to be executed since it runs on a local server.

We highly recommend using [anaconda distribution](https://www.anaconda.com/) to run them. 

[Our report here](https://drive.google.com/open?id=1-K1WFsuSeG8UaD2Zj7cguEYUzXjszIWW) summarizes our works on these visualizations. 

### Sound visualizations

You will find the visualizations of the sounds in the notebook [birds_sound_visualizations.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/birds_sound_visualizations.ipynb). 

****

##### Credits

*Ruth Kueviakoe*,
*Sajeevan Puvikaran*,
*Nicolas Toussaint*,
*Guillaume Fradet*.
