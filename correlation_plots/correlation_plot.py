import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV file
df = pd.read_csv('output3.csv')

# Create a folder to store the plots
plot_folder = 'correlation_plots'
if not os.path.exists(plot_folder):
    os.makedirs(plot_folder)

# Group the data by book_name and create a correlation plot for each book
for book_name, group in df.groupby('book_name'):
    # Create a scatter plot of similarity vs frequency
    plt.scatter(group['similarity'], group['frequency'])
    plt.xlabel('Similarity')
    plt.ylabel('Frequency')
    plt.title(f'Correlation Plot for {book_name}')
    plt.savefig(os.path.join(plot_folder, f'{book_name}_correlation_plot.png'))
    plt.close()