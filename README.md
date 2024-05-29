# 📊 DashBoard: Sample SuperStore EDA

Welcome to the Sample SuperStore EDA! This repository contains a powerful Streamlit app for exploring and analyzing sales data from a sample superstore dataset. Dive into various visualizations and interactive features to uncover insights on sales trends, regional performance, category-wise sales, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To run this Streamlit app locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/superstore-eda.git
    cd superstore-eda
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Usage

Upload your dataset file (CSV, TXT, XLSX, or XLS) using the file uploader in the app, or use the default dataset provided. You can filter the data by date, region, state, and city. The app will generate various charts and tables to help you analyze the sales data.

## Features

- 📂 **File Uploader:** Upload your own dataset file.
- 📅 **Date Filters:** Filter data by order date.
- 🌍 **Region, State, and City Filters:** Filter data by geographic regions.
- 📊 **Category-wise Sales:** Bar chart showing sales for each product category.
- 🥧 **Region-wise Sales:** Pie chart showing sales distribution across regions.
- 📈 **Time Series Analysis:** Line chart showing sales trends over time.
- 🌳 **Hierarchical View:** Treemap showing sales by region, category, and sub-category.
- 📉 **Segment-wise Sales:** Pie chart showing sales distribution across customer segments.
- 🗂️ **Category-wise Sales:** Pie chart showing sales distribution across product categories.
- 📅 **Month-wise Sub-Category Sales Summary:** Summary table and pivot table of sales by month and sub-category.
- 📉 **Scatter Plot:** Scatter plot showing the relationship between sales and profit.
- 💾 **Download Options:** Download filtered data, category data, region data, time series data, and the original dataset as CSV files.

## File Descriptions

- **app.py:** The main script containing the Streamlit app code.
- **requirements.txt:** List of Python packages required to run the app.
- **Sample - Superstore.csv:** Default dataset used by the app if no file is uploaded.

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was developed using Streamlit and Plotly for interactive visualizations. Special thanks to the creators of the sample superstore dataset.
