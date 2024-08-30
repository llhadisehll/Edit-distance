import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the CSV file
df = pd.read_csv('output1.csv')

# Get a list of unique book names
book_names = df['book_name'].unique()

# Create a folder to save the word clouds
wordcloud_folder = 'wordclouds'
import os
if not os.path.exists(wordcloud_folder):
    os.makedirs(wordcloud_folder)

# Create a word cloud for each book
for book_name in book_names:
    book_df = df[df['book_name'] == book_name]
    word_pairs = book_df['word_pair']
    similarities = book_df['similarity']
    
    # Calculate the average similarity for each word
    word_similarities = {}
    for word_pair, similarity in zip(word_pairs, similarities):
        words = word_pair.split()
        for word in words:
            if word not in word_similarities:
                word_similarities[word] = []
            word_similarities[word].append(similarity)
    for word, sims in word_similarities.items():
        word_similarities[word] = sum(sims) / len(sims)
    
    # Create the word cloud
    wordcloud = WordCloud(width=800, height=600, max_words=100, 
                          background_color='white', 
                          stopwords=['the', 'and', 'a', 'of', 'to'])
    wordcloud.generate_from_frequencies(word_similarities)
    
    # Save the word cloud to a file
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(book_name)
    plt.savefig(os.path.join(wordcloud_folder, f'{book_name}_wordcloud.png'), dpi=300)
    plt.close()