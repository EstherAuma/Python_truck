def paye(salary,name):
   rate = 0.3
   if salary >= 300000:
        tax = rate*salary
        net_pay = salary-tax
        print("*********************")
        print("Dear: ",name) 
        print("Your tax payable is: ",tax)
        print("And your take home salary is: ",net_pay)
        print(".....................")        

   else:
       print("Dear: ",name)
       print("Your salary is non-taxable")

print ("You are wellcome! ")    
name = raw_input("Please input your name here: ")
salary = input("Please input your salary here: ")
location = raw_input("Please input your location here: ")
age = input("Please enter your year of birth here: ")
occupation = raw_input("Please enter your occupation here: ")


paye (salary,name)   




def examp():
    my_list = []
    num = input("Please enter your lucky number: ")
    my_list.append(num)
    print(my_list)
    for item in my_list:
        print(item)
     
     
    

examp()