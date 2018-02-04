import csv, random, datetime, os

#List of Names
PLAYERS = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9', 'name10']

SCORES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def write_to_csv():
  #Initial Randomization of both lists
  random.shuffle(PLAYERS)
  random.shuffle(SCORES)
  counter=0
  with open('SuperBowl.csv', 'wb') as superbowl:
    wr = csv.writer(superbowl)
    #handles the top row of scores and attaches and empty space to the beginning
    top = [''] + SCORES   
    wr.writerow(top)
    #shuffles Scores again
    random.shuffle(SCORES) 
    
    for row in SCORES:
      #assign new list of Players to names list
      names = PLAYERS
      #adds the far left column of random numbers to the column 0
      names.insert(0, SCORES[counter])
      wr.writerow(names)
      #Removes the addition of the far left column
      names.pop(0)
      counter+=1
      #shuffles everything again
      random.shuffle(PLAYERS)
    #close file
    superbowl.close()
    
if __name__=='__main__':
  write_to_csv()
