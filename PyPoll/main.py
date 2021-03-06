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

# path = "/Users/abayomi/GitHubs/Python-Challenge/PyPoll/"
# election_data = os.path.join(path,"Resources", "election_data.csv")
election_data = os.path.join("Resources", "election_data.csv")

def formatted(number):
    #Formats large numbers for more readability
    format_number = "{:,}".format(number)
    return format_number

def vote_percentage(nums):
    #Calculates and formats percentage of vote
    percent = nums/vote_count
    percent = "{:.3%}".format(percent)
    return percent

# Function not necessary for solution
# def candidates_list(list1): 
#     #Returns a list of the unique candidates 
#     each_candidate = []
#     for i in list1:
#         if i not in each_candidate:
#             each_candidate.append(i)
#     return each_candidate

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    vote_count = 0
    candidates = []

    for row in csvreader:
        vote_count += 1
        
        #Converting Candidate column into a list
        candidates.append(row[2])

    print('\nElection Results')
    print('-------------------------')
    print(f'Total Votes: {formatted(vote_count)}')
    print('-------------------------')

    # Getting the unique candidates (Not necessary)
    # unique_candidates = candidates_list(candidates)

    # Creates a list of tuples for each unique occurrence
    # List Comprehension: Tuples will each have 2 elements (candidate name and number of votes)
    counter = [(i, candidates.count(i)) for i in set(candidates)]

    # Traditional for-loop for the list comprehension above
    # counter = []
    # for i in set(candidates):
    #     counter.append((i, candidates.count(i)))

    for i in counter:
        candidate_name = i[0]
        num_of_votes = i[1]

        print(f'{candidate_name}: {vote_percentage(num_of_votes)} ({formatted(num_of_votes)})')

    #Loops through the counter list and creates another list containing only the number of votes
    highest_votes = []
    for j in counter:
        highest_votes.append(j[1])
        highest_votes.sort()

        # List comprehension to check the highest number of votes in the counter list and to output its corresponding element  
        # winner = [k for k in counter if k[1] == highest_votes[-1]]

        # Traditional for-loop below is the same as list comprehension above (name_winner will be winner[0][0]) instead
        winner = []
        for k in counter:
            if k[1] == highest_votes[-1]:
                winner.append(k[0])

        name_winner = winner[0]

    print('-------------------------')
    print(f'Winner: {name_winner}')
    print('-------------------------')

    #Export a text file with the results
    
    # path2 = "/Users/abayomi/GitHubs/Python-Challenge/PyPoll/Analysis/"
    # file_name = 'analysis.txt'
    # complete_name = os.path.join(path2,file_name)

    complete_name = os.path.join('Analysis','analysis.txt')

    f = open(complete_name, 'w')
    f.write('\nElection Results\n')
    f.write('-------------------------\n')
    f.write(f'Total Votes: {formatted(vote_count)}\n')
    f.write('-------------------------\n')
    for i in counter:
        candidate_name = i[0]
        num_of_votes = i[1]
        f.write(f'{candidate_name}: {vote_percentage(num_of_votes)} ({formatted(num_of_votes)})\n')
    f.write('-------------------------\n')
    f.write(f'Winner: {name_winner}\n')
    f.write('-------------------------')

    f.close()