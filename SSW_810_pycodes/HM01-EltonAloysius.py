import random

print(" Rock \n Paper \n Scizzors \n")
user = input()

a = ['Rock','Paper','Scizzors']
comp = random.choice(a)             #Used Random String generator from the List.
print(comp)

if(user == 'Rock' and comp == 'Scizzors' or user == 'Paper' and comp == 'Rock' or user == 'Scizzors' and comp == 'Paper'):
      print("User wins")

elif(user == 'Scizzors' and comp == 'Rock' or user == 'Rock' and comp == 'Paper' or  user == 'Paper' and comp == 'Scizzors'):
       print("Comp wins")      

else: 
       print("Its a Draw")       