"# Streamlit-Task1"
1)--Data Sweeper--
Data Sweeper is a user-friendly web application built using Streamlit that allows users to seamlessly transform their data files between CSV and Excel formats. The tool comes with built-in data cleaning and visualization features, making it perfect for quick analysis and cleaning of datasets.
**Features**
-File Upload: Upload multiple CSV or Excel files for processing.
-Data Cleaning:
-Remove Duplicates: Automatically remove duplicate rows from your dataset.
-Fill Missing Values: Fill missing numeric values with the mean of the column.
-Data Preview: View a preview of the first five rows of your data.
-Column Selection: Choose specific columns to keep or convert before processing the file.
-Data Visualization: Generate a simple bar chart of the first two numeric columns to quickly visualize data distribution.
-File Conversion:
-Convert your processed dataset between CSV and Excel formats.
-Download the transformed files directly from the app.
**Technologies Used**
-Streamlit: For creating the interactive web interface.
-Pandas: For data manipulation and processing.
-Python: The underlying programming language for building the application.
**Future Enhancements**
-Support for additional data cleaning operations (e.g., remove outliers, standardize text).
-More advanced visualizations like scatter plots, histograms, etc.
-Support for more file formats (e.g., JSON, Parquet).

2)--Unit Converter--
The Universal Unit Converter is a simple and interactive web app built using Streamlit. It allows users to perform a wide range of unit conversions, including length, weight, temperature, speed, time, volume, area, and currency. The app provides a user-friendly interface that helps you easily convert values between various units of measurement or currencies with real-time exchange rates.
**Features**
-Convert between multiple types of units including:
-Length: meter, kilometer, mile, yard, foot, inch, centimeter
-Weight: gram, kilogram, pound, ounce, ton
-Temperature: Celsius, Fahrenheit, Kelvin
-Speed: meter per second, kilometer per hour, mile per hour, knot
-Time: second, minute, hour, day, week, month, year
-Volume: liter, milliliter, gallon, cubic meter, cubic foot
-Area: square meter, square kilometer, square mile, hectare, acre
**Currency Conversion**
-Convert between currencies with real-time exchange rates using the Forex Python API.
-Currently supports any two currencies (e.g., USD to EUR, GBP to INR, etc.).
**Technologies Used**
-Streamlit: A powerful framework for building interactive web apps.
-Pint: A Python package to handle unit conversions (e.g., meter to kilometer).
-Forex Python: A library for retrieving real-time currency exchange rates.
-Python: Backend logic is written in Python to handle the unit and currency conversions.
