# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has provided the following tasks to complete the election audit of a recent local congressional election. The purpose of this project is to conduct an audit and report on the following metrics below:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Summary
### Election Audit Results

![Election_Results](https://github.com/mhenson1989/Election_Analysis/blob/main/Resources/Election_Results.PNG)

The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candiate results were: 
    - Charles Casper Stockham received 23% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes. 
- The county with the largest turnout of votes was Denver County with 306,055 votes, which compiled 82.8% of the total votes cast.
- The winner of the election was:
    - Diane DeGette who recieved 73.8% of the vote and 272,892 votes.

### Election Audit Summary
The Election Aduit Analysis script provides an efficient template script to run analysis for election campaigns when tallying counts of votes, percentage of votes tallied within voting counties and for candidates. This code would be effective for larger sets of data as well, with additional counties, votes and candidates. In order to streamline this script to scale or be modified for other elections, however, one could consider refactoring the code in the following ways: 

    - Manually Define a Dictionary or Array of Counties and Candidates
        - Ex: county_list = ["Harris County", "Waller County", "Brazoria County"] and candidate_list = ["John Smith", "Pocahontas", "Meeko"]
    - Consolidate the For Loops and Conditionals
        - Combine the county results for county percentages, candidate breakdown and winner into one summary print statement, instead of breaking the conditionals into seperate print statements. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1
