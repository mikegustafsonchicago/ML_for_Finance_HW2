import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Data loading
def load_data():
    try:
        # Load the datasets
        topics_df = pd.read_csv('topics.csv')
        macro_df = pd.read_csv('macro.csv')
        
        print("\nTopics DataFrame Shape:", topics_df.shape)
        print("Macro DataFrame Shape:", macro_df.shape)
        
        return topics_df, macro_df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure 'topics.csv' and 'macro.csv' are in the same directory as this script.")
        return None, None

def explore_data(topics_df, macro_df):
    """Basic data exploration and visualization"""
    
    # Display basic information about the datasets
    print("\n--- Topics DataFrame Info ---")
    print(topics_df.head())
    print("\nTopics DataFrame Columns:", topics_df.columns.tolist())
    
    print("\n--- Macro DataFrame Info ---")
    print(macro_df.head())
    print("\nMacro DataFrame Columns:", macro_df.columns.tolist())
    
    # Visualize market returns distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(macro_df['mret'], kde=True)
    plt.title('Distribution of Market Returns')
    plt.xlabel('Market Returns')
    plt.ylabel('Count')
    plt.show()
    
    # Create a correlation heatmap for macro variables
    plt.figure(figsize=(12, 8))
    macro_corr = macro_df.corr()
    sns.heatmap(macro_corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Macro Variables')
    plt.tight_layout()
    plt.show()

def main():
    # Load the data
    topics_df, macro_df = load_data()
    
    if topics_df is not None and macro_df is not None:
        # Explore and visualize the data
        explore_data(topics_df, macro_df)

if __name__ == "__main__":
    main()
