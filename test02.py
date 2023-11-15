import pandas
import graphing

# Read the text file containing data using pandas
dataset = pandas.read_csv('doggy-boot-harness.csv')

# Print how many rows of data we have
#print(f"We have {len(dataset)} rows of data")

# Determine whether each avalanche dog's harness size is < 55
# This creates a True or False value for each row where True means 
# they are smaller than 55
is_small = dataset.harness_size < 55
#print("\nWhether the dog's harness was smaller than size 55:")
#print(is_small)

# Now apply this 'mask' to our data to keep the smaller dogs
data_from_small_dogs = dataset[is_small]
#print("\nData for dogs with harness smaller than size 55:")
#print(data_from_small_dogs)

# Print the number of small dogs
#print(f"\nNumber of dogs with harness size less than 55: {len(data_from_small_dogs)}")

data_smaller_paws = dataset[dataset.boot_size < 40].copy()

#print(f"we now have {len(data_smaller_paws)} rows in our data set. The last few rows are:")
#print(data_smaller_paws.tail())

# Load and prepare plotly to create our graphs
import plotly.express
import graphing # This is a custom file you can find in our code on github

# Show a graph of harness size by boot size
plotly.express.scatter(data_smaller_paws, x="harness_size", y="boot_size")

# Convert harness sizes from metric to imperial units 
# and save the result to a new column
data_smaller_paws['harness_size_imperial'] = data_smaller_paws.harness_size / 2.54

# Show a graph of harness size in imperial units
plotly.express.scatter(data_smaller_paws, x="harness_size_imperial", y="boot_size")
