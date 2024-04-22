# Project 4 Group 5

## README

### Introduction
This repository contains SQL scripts and Python code to import, analyze, and model American Housing Survey (AHS) data. The data is sourced from the [U.S. Census Bureau's AHS Table Creator](https://www.census.gov/programs-surveys/ahs/data/interactive/ahstablecreator.html), focusing on the years 2011 to 2021.

### Setup
To replicate the analysis, follow these steps:

1. Navigate to the [AHS Table Creator](https://www.census.gov/programs-surveys/ahs/data/interactive/ahstablecreator.html).
2. Choose the year 2021 and select the "General Housing" table.
3. Specify the variables and filters as outlined below:

   - Variables:
     - Homeownership
     - Income
     - Age
     - Total

   - Filters:
     - By Group 1: Homeownership
     - By Group 2: Income

4. Export the data and save it as a CSV file.

### SQL Scripts
Use the following SQL scripts to create tables and import datasets:

```sql
-- Create tables
CREATE TABLE homeownership (
    homeownership VARCHAR(10),
    income VARCHAR(20),
    age VARCHAR(20),
    total INT,
    year INT
);

CREATE TABLE owner (
    homeownership VARCHAR(10),
    income VARCHAR(20),
    age VARCHAR(20),
    total INT,
    year INT
);

CREATE TABLE renter (
    homeownership VARCHAR(10),
    income VARCHAR(20),
    age VARCHAR(20),
    total INT,
    year INT
);

-- Import datasets into tables
-- You need to load the data from the CSV file into these tables

### Perform the following calculations using SQL queries:

-- Calculate the percentage of homeownership by income group for a specific year:

-- Calculate the total number of homeowners by age group for a specific year:

-- Calculate the percentage of homeownership by age group for a specific year:

-- Calculate the change in the total number of homeowners from one year to the next:

### Data Modeling

To create a predictive model for homeownership using the AHS data, follow these steps:

1. **Data Preprocessing:**
   - Load the dataset from the provided CSV file.
   - Perform any necessary data cleaning and preprocessing steps, such as encoding categorical variables and handling missing values.

2. **Feature Engineering:**
   - Extract relevant features from the dataset that can contribute to predicting homeownership, such as income, age, and interactions between them.
   - Create new features if needed to enhance the predictive power of the model.

3. **Splitting the Data:**
   - Divide the dataset into training and testing sets using a suitable split ratio (e.g., 80% for training and 20% for testing).
   - Ensure that the split maintains the representativeness of the data across different classes of homeownership.

4. **Model Selection:**
   - Choose an appropriate machine learning algorithm for the predictive modeling task. In this case, a RandomForestClassifier is recommended due to its ability to handle both numerical and categorical features, as well as its capability to capture complex relationships in the data.

5. **Model Training:**
   - Train the selected model using the training dataset.
   - Tune the hyperparameters of the model to optimize its performance. This can be done using techniques like grid search with cross-validation.

6. **Model Evaluation:**
   - Assess the performance of the trained model using the testing dataset.
   - Evaluate the model's accuracy and other relevant metrics such as precision, recall, and F1-score.
   - Ensure that the model generalizes well to unseen data and does not overfit the training set.

7. **Interpretation and Validation:**
   - Interpret the results of the model to understand the factors that influence homeownership.
   - Validate the model's predictions against real-world observations and domain knowledge.
   - Iterate on the modeling process if necessary to improve the model's performance or address any shortcomings.

By following these steps, you can develop a reliable predictive model for homeownership using the AHS data, which can provide valuable insights for various stakeholders in the housing sector.
