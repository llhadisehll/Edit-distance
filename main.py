import os
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
import csv
import re

# download nltk resources
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')

def do(folder_path):
    stop_words = set(stopwords.words('english'))
    Lemmatizer = nltk.WordNetLemmatizer()

    # lists to store names and contents of books
    book_names = []
    books_contents = []
    books_sentences = []
    books_sentences_tokens = []
    books_distances = []

    # iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):  # consider only.txt files
            # read the content of the file
            with open(os.path.join(folder_path, file_name), 'r', encoding='latin-1') as file:
                content = file.read()
                #content = content[2000:2500]
                sentences = nltk.sent_tokenize(content)
                # append the file name and content to their respective lists
                book_names.append(file_name)
                books_contents.append(content)
                books_sentences.append(sentences)

                books_sentences_tokens = []
                for sentence in sentences:
                    tokens = word_tokenize(sentence.lower())
                    tokens = [token.strip() for token in tokens]
                    tokens = [token for token in tokens if token not in stop_words]
                    tokens = [Lemmatizer.lemmatize(token) for token in tokens]
                    tokens = [token for token in tokens if re.match("^['a-zA-Z]+$", token)]
                    tokens = [token for token in tokens if len(token) > 1]
                    books_sentences_tokens.append(tokens)

                book_distances = dict()
                for distance in range(1, 4):
                    book_distances[distance] = []

                books_distances.append(book_distances)

                for sentences_tokens in books_sentences_tokens:
                    for distance in range(1, 4):
                        token_pairs = book_distances[distance]
                        if len(sentences_tokens) > distance:
                            for token_index in range(0, len(sentences_tokens) - distance):
                                token_1 = sentences_tokens[token_index]
                                token_2 = sentences_tokens[token_index + distance]
                                token_pair = (token_1, token_2)

                                # Calculate Wu-Palmer similarity
                                synsets_1 = wordnet.synsets(token_1)
                                synsets_2 = wordnet.synsets(token_2)
                                if synsets_1 and synsets_2:
                                    synset_1 = synsets_1[0]
                                    synset_2 = synsets_2[0]
                                    similarity = synset_1.wup_similarity(synset_2)
                                    if similarity is not None:
                                        token_pairs.append((token_pair, similarity))

    return (
        book_names,
        books_contents,
        books_sentences,
        books_sentences_tokens,
        books_distances,
    )

# provide the path to your folder containing the books
folder_path = "books"
# call the function to read the books
book_names, books_contents, books_sentences, books_sentences_tokens, books_distances = do(folder_path)


# write the word pairs and their similarity scores to separate CSV files
#...

# write the word pairs and their similarity scores to separate CSV files
for distance in range(1, 4):
    file_name = f'word_pairs_distance_{distance}.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['book_name', 'word_pair', 'similarity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book_index, book_distances in enumerate(books_distances):
            book_name = book_names[book_index]
            pair_distance = book_distances[distance]
            for token_pairs in pair_distance:
                word_pair, similarity = token_pairs
                writer.writerow({'book_name': book_name, 'word_pair': ' '.join(word_pair), 'similarity': similarity})