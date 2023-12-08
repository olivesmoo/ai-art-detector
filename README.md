# Forged Renaissance: Using Deep Learning to Differentiate Human-Produced Art from AI Art

Code: You must submit all the Matlab / Python code files used and developed during and for this
project. The codes are expected to run in sequential fashion, that is, one trigger must make the
whole code run in sequence without any disruption, until results (visual and metric) are produced.
Please include an estimated time for completion and display real-time progress on the code (such
as “Training Completed” etc.). Please also provide adequate comments in the code files.
Include a README file containing detailed instructions on how to run the code. Also include any
libraries that are used in your implementation. The instructor should be able to compile and run
the code in his machine and generate the results produced in the report.
In any cases of borrowed code, be it from forums or external sources, appropriate citation must be
provided. Borrowing code without appropriate citation will be considered a violation of academic
integrity.
Submit the code files and the project report (in PDF format) as a single zip file through Canvas.
Only one submission is required from each project team.
## Running the Code
- To use the code, access the [colab link](https://colab.research.google.com/drive/17TpZHDxVt-a_7xMHO3de7HSe7-MSggi1?usp=sharing) or open the Jupyter Notebook file included in this directory in Google Colab
- Before running the code, change the Hardware Accelerator by clicking "Runtime", "Change Runtime Type", and then selecting "T4 GPU". This is important to speed up the time it takes to run the models.
- To run all the code in a sequential fashion, select "Runtime" and then "Run all".
- The estimated time for completion can vary, but when running with the GPU, it takes approximately ____. If running with the CPU, it takes approximately ____.

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
[Art Scraper](data-parsing/artstation_scraper.py): [https://github.com/hueyning/art-station-scraper](https://github.com/hueyning/art-station-scraper)
