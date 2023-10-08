#-------------------------------------------------------------
#-------------------------------------------------------------
#                     PART 1 - PYBANK
#-------------------------------------------------------------
#-------------------------------------------------------------

import os
import csv

budget_data_csv = os.path.join('PyBank', 'Resources', "budget_data.csv")

#Creating empty lists to store our 2 sets of data in the csv file
months = []
profits_losses = []

#Reads the csv file and adds data into our 2 empty lists
with open(budget_data_csv, 'r') as csvfile_pybank:
       
        csvreader_pybank = csv.reader(csvfile_pybank)

        #Stores the header row
        header = next(csvreader_pybank)

        for row in csvreader_pybank:
              
              months.append(row[0])
              profits_losses.append(row[1])

#Converts the data in the profits and losses list to integers
int_profits_losses = [int(i) for i in profits_losses]


#This comprehensive list was added with the aid of StackOverflow: https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
#Creates a list of the difference between values_pybank
# for the profits and losses
int_changes = [int_profits_losses[i+1] - int_profits_losses[i] for i in range(len(int_profits_losses) - 1)]

#Shows the output_pybank in the format we're looking for
#Extra print("") functions to output_pybank extra spaces. Keeps the data clean, spaced out, and easy to read
print("")
print("Financial Analysis\n")
print("---------------------------\n")


#Prints the Values and their associated Results in the terminal

#Total Months is the length of our months list
print(f'Total Months: {len(months)}\n')

#Total is the sum of all our Profits and Losses
print(f'Total: ${sum(int_profits_losses)}\n')

#Average Change is the sum of all the changes from our profits and losses divided by the amount of changes there are. Rounded to 2 decimal places
print(f'Average Change: ${round((sum(int_changes)) / (len(int_changes)), 2)}\n')

#Greatest Increase in Profits found to be the maximum value in our changes list
#We then find the index of said value in our changes list and match that with the corresponding month in our months list
print(f'Greatest Increase in Profits: {months[int_changes.index(max(int_changes)) + 1]} (${max(int_changes)})\n')

#Greatest Increase in Profits found to be the minimum value in our changes list
#Same process with finding the corresponding month for the minimum value
print(f'Greatest Decrease in Profits: {months[int_changes.index(min(int_changes)) + 1]} (${min(int_changes)})\n')


#Creating the lists we're going to zip together to display in the outputed text file
values_pybank = ["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
results_pybank = [(f'{len(int_profits_losses)}'),
           (f'${sum(int_profits_losses)}'),
           (f'${round((sum(int_changes)) / (len(int_changes)), 2)}'),
           (f'{months[int_changes.index(max(int_changes)) + 1]} (${max(int_changes)})'),
           (f'{months[int_changes.index(min(int_changes)) + 1]} (${min(int_changes)})')]

#Zipping the two lists together
output_pybank = list(zip(values_pybank, results_pybank))


output_text_pybank = os.path.join('PyBank', 'Resources', 'output_pybank.csv')

#Opening our output_pybank text file
with open(output_text_pybank, 'w') as pybank_output:
      
    writer = csv.writer(pybank_output)

    #Creating the header row
    writer.writerow(['Values', 'Results'])

    #Adding the zipped list into rows within the output_pybank file
    writer.writerows(output_pybank)