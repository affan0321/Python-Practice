import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists:
                with open(database) as fs:
                    data = json.loads(fs.read())
        else:
            print("No such data exists")             
                
    except Exception as err:
         print(f"An error occured as {err}") 

    @classmethod
    def __Update(cls):
         with open(cls.database,'w') as fs:
              fs.write(json.dumps(cls.data))              

    @classmethod
    def __accountGenerate(cls):
         alpha = random.choices(string.ascii_letters,k = 3)
         num = random.choices(string.digits,k = 3)
         spchr = random.choices("!@#$%^&*", k = 1)
         id = alpha + num + spchr
         random.shuffle(id)
         return "".join(id)

    def CreateAccount(self):
         info = {
              "name" : input("Tell your name : "),
              "age" : int(input("Tell your age :")),
              "email": input("Tell your email : "),
              "pin" : int(input("Tell your 4 digit pin : ")),
              "accountNo" : Bank.__accountGenerate(),
              "balance" : 0
         }
         if info['age'] < 18 and len(str(info['pin'])) != 4:
              print("Sorry you cannot create account")
         else:
              print("Your account has been created successfully!")
              for i in info:
                   print(f"{i} : {info[i]}")
              print("Please note down your account details.")
              Bank.data.append(info) 
              Bank.__Update()    


    def DepositMoney(self):
         accNo = input("Enter your account number : ")
         pin = int(input("Enter your pin"))

         userData = [i for i in Bank.data if i['accountNo'] == accNo and i['pin'] == pin ]   
         if userData == False:
              print("Sorry! no data found")
         else:
              amount = int(input("Enter the amount you want to deposit"))
              if amount > 10000 or amount < 0:
                   print("Amount should be less than 10000 and amount should be positive")
              else:
                   print(userData)
                   userData[0]['balance'] += amount 
                   Bank.__Update()
                   print("Amount deposited successfully!")        
                     
        

user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositting the amount of money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response : "))

if check == 1:
    user.CreateAccount()
if check == 2:
     user.DepositMoney()    