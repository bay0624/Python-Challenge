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

def vote_percentage(nums):
    #Calculates and formats percentage of vote
    percent = nums/vote_count
    percent = "{:.3%}".format(percent)
    return percent

def candidates_list(list1): #Function not needed for solution
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
    #voters = []
    for row in csvreader:
        vote_count += 1
        
        #Converting Candidate column into a list
        candidates.append(row[2])

    print('\nElection Results')
    print('-------------------------')
    print(f'Total Votes: {formatted(vote_count)}')
    print('-------------------------')

    #Getting the unique candidates (Not necessary)
    unique_candidates = candidates_list(candidates)
    # print(candidates.count(unique_candidates[0]))

    #Creates a list of tuples for each unique occurrence
    counter = [(i, candidates.count(i)) for i in set(candidates)]

    for i in counter:
        candidate_name = i[0]
        num_of_votes = i[1]

        print(f'{candidate_name}: {vote_percentage(num_of_votes)} {formatted(num_of_votes)}')

    highest_votes = []
    for j in counter:
        highest_votes.append(j[1])
        highest_votes.sort()
        winner = [k for k in counter if k[1] == highest_votes[-1]]
        name_winner = winner[0][0]
        
    # print(highest_votes)
    # print(winner)

    print('-------------------------')
    print(f'Winner: {name_winner}')
    print('-------------------------')