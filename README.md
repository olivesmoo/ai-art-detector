# CAP5771 - Final Project
# Forged Renaissance: Using Deep Learning to Differentiate Human-Produced Art from AI Art

## Group Members
- **Olivia Mei**: om21@fsu.edu
- **Chelsea Wang**: cw20b@fsu.edu
- **Alexis Amoyo**: aga21a@fsu.edu

## Objectives
AI art generators have been under heavy scrutiny because of ethical issues relating to training art generator models using art created by artists who have not given their consent, are not getting paid, and are not credited for their work. Artists’ names will be fed into prompts in order to generate artwork with their style, creating works very similar to their original art, without having to hire them. Because of these concerns, there have been detectors developed to identify whether an artwork was generated by AI or created by an artist with varying degrees of accuracy. As new AI art generators are being developed and provided to the public, it is important to improve and develop new methods to accurately classify whether a given piece of art is machine or man-made. As a result, we chose 4 different machine learning models: ResNet50, ResNet101, VGG19, and ViT, to train on the same datasets and compare how well each of them performs.

## How to Run - The Final DATA IS MINING
To use the code, access the Google Colab Notebook [colab link](https://colab.research.google.com/drive/17TpZHDxVt-a_7xMHO3de7HSe7-MSggi1?usp=sharing) or open the Jupyter Notebook file included in this directory in Google Colab
1. Before running the code, change the Hardware Accelerator by clicking "Runtime", "Change Runtime Type", and then selecting "T4 GPU". This is important to speed up the time it takes to run the models.
2. To run all the code in a sequential fashion, select "Runtime" and then "Run all".
3. The estimated time for completion can vary, but when running with the GPU, it takes approximately an hour and 2 minutes.

## Libraries
- [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)
- [NumPy](https://numpy.org/)
- [MatPlotLib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Keras](https://www.tensorflow.org/guide/keras)
- [scikit-learn](https://scikit-learn.org/stable/)
- [io](https://docs.python.org/3/library/io.html)

## Sources
- [Art Scraper](data-parsing/artstation_scraper.py): [https://github.com/hueyning/art-station-scraper](https://github.com/hueyning/art-station-scraper)
- [WikiArt](https://www.kaggle.com/datasets/ipythonx/wikiart-gangogh-creating-art-gan)
- [Midjourney](https://doi.org/10.34740/KAGGLE/DS/2349267)
