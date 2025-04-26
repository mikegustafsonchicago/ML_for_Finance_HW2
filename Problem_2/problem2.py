import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

def load_data():
    """Load and prepare the articles data"""
    try:
        # Load the parquet file
        articles_df = pd.read_parquet('articles.pq')
        print("\nArticles DataFrame Shape:", articles_df.shape)
        print("\nSample of articles:")
        print(articles_df.head())
        return articles_df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure 'articles.pq' is in the same directory as this script.")
        return None

def create_prompt(headline, persona="neutral", temperature=0.7):
    """Create a prompt for topic generation"""
    base_prompt = f"""Analyze the following news headline and identify the main economic topics:
    
Headline: {headline}

Please identify the main economic topics in this headline. 
"""
    
    if persona == "bull":
        base_prompt += "\nAnalyze this from an optimistic market perspective."
    elif persona == "bear":
        base_prompt += "\nAnalyze this from a cautious market perspective."
    
    return base_prompt

def explore_headlines(articles_df):
    """Basic exploration of the headlines data"""
    if articles_df is None:
        return
    
    # Display basic statistics
    print("\n--- Headlines Statistics ---")
    print(f"Total number of articles: {len(articles_df)}")
    print("\nSample headlines:")
    print(articles_df.head())
    
    # You might want to add more visualizations here
    # For example, timeline of article counts, word clouds, etc.

def main():
    # Load the articles data
    articles_df = load_data()
    
    if articles_df is not None:
        # Explore the headlines
        explore_headlines(articles_df)
        
        # Example of prompt creation
        sample_headline = articles_df.iloc[0]['headline']  # adjust column name if needed
        
        print("\nExample prompts:")
        print("\nNeutral prompt:")
        print(create_prompt(sample_headline))
        
        print("\nBullish prompt:")
        print(create_prompt(sample_headline, persona="bull"))
        
        print("\nBearish prompt:")
        print(create_prompt(sample_headline, persona="bear"))

if __name__ == "__main__":
    main()
