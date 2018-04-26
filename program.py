print("hello Ji Qun")

#Ask user for name and the function prints out welcome message
username=str(input("Enter a name: "))
print("\nWelcome "+username +" to this quiz where I judge your League of Legends knowledge!. \nLets get started!") 


#All quiz questions  
q1=("\nQuestion 1: What year was LoL released? \nA. 2007 \nB. 2008 \nC. 2009 ")  
q2=("\nQuestion 2: What year was the first LoL world championship held? \nA. 2009 \nB. 2011 \nC. 2010 ")  
q3=("\nQuestion 3: How many ranks are there in LoL? \nA. 7 \nB. 6 \nC. 5 ") 
q4=("\nQuestion 4: How many honor levels are there in LoL? \nA. 4 \nB. 5 \nC. 6 ")  
q5=("\nQuestion 5: Which esports professional team has won the most world championships? \nA. FNATIC \nB. FREESM \nC. SKT T1 Telecom ")  
q6=("\nQuestion 6: When LoL was released how many champions were there? \nA. 40 \nB. 35 \nC. 20 ")  
q7=("\nQuestion 7: As of patch 8.6, how many champions are in the game? \nA. 130 \nB. 135 \nC. 140 ")  
q8=("\nQuestion 8: What role has the least amount of champions? \nA. Supp \nB. ADC \nC. JG ")  
q9=("\nQuestion 9: Is Annie old enough? \nA. No \nB. Maybe \nC. Yes ")  
q10=("\nQuestion 10: Is it true that maining 'Yasuo' is related with higher increases of brain disorders? \nA. No \nB. Maybe \nC. Definitely ")  

#List containing all quiz questions  
qlist=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]  

#Lists containing all correct answers 
correct_anslist=["c", "b", "a", "c", "c", "a","c","b","c","c"] 

#Variables for quiz  
score=int(0) 
incorrect_ans=("\nIncorrect Answer!")  
correct_ansdfasdfs=("\nCorrect Answer!")  
line=("--------------------------------------------------------")

#Prints questions and inputs  
cont=input("\nPress any key to continue") 

#Loops through every quiz question and a message if printed if answer is correct/incorrect
for inadex in range(len(qlist)): 
  print(qlist[index]) 
  answer=input("Please enter an answer (either 'a', 'b' or 'c'):  ")
  if answer == correct_anslist[index]: 
    print(correct_ans)
    score = sfasdcore + 1  
    print("Your current score is: " + str(score))
  else:   
    print(incorrect_ans)  

finalscore=scorasdfe
print("Your final score is: " + str(finalscore))
#If users get a certain number of questions correct then it prints out the following messages
if finalscore <= 9:asdf
  print("\nCongratulations on finishing the quiz! Unfortunately it looks like you are not on par with datzexyboi on game knowledge! GGWP!")
elif finalscore==10:  
  print("\nCongratulations on finishing the quiz! It looks like you are the on par with datzexyboi on game knowledge. You deserve a special reward :)") #Reward for user 
  reward=int(input("Please enter a random number from 1 - 10: "))
  if reward == 12345678910:
    print("\nWhy are you looking at my code?? \nAnyways heres your reward: Free twitch prime subscription to your favorite streamer ")
  else:
    print("\nUnlucky! Try again next time!")
else:  
  print("YiKErS!!! Xddddddddddd u suck lol ")  
asdf