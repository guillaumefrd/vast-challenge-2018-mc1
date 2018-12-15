# vast-challenge-2018-mc1

Visualizations for the [VAST mini-challenge 1 (2018)](http://www.vacommunity.org/VAST+Challenge+2018+MC1).

## Our work

Check our work and visualization **without the need to run anything**, thanks to these html links:

1. [basic map](https://guillaumefrd.github.io/vast-challenge-2018-mc1/html/1_basic_map.html)
2. [dynamic map](https://guillaumefrd.github.io/vast-challenge-2018-mc1/html/2_dynamic_map.html) (you need to run this since it runs on a local server)
3. [amplitude analysis](https://guillaumefrd.github.io/vast-challenge-2018-mc1/html/3_amplitude_analysis/3_amplitude_analysis.html)
4. [spectral analysis](https://guillaumefrd.github.io/vast-challenge-2018-mc1/html/4_spectral_analysis/4_spectral_analysis.html)
5. [classification (machine learning)](https://guillaumefrd.github.io/vast-challenge-2018-mc1/html/5_classification_ml/5_classification_ml.html)
6. [conclusion](https://docs.google.com/presentation/d/1oOwXbxa9OBZ5nYgeAn8yLO9sveuYgXnVLya9_R1UvwM/edit?usp=sharing)

### Demo of the dynamic map

![demo_gif](https://raw.githubusercontent.com/guillaumefrd/vast-challenge-2018-mc1/master/docs/demo.gif)

## Notebooks 

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

- [1_basic_map.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/1_basic_map.ipynb)
- [2_dynamic_map.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/2_dynamic_map.ipynb)
- [report](https://drive.google.com/open?id=1-K1WFsuSeG8UaD2Zj7cguEYUzXjszIWW):  summary of our work on these visualizations.

### Sound visualizations

- [3_amplitude_analysis.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/3_amplitude_analysis.ipynb)
- [4_spectral_analysis.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/4_spectral_analysis.ipynb)
- [5_classification_ml.ipynb](https://github.com/guillaumefrd/vast-challenge-2018-mc1/blob/master/5_classification_ml.ipynb)


****

##### Credits

*Ruth Kueviakoe*,
*Sajeevan Puvikaran*,
*Nicolas Toussaint*,
*Guillaume Fradet*.
