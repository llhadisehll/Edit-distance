import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the output folder
output_folder = 'path/to/output/folder'

# Define the list of CSV files
files = ['output1.csv','output2.csv','output3.csv']

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file
for file in files:
    # Read the CSV file
    df = pd.read_csv(file)

    # Group the data by book_name
    grouped = df.groupby('book_name')

    # Loop through each book
    for book_name, book_data in grouped:
        # Calculate the mean similarity and distance for each book
        avg_similarity = book_data['similarity'].mean()
        avg_distance = book_data['distance'].mean()

        # Plot the bar chart
        fig, ax = plt.subplots()
        ax.bar(x=['Similarity', 'Distance'], height=[avg_similarity, avg_distance], label=[book_name, ''])
        ax.set_xlabel('')
        ax.set_ylabel('Value')
        ax.set_title(f"Book: {book_name}")
        ax.legend()

        # Save the plot as a PNG file in the output folder
        output_file = os.path.join(output_folder, f"{book_name}.png")
        plt.savefig(output_file, bbox_inches='tight')

        # Close the figure to free up memory
        plt.close(fig)