'''
This defines a function called tests.
It takes two parameters, test1 and test2.

'''

#The function performs tests on given inputs
def tests(test1, test2):
	#Check if test1 is equal to test2
	if test1 == test2:
		
		#If test1 is not equal to test2, 
        # perform some other actions or return a different value.
		return test1
	else:
		#This return statement allows the function to pass the value of test2 back to the caller.
		return test2
	#Asks the user to enter the marks for test one and test two.	
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))


"""
It defines a function called courseWork.
It takes in a parameter 'cswork' which represents the specific coursework.
"""

def courseWrk(cswork):

	#Call the 'tests' function with the arguments 'test1' and 'test2'.
	testsMark = tests(test1,test2)
	#The sum of 'cswork' and 'testsMark' is divided by 2 to obtain the average.
	avgtestsCswork = (cswork + testsMark)/2
	#Calculate the final combined score for tests and coursework.
	fnltestsCswork = avgtestsCswork * (40/100)
	
     #Print a visual separator or divider consisting of a series of dots.
	print('..............................')
	
      #Print the final coursework marks.
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
	
   #Request the user to enter their course work marks.  
cswork = int(input('Please enter your course work Marks: '))
#calls the function courseWork.
courseWrk(cswork)



"""
This function calculates the final coursework marks. 
based on the given coursework marks and the average of test scores. 
The calculated final coursework marks are printed as output.
"""