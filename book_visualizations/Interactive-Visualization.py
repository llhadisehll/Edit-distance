import os
import pandas as pd
import plotly.express as px

FIG_WIDTH = 800
FIG_HEIGHT = 1000

def load_data(file_path: str) -> pd.DataFrame:
    """Load the CSV file"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def create_figure(group_data: pd.DataFrame, color: str) -> px.scatter:
    """Create a figure for a single book with a specified color"""
    fig = px.scatter(group_data, x="word_pair", y="similarity", title=group_data['book_name'].iloc[0], color="book_name", color_discrete_sequence=[color])
    fig.update_traces(hovertemplate="%{text}<br>%{y:.2f}", text=[f"{row['book_name']}: {row['word_pair']}" for index, row in group_data.iterrows()])
    fig.update_layout(height=FIG_HEIGHT, width=FIG_WIDTH)
    return fig

def save_figure(fig: px.scatter, file_path: str) -> None:
    """Save the figure to an HTML file"""
    if not os.path.exists("book_visualizations"):
        os.makedirs("book_visualizations")
    fig.write_html(os.path.join("book_visualizations", file_path))

def main() -> None:
    file_path = "output3.csv"
    df = load_data(file_path)
    if df is not None:
        book_groups = df.groupby('book_name')
        book_colors = list(px.colors.qualitative.Plotly)
        for i, (name, group) in enumerate(book_groups):
            fig = create_figure(group, book_colors[i % len(book_colors)])
            save_figure(fig, f"{name}_similarities.html")
            fig.show()

if __name__ == "__main__":
    main()