import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# Set random seed for reproducibility
np.random.seed(42)

def load_data():
    """
    Load and prepare the data files needed for the analysis
    """
    try:
        # Load the articles data
        articles_df = pd.read_parquet('articles.pq')
        
        # Load the topics data
        topics_df = pd.read_csv('topics.csv')
        
        # Load the macro data
        macro_df = pd.read_csv('macro.csv')
        
        return articles_df, topics_df, macro_df
    
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        print("Please ensure all required files are in the correct directory")
        return None, None, None

def explore_data(articles_df, topics_df, macro_df):
    """
    Basic data exploration and visualization
    """
    print("\nArticles Dataset Info:")
    print(articles_df.info())
    print("\nSample of articles:")
    print(articles_df.head())
    
    print("\nTopics Dataset Info:")
    print(topics_df.info())
    print("\nSample of topics:")
    print(topics_df.head())
    
    # Plot number of articles over time
    if 'date' in articles_df.columns:
        articles_df['date'] = pd.to_datetime(articles_df['date'])
        monthly_counts = articles_df.resample('M', on='date').size()
        
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_counts.index, monthly_counts.values)
        plt.title('Number of Articles per Month')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Load the data
    articles_df, topics_df, macro_df = load_data()
    
    if articles_df is not None:
        # Explore and visualize the data
        explore_data(articles_df, topics_df, macro_df)

if __name__ == "__main__":
    main()
