# The analysis and visualization project of the similarity of words in texts

This project involves processing textual data (books in `.txt' format) that calculates word similarity using the Wu-Palmer method from WordNet. The results are then saved as CSV files and various types of visualizations such as bar charts, scatter charts, correlation charts, heat maps and keywords are created.

## Table of contents

- [Prerequisites] (#prerequisites)
- [installation and setup] (#install-and-setup)
- [Usage guide] (#guide-to-use)
- [code description] (#code-description)
- [outputs] (#outputs)
- [visualizations] (#visualizations)
- [Folder structure] (#structure-folders)
- [Remarks] (#remarks)
- [Gratitude] (#Gratitude)

## Prerequisites

To implement this project, you need the following:

- Python 3.7 or higher
- Required libraries:
 - ``nltk``
 - ``pandas``
 - `matplotlib`
 - ``seaborn``
 - ``wordcloud``
 - ``plotly``

## Installation and commissioning

1. First, clone the project repository:
 ```bash
 git clone https://github.com/your-repository.git
 cd your-repository
 ```

2. Install the required libraries:
 ```bash
 pip install -r requirements.txt
 ```

3. Download the required NLTK resources:
 ```python
 import nltk
 nltk.download('stopwords')
 nltk.download('punkt')
 nltk.download('wordnet')
 ```

## Usage guide

1. Place your text books in ``books'' folder. These files must be in `.txt' format.

2. Run the main script to process the books and generate the CSV files:
 ```bash
 python main.py
 ```

3. The generated CSV files are placed in the current folder and have names such as `output1.csv`, `output2.csv`, and `output3.csv`, which refer to the space between words.

## Visualization production

### Bar charts
To generate bar charts, update the output_folder path of bar_charts.py to the storage path.
Run the script:
``` bar_charts.py```

### Scatter plots
To generate scatter plots from CSV files, run the script:
``` scatter_plots.py```

### Correlation charts
In correlation_plot.py, update the output3.csv file path if needed.
Run the script:

``` correlation_plot.py```

### Thermal maps
In ``heatmaps.py``, modify the design path of heat maps if needed.
Run the script:
``` heatmaps.py```

 ### Factory visualizations
In `interactive_plots.py`, update the file path if needed.
Run the script:
```python interactive_plots.py```

 ### Generate keywords
In `wordclouds.py`, make the directory path of `wordcloud_folder` if needed.
Run the script:
``wordclouds.py``

## Description of the code

### Text processing

The main script (`do' function) consists of the following steps:

- **Removal of stop words and punctuation:** Stop words (such as "the", "and") are removed from the texts and the words are converted into the base form (lemmatize).

- **Computation of word similarity:** For each pair of words in certain intervals (1 to 3 words), the similarity between them is calculated using the Wu-Palmer method.

- **Generate CSV files:** Word pairs and their similarity scores are stored in separate CSV files for each interval.

### Data visualization

After data processing, several types of visualization are performed:

- **Bar graphs:** Average similarity and distance for each book are displayed in bar graphs.

- **Scatter charts:** These charts show the relationship between similarity and word distance.

- **Heat maps:** Similarities between specific pairs of words are displayed as a heat map.

- **Superwords:** Based on the similarity of words, superwords are created for each book.

### Side scripts

In addition to the main script, there are a few side scripts to generate additional charts and visualizations:

- `bar_charts.py`: Productions of average similarity and distance bars.
- `correlation_plots.py`: generate correlation plots for word similarity and frequency.
- `heatmap_generator.py`: generating heatmaps based on the similarity of pairs of words.
- `scatter_plots.py`: generate scatter plots for similarity and distance.
- `wordcloud_generator.py`: generate keywords for each book.
## Outputs

After running the scripts, the following outputs are produced:

- **CSV files:** containing pairs of words and their similarity scores.
- **Bar charts:** stored in `plots` folder.
- **Scatter plots:** stored in `plots` folder.
- **Heatmaps:** stored in `heatmaps` folder.
- **Superwords:** stored in `wordclouds` folder.
- **Interactive visualizations:** stored in `book_visualizations' folder as HTML files.

## Visualizations

### Bar charts

Bar graphs show average similarity and distance for each book. These charts help to identify the overall similarity and variation between pairs of words within each book.

### Scatter plots

These graphs show the relationship between the similarity of pairs of words and their frequency and help to identify patterns of word usage in different books.

### Thermal maps

Heatmaps show the similarities between specific pairs of words. These maps are especially useful for viewing high similarities (between 0.8 and 0.9).

### Keywords

Keywords are created for each book and generated based on word similarity. These keywords provide a quick and visual summary of the most important words in each book.

### Interactive visualizations

Interactive charts are created using Plotly and saved as HTML files that you can open in a web browser.

## Folder structure

The structure of the project folders is as follows:

```
project_root/
│
├── books/ # Folder containing text books
├── plots/ # Folder containing bar and scatter charts
├── heatmaps/ # Folder containing heatmaps
├── wordclouds/ # Folder containing keywords
├── book_visualizations/# Folder containing interactive visualizations
├── output/ # Folder containing output CSV files
├── readme.py #project description
└── main.py # Main script
```

## Remarks

- **INPUT FILES FORMAT:** Make sure that the input files are in the correct
 `.txt` format and are in the `books` folder.

- **Efficiency:** Due to the number and volume of books, processing may take time. Therefore, it is recommended to do a short test first for large books.

- **Similarity sensitivity:** The Wu-Palmer method calculates semantic similarities between words, but the results may not always be accurate. Therefore, the interpretation of the results should be done carefully.

## Appreciation

- The [NLTK] (https://www.nltk.org/) library has been used to process natural language and calculate word similarities.
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) were used to generate graphs and visualize data.
- [Plotly](https://plotly.com/) was used to create interactive charts.
- [WordCloud](https://github.com/amueller/word_cloud) is used to generate keywords.