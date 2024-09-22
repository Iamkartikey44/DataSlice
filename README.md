# DataSlice

---
![image](https://github.com/user-attachments/assets/dfc2d258-6233-4916-bd54-1ab67c6dacc7)

# Sampling Techniques Explorer with Visualizations 📊

Welcome to the **Sampling Techniques Explorer**, an interactive web application built with **Streamlit** that allows users to explore and visualize various sampling techniques on their dataset. This project includes advanced visualizations and statistical comparisons to understand how sampling affects the data distribution.

## Features

- **Upload Dataset**: Users can upload their dataset in CSV or Excel format.
- **Sampling Techniques**:
  - **Random Sampling**: Selects a random sample from the dataset.
  - **Stratified Sampling**: Samples based on a categorical column.
  - **Cluster Sampling**: Samples based on specific clusters of data.
  - **Systematic Sampling**: Selects every k-th record from the dataset.
  - **Reservoir Sampling**: (Note: This method is more suitable for streaming data, thus only informative here).
  - **Importance Sampling**: Samples based on the importance (weights) of a numeric column.
- **Visualizations**:
  - **Box Plot**
  - **Violin Plot**
  - **KDE Plot (Kernel Density Estimate)**
- **Comparative Statistics**:
  - Mean and Standard Deviation of both original and sampled data.
- **Data Export**: Download the sampled dataset in CSV format.

## How to Run the Application

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sampling-techniques-explorer.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

4. Open your browser at `http://localhost:8501` to access the app.

## Dependencies

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- Streamlit

Install all the necessary libraries using:
```bash
pip install -r requirements.txt
```

## Usage

1. **Upload your dataset**: The application accepts CSV and Excel files.
2. **Select Sampling Technique**: Choose from the provided sampling methods.
3. **Visualize the Data**: View different visualizations like box plots, violin plots, and KDE plots for sampled data.
4. **Compare Statistics**: Compare the mean and standard deviation of the original dataset vs. the sampled dataset.
5. **Download Sampled Data**: Export your sampled data to a CSV file for further use.

## Screenshots

| Feature                      | Screenshot |
|------------------------------|------------|
| Data Upload & Summary         | ![Upload Preview](![image](https://github.com/user-attachments/assets/2bbde1e2-82e4-4b0d-ab19-d0fff64e5ebb) |
| Sampling Technique Selection  | ![Sampling Selection] (https://github.com/user-attachments/assets/f6de3221-bbf2-4a3b-8601-cc1a318d4029)) |
| Sampled Data Visualization    | ![Box Plot Example] (https://github.com/user-attachments/assets/498f3bcd-95f5-466f-a645-647fe6054eb7)) |



