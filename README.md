# NY-Property-Sale

## Project description

The purpose of this project is to aggregate, describe and analyze phenomena found in the real estate market in New York City.

## Link to the visualizations

Deploying to heroku.
[New York City Property Sales](https://nyc-property-sales.herokuapp.com/)

## Tools Used

1. Python (Data Aggregation)
  - Jupyter Notebook and Pandas

2. Tableau (Visualization and Analysis)

3. Heroku (Publishing of Results and Analysis)

## Steps

1. Use Python to aggregate data from NYC Open Data page. Files from 2016 until the end of June 2020.

  - The CSV files in the data_original folder were uploaded to Pandas Pandas DataFrames
  - The headers of the Pandas DataFrames were changed to be the same for all the CSV files
  - The Pandas DataFrames with the standardized headers were exported to the data_modified folder
  - The CSV files in the modified folder were uploaded to a single Pandas DataFrame

2. Elimination of outliers by using Python.
 
  - The Pandas DataFrame containing the data of all the months was filtered to eliminate the outliers
  - Small CombinedData CSV files, the product of the aggregation, were exported to the data_output folder

3. Use of Tableau to describe and analyze the phenomena from the data by creating visualizations and dashboards







