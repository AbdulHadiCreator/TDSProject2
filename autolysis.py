# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "pandas",
#   "numpy",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "openai",
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# Ensure the script is run with a CSV filename argument
if len(sys.argv) != 2:
    print("Usage: uv run autolysis.py <dataset.csv>")
    sys.exit(1)

csv_file = sys.argv[1]

if not os.path.exists(csv_file):
    print(f"Error: File '{csv_file}' not found.")
    sys.exit(1)

# Set up the AIPROXY_TOKEN environment variable
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)

# Load the dataset
try:
    df = pd.read_csv(csv_file)
    print(f"Loaded dataset '{csv_file}' with shape {df.shape}")
except Exception as e:
    print(f"Error loading CSV file: {e}")
    sys.exit(1)

def basic_analysis(data):
    """Perform basic analysis on the dataset."""
    analysis = {
        "head": data.head(5).to_dict(orient="records"),
        "columns": list(data.columns),
        "description": data.describe(include="all").to_dict(),
        "missing_values": data.isnull().sum().to_dict()
    }
    return analysis

def generate_visualizations(data, output_prefix):
    """Generate visualizations for the dataset."""
    paths = {}

    # Correlation Heatmap
    if not data.select_dtypes(include="number").empty:
        corr = data.corr(numeric_only=True)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        heatmap_path = f"{output_prefix}_correlation_heatmap.png"
        plt.title("Correlation Heatmap")
        plt.savefig(heatmap_path)
        plt.close()
        paths["heatmap"] = heatmap_path

    # Histograms for numeric columns
    numeric_cols = data.select_dtypes(include="number").columns
    paths["histograms"] = []
    for column in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True, color="blue")
        plt.title(f"Histogram of {column}")
        hist_path = f"{output_prefix}_{column}_histogram.png"
        plt.savefig(hist_path)
        plt.close()
        paths["histograms"].append(hist_path)

    return paths

def ask_llm(prompt):
    """Send a prompt to the LLM via AIProxy and return the response."""
    api_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a data analysis assistant."},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: LLM request failed with status {response.status_code}")
        print(response.text)
        sys.exit(1)

def narrate_analysis(data_summary, visualizations):
    """Use the LLM to narrate the analysis and generate a story."""
    prompt = f"""
    Dataset Analysis Summary:
    - Columns: {data_summary['columns']}
    - Missing Values: {data_summary['missing_values']}
    - Key Statistics: {data_summary['description']}

    Visualizations include:
    - Correlation Heatmap
    - Histograms of numeric columns

    Please summarize the dataset analysis into a story with insights and recommendations.
    """
    return ask_llm(prompt)

# Main script logic
if __name__ == "__main__":
    print("Performing analysis...")

    # Perform basic analysis
    data_summary = basic_analysis(df)

    # Generate visualizations
    output_prefix = os.path.splitext(os.path.basename(csv_file))[0]
    visualizations = generate_visualizations(df, output_prefix)

    # Generate narrative using LLM
    story = narrate_analysis(data_summary, visualizations)

    # Create README.md with results
    with open("README.md", "w") as f:
        f.write("# Automated Data Analysis Report\n\n")
        f.write(f"## Dataset: {csv_file}\n\n")
        f.write("### Basic Analysis\n")
        f.write(f"- Columns: {data_summary['columns']}\n")
        f.write(f"- Missing Values: {data_summary['missing_values']}\n\n")
        f.write("### Key Insights\n")
        f.write(story + "\n\n")
        f.write("### Visualizations\n")
        if "heatmap" in visualizations:
            f.write(f"![Correlation Heatmap]({visualizations['heatmap']})\n")
        for hist in visualizations["histograms"]:
            f.write(f"![Histogram: {hist}]({hist})\n")

    print("Analysis completed. Results saved to 'README.md'.")
