# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "pandas",
#   "numpy",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "openai",
#   "scikit-learn",
#   "tabulate",
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

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

# Load the dataset with encoding handling
try:
    df = pd.read_csv(csv_file, encoding="utf-8")
except UnicodeDecodeError:
    print("UTF-8 decoding failed. Attempting with 'latin-1' encoding.")
    try:
        df = pd.read_csv(csv_file, encoding="latin-1")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

print(f"Loaded dataset '{csv_file}' with shape {df.shape}")

# Get dataset name without extension
dataset_name = os.path.splitext(os.path.basename(csv_file))[0]

# Create output directory for the dataset
output_dir = os.path.join(os.getcwd(), dataset_name)
os.makedirs(output_dir, exist_ok=True)

# Variables to store results for README
outlier_results = []
feature_importance_results = None
distribution_results = []
story = None
recommendations = "No specific recommendations were generated."
conclusions = "No specific conclusions were drawn."


def basic_analysis(data):
    """Perform basic analysis on the dataset."""
    analysis = {
        "head": data.head(5).to_dict(orient="records"),
        "columns": list(data.columns),
        "description": data.describe(include="all").to_dict(),
        "missing_values": data.isnull().sum().to_dict()
    }
    return analysis


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


def suggest_analysis(data_summary):
    """Suggest additional analyses dynamically using LLM."""
    prompt = f"""
    Dataset Summary:
    - Columns: {data_summary['columns']}
    - Missing Values: {data_summary['missing_values']}
    - Key Statistics: {data_summary['description']}
    
    Suggest analyses that would yield meaningful insights from this dataset.
    """
    return ask_llm(prompt)


def narrate_analysis(data_summary, analyses):
    """Generate a cohesive story using LLM."""
    global story, recommendations, conclusions
    prompt = f"""
    Dataset Analysis Summary:
    - Columns: {data_summary['columns']}
    - Missing Values: {data_summary['missing_values']}
    - Key Statistics: {data_summary['description']}

    Additional Analysis Results:
    {analyses}

    Provide:
    - Key Insights
    - Dataset Overview
    - Key Findings
    - Recommendations
    - Conclusions
    """
    story = ask_llm(prompt)
    return story


def generate_visualizations(data, output_prefix):
    """Generate up to 7 meaningful visualizations for the dataset."""
    paths = {}

    # Correlation Heatmap
    numeric_cols = data.select_dtypes(include="number").columns
    if not numeric_cols.empty:
        corr = data[numeric_cols].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        heatmap_path = f"{output_prefix}/correlation_heatmap.png"
        plt.title("Correlation Heatmap")
        plt.savefig(heatmap_path)
        plt.close()
        paths["heatmap"] = heatmap_path

    # Boxplots for top 3 numeric columns
    paths["boxplots"] = []
    for column in numeric_cols[:3]:  # Limiting to 3 columns for better visualization
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=data[column], color="skyblue")
        plt.title(f"Boxplot of {column}")
        boxplot_path = f"{output_prefix}/{column}_boxplot.png"
        plt.savefig(boxplot_path)
        plt.close()
        paths["boxplots"].append(boxplot_path)

    # Histograms for top 3 numeric columns
    paths["histograms"] = []
    for column in numeric_cols[:3]:  # Limiting to 3 columns
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True, color="blue")
        plt.title(f"Histogram of {column}")
        hist_path = f"{output_prefix}/{column}_histogram.png"
        plt.savefig(hist_path)
        plt.close()
        paths["histograms"].append(hist_path)

    return paths


def detect_outliers(data, column):
    """Detect outliers in a numeric column using the IQR method."""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    result = f"Detected outliers in '{column}': {len(outliers)} rows"
    print(result)
    outlier_results.append(result)
    return outliers


def feature_importance_analysis(data, target_column):
    """Analyze feature importance using a Random Forest."""
    global feature_importance_results
    numeric_data = data.select_dtypes(include="number").dropna()
    if target_column not in numeric_data.columns:
        print(f"Target column '{target_column}' is not numeric or not available.")
        return None

    X = numeric_data.drop(columns=[target_column])
    y = numeric_data[target_column]
    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)
    importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    print("Feature Importance Analysis:")
    print(importance)
    feature_importance_results = importance
    return importance


# Main script logic
if __name__ == "__main__":
    print(f"Performing analysis for dataset '{dataset_name}'...")

    # Perform basic analysis
    data_summary = basic_analysis(df)

    # Detect outliers in numeric columns
    numeric_cols = df.select_dtypes(include="number").columns
    for column in numeric_cols:
        detect_outliers(df, column)

    # Perform feature importance analysis (example: using the last numeric column as target)
    if len(numeric_cols) > 1:
        target_column = numeric_cols[-1]
        feature_importance_analysis(df, target_column)

    # Generate visualizations
    visualizations = generate_visualizations(df, output_dir)

    # Generate narrative using LLM
    analyses_summary = f"""
    Outlier Detection: {outlier_results}
    Feature Importance: {feature_importance_results.to_dict() if feature_importance_results is not None else "N/A"}
    """
    narrate_analysis(data_summary, analyses_summary)

    # Generate analysis suggestions from LLM
    suggestions = suggest_analysis(data_summary)

    # Write results to README.md
    # Write results to README.md
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# Automated Data Analysis Report for {dataset_name.capitalize()}\n\n")
        f.write(f"## Dataset: {csv_file}\n\n")
        f.write("### Dataset Overview\n")
        f.write(f"- **Columns**: {data_summary['columns']}\n")
        f.write(f"- **Missing Values**: {data_summary['missing_values']}\n\n")
        f.write(story + "\n\n")
        f.write("### Outlier Detection Results\n")
        f.write("\n".join(outlier_results) + "\n\n")
        if feature_importance_results is not None:
            f.write("### Feature Importance Analysis\n")
            f.write(feature_importance_results.to_markdown() + "\n\n")
        if "heatmap" in visualizations:
            f.write("### Correlation Heatmap\n")
            f.write(f"![Correlation Heatmap]({visualizations['heatmap']})\n\n")
        if "boxplots" in visualizations:
            f.write("### Boxplots\n")
            for boxplot_path in visualizations["boxplots"]:
                f.write(f"![Boxplot]({boxplot_path})\n\n")
        if "histograms" in visualizations:
            f.write("### Histograms\n")
            for hist_path in visualizations["histograms"]:
                f.write(f"![Histogram]({hist_path})\n\n")
        f.write("## Suggestions\n\n")
        f.write(suggestions + "\n\n")



    print(f"Analysis completed. Results saved to {readme_path}")
