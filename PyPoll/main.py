#-------------------------------------------------------------
#-------------------------------------------------------------
#                     PART 2 - PYPOLL
#-------------------------------------------------------------
#-------------------------------------------------------------

import os
import csv

election_data_csv = os.path.join('Resources', "election_data.csv")

#Empty lists to store our data from the csv file
voter_id = []
county = []
candidate = []

#Appending empty lists with csv data
with open(election_data_csv, 'r') as csvfile_pypoll:
       
        csvreader_pypoll = csv.reader(csvfile_pypoll)

        #Stores the header row
        header = next(csvreader_pypoll)

        for row in csvreader_pypoll:
              
              voter_id.append(row[0])
              county.append(row[1])
              candidate.append(row[2])

#List to display all the candidates as we go through the data and to assign each ballot
ballot_count = [0, 0, 0]
candidate_list = []

#Goes through each candidate within the candidate section
for i in candidate:

    #Adds unique candidates into candidate list
    if i not in candidate_list:
        
        
        candidate_list.append(i)

    #Finds the index of each respective candidate
    candidate_index = candidate_list.index(i)

    #Adds a vote to the candidate with said index number
    ballot_count[candidate_index] += 1


#Displays the results in the desired format. Extra Print('') statement to separate result from previous terminal outputs
print('')
print('Election Results\n')
print('---------------------------\n')

#Amount of votes is the length of our voter list as each casted a vote
print(f'Total Votes: {len(voter_id)}\n')
print('---------------------------\n')

#Displays each candidate per their index number as well as the percent of votes they received and the total number of votes
print(f'{candidate_list[0]}: {round(((ballot_count[0] / (len(voter_id)))*100), 3)}% ({ballot_count[0]})\n') 
print(f'{candidate_list[1]}: {round(((ballot_count[1] / (len(voter_id)))*100), 3)}% ({ballot_count[1]})\n')
print(f'{candidate_list[2]}: {round(((ballot_count[2] / (len(voter_id)))*100), 3)}% ({ballot_count[2]})\n')
print('---------------------------\n')

#Determines the winner according to the highest vote count
print(f'Winner: {candidate_list[ballot_count.index(max(ballot_count))]}\n')
print('---------------------------\n')

#Contains the values info for our csv output including the candidate names
values_pypoll = ['Total Results', 
                 (f'Percentage of votes for {candidate_list[0]}'),
                 (f'Percentage of votes for {candidate_list[1]}'), 
                 (f'Percentage of votes for {candidate_list[2]}'), 
                 'Winner']

#Contains the results info for our csv output including pecent of votes and number of votes 
results_pypoll = [(f'{len(voter_id)}'),
                  (f'{round(((ballot_count[0] / (len(voter_id)))*100), 3)}% ({ballot_count[0]})'),
                  (f'{round(((ballot_count[1] / (len(voter_id)))*100), 3)}% ({ballot_count[1]})'),
                  (f'{round(((ballot_count[2] / (len(voter_id)))*100), 3)}% ({ballot_count[2]})'),
                  (f'{candidate_list[ballot_count.index(max(ballot_count))]}')]

#Zips the two together to be used as our csv file output
output_pypoll = list(zip(values_pypoll, results_pypoll))


output_text_pypoll = os.path.join('Resources', 'output_pypoll.csv')

#Opening our output text file and writing our data to it
with open(output_text_pypoll, 'w') as pypoll_output:
    
    writer = csv.writer(pypoll_output)

    #Creating the header row
    writer.writerow(['Values', 'Results'])

    #Adding the zipped list into rows within the output file
    writer.writerows(output_pypoll)