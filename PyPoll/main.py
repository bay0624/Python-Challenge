"""
A script to run analysis for the PyPoll Data.

A Python script that analyzes a set of polling data called election_data.csv.

This script will analyze the votes and calculate the following:
1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on popular vote.

Author: Abayomi Olujobi
"""
import os
import csv

path = "/Users/abayomi/GitHubs/Python-Challenge/PyPoll/"
election_data = os.path.join(path,"Resources", "election_data.csv")

def formatted(number):
    #Formats large numbers for more readability
    format_number = "{:,}".format(number)
    return format_number

def candidates_list(list1):
    #Returns a list of the unique candidates
    each_candidate = []
    for i in list1:
        if i not in each_candidate:
            each_candidate.append(i)
    return each_candidate

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    vote_count = 0
    candidates = []
    dates = []
    for row in csvreader:
        vote_count += 1
        
        #Converting Candidate column into a list
        candidates.append(row[2])


    print('\nElection Results')
    print(f'-------------------------')
    print(f'Total Votes: {formatted(vote_count)}')
    print(f'-------------------------')

    #Getting the names of candidates
    unique_candidates = candidates_list(candidates)
    print(unique_candidates)
    
    
        


