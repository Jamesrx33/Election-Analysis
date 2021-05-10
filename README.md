# **<p align="center">Election Results Analysis</p>**

### **<p align="center">A Python-based analytics report designed to determine the winner of a local Colorado election.</p>**

---
## Overview
This report will display the results of a local Colorado election, given data provided from the election commission in CSV format. Using Python to iterate through and process each recorded vote, we have determined the victor of this election and outputted the results in a .txt file. Per request, we have also provided voter turnout metrics per county and the county with the largest turnout overall. Should this report meet the expectations of the election commission, it is our desire that this code me implemented in future elections.

---
## Winning Candidate - Diana Degette
1. **Number of Votes:** 272,892
2. **Winning Percentage:** 73.8%

---
## Voting Metrics - [Link to Results File](https://github.com/Jamesrx33/election-analysis/blob/1440b577eeec8f065f3e86996c23e9cee7551b7f/analysis/election_analysis.txt)

1. Total Number of Votes Cast: 369,711
2. County Metrics:
   * **Jefferson:** 38,855 (10.5%)
   * **Denver:** 306,055 (82.8%)
   * **Arapahoe:** 24,801 (6.7%)
3. Largest County Turnout: **Denver** (306,055)
4. Candidate Metrics:
   * **Charles Casper Stockham:** 85,213 (23.0%)
   * **Diana DeGette:** 272,892 (73.8%)
   * **Raymon Anthony Doane:** 11,606 (3.1%)

---
## Summary
This Election-Analysis script was able to process and display the results of nearly 370,000 votes in a matter of seconds. Given the following modifications (and assuming the same CSV raw data format), we can apply this script to any election of our choosing:
* Implement an input box where a user can input the directory of the CSV file.
   - **file_to_load** = input("Please enter the directory path to the CSV data file.")
* Add to our conditional statement to account for a Tie
   - **if (vote_percentage == winning_percentage):**
   
         winning_count = candidateVotes
         winning_candidate = "There was a Tie, a recount is recommended."
         winning_percentage = vote_percentage
     **elif (candidateVotes > winning_count) and (vote_percentage > winning_percentage):**
     
         winning_count = candidateVotes
         winning_candidate = candidate_name
         winning_percentage = vote_percentage


---
## Reference Documentation - [Source Code Repository](https://github.com/Jamesrx33/election-analysis), [Download .zip file](https://github.com/Jamesrx33/election-analysis/archive/refs/heads/main.zip)
