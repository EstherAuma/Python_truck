'''
This code demonstrates the usage of functions.

'''

#The function performs tests on given inputs
def tests(test1, test2):
	
	if test1 == test2:
		#Check if test1 is equal to test2
		return test1
	else:
		#If test1 is not equal to test2, 
        # perform some other actions or return a different value.
		return test2
#This return statement allows the function to pass the value of test2 back to the caller.
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
Asks the user to enter the marks for test one and test two.
The input function is used to capture user input, which is then converted to an integer using the int() function.
The entered marks will be stored in the variables test1 and test2 respectively.
'''


# Perform some operations or actions related to the given cswork.
def courseWrk(cswork):
	
	testsMark = tests(test1,test2)
	#Call the 'tests' function with the arguments 'test1' and 'test2'.
	avgtestsCswork = (cswork + testsMark)/2
	#The sum of 'cswork' and 'testsMark' is divided by 2 to obtain the average.
	fnltestsCswork = avgtestsCswork * (40/100)
	'''
	 Calculate the final combined score for tests and coursework.
     The average score obtained from 'avgtestsCswork' is multiplied by the weighting factor (40%).
     The result represents the final combined score, which takes into account both test and coursework performance.
    '''
	print('..............................')
	'''
	 Print a visual separator or divider consisting of a series of dots.
     This line of code generates a visual representation of a separator to visually separate or divide sections of output or text.
     The specific number of dots and their length can be adjusted as needed.
     '''
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
	'''
     Print the final coursework marks.
     The variable 'fnltestsCswork' holds the calculated combined score for tests and coursework, which represents the final coursework marks.
     The value of 'fnltestsCswork' is displayed along with the descriptive text "your final coursework marks is: ".
     This line provides the user with their coursework performance result.
    '''

cswork = int(input('Please enter your course work Marks: '))
'''
Prompt the user to enter their course work marks.
The input function is used to capture the user's input, which is expected to be the course work marks.
The entered value is converted to an integer using the int() function.
The converted value is then stored in the variable 'cswork' for further processing or calculations.
'''

courseWrk(cswork)
