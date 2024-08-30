import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs('plots', exist_ok=True)

df2 = pd.read_csv('output1.csv')
df1 = pd.read_csv('output2.csv')
df3 = pd.read_csv('output3.csv')

df = pd.concat([df1, df2, df3])

for name, sub_df in df.groupby('book_name'):
    sns.scatterplot(x='similarity', y='distance', data=sub_df)
    plt.savefig(f'plots/book_{name}.png')
#    plt.clf()