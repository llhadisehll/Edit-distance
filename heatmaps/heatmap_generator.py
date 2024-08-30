import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the CSV file
df = pd.read_csv("output3.csv")

# Create a new folder to store the heatmaps
if not os.path.exists('heatmaps'):
    os.makedirs('heatmaps')

# Split the word_pair column into two separate columns
df[['word1', 'word2']] = df['word_pair'].str.split(expand=True)

# Group the data by book_name
for book_name, group in df.groupby('book_name'):
    # Filter word pairs based on similarity value
    filtered_group = group[(group['similarity'] > 0.8) & (group['similarity'] <= 0.9)]
    
    # Create a pivot table with word1 as index and word2 as columns, and similarity as values
    pivot_table = filtered_group.pivot_table(index='word1', columns='word2', values='similarity')
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 10))
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm', square=True)
    plt.title(f'Heatmap of Word Pairs for {book_name}')
    plt.xlabel('Word 2')
    plt.ylabel('Word 1')
    
    # Save the heatmap to a file
    plt.savefig(f'heatmaps/{book_name}_heatmap.png')
    plt.close()