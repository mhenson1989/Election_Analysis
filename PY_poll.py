# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and Print the header row

    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file

# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode, we will write data to the file

    # open(file_to_save, "w")

# Use the with statement to open the file as a text file

# Write some data to the file

# To do: read and analyze the data here



# To do: perform analysis
   
# Print the file object
# for row in file_reader:
    # print(row) 
    

# Close the file



# Steps to Edit Election_Analysis.txt file
# Create a filename variable to a direct or indirect path to the file.

#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the with open statement to open the file as a text file.

# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Counties in the Election\n-------------\nArapahoe\nDenver\nJefferson")
