# NY-Property-Sale

## Project description

The purpose of this project is to aggregate, describe and analyze phenomena found in the real estate market in New York City.

## Link to the visualizations

Deploying to heroku.
[New York City Property Sales](https://nyc-property-sales.herokuapp.com/)

## Tools Used

1. Python (Data Aggregation)
* Jupyter Notebook and Pandas

2. Tableau (Visualization and Analysis)

3. Heroku (Publishing of Results and Analysis)

## Steps

1. Use Python to aggregate data from NYC Open Data page. Files from 2016 until the end of June 2020.

 * The CSV files in the data_original folder were uploaded to Pandas Pandas DataFrames
 * The files had some different columns so dropped them and made the files had the same columns for all the CSV files and exported to the Combined folder in
  the data folder.
 * Combined the files and saved CombinedData to the data folder
 * Uploaded the CombinedData and dropped some columns that had fewer data than other fields and dropped duplicate values and saved as FinalCombinedData in the 
  data folder

2. Use of Tableau to describe and analyze the NYC residential property sales' phenomena and trends from the data by creating visualizations and dashboards 

* Filtered data with dwellings, apartments, and condominiums to analyze for residential properties
* Created propery type group using buiding class number
* Used set function to show only dwellings, apartments and condomiums
* Used action for map chart to show median sold price trend by property type for each area

### Tableau Dashboards

1) Area chart and the mark for the highest point
![NYC](img/DynamicsSeason.png)

2) Line chart to show median sold price by property type
![NYC](img/MedianSalesPrices.png)

3) Bar chart 
![NYC](img/MarketBreakdown.png)
![NYC](img/LuxuryProperty.png)

4) Pie chart
![NYC](img/EraPie.png)

5) Map and area chat with action
![NYC](img/NYMap.png)






