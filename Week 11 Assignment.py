l = [1121, "Jackie Grainger", 22.22,    



 1122, "Jignesh Thrakkar", 25.25,



 1127, "Dion Green", 28.75, False,



 24.32, 1132, "Jacob Gerber",



 "Sarah Sanderson", 23.45, 1137, True,



 "Brandon Heck", 1138, 25.84, True,



 1152, "David Toma", 22.65,



 23.75, 1157, "Charles King", False,



 "Jackie Grainger", 1121, 22.22, False,



 22.65, 1152, "David Toma"]  #Original Unsorted List





employee_num = [] #List for Employee Numbers

employee_name = [] #List for Employee Names

employee_wage = [] #List for Employee Hourly Wage



for i in l: #For sorting the list

	if isinstance(i,bool): #skip to the next iteration if the variable is a boolean

		continue

	elif isinstance(i,int): #append to the Employee Numbers list if variable is integer

		employee_num.append(i)

	elif isinstance(i,str): #append to the Employee Names list if variable is a string

		employee_name.append(i)

	elif isinstance(i,float): #append to the Employee Hourly Wage list if variable a float/decimal

		employee_wage.append(i)





print("Employee Info: ",employee_num)

print("Employee Wage: ",employee_wage)

print("Employee Name: ",employee_name)



print("-----------------------------------------------------------------------------------------------------------------------")



total_hourly_rate = [] # List for the Total Hourly Rate



for i in employee_wage: #iterate over the Employee Hourly Wage list 

	total_hourly_rate.append(1.3*i) #multiply var by 1.3 and append to the Total HourlyRate list



print("Total Hourly Rate: ", total_hourly_rate)





# Program to find largest 

# number in a list 

# initially and assign it to variable "max" 

maxnum = total_hourly_rate[0] 

for x in total_hourly_rate: #traverse through the list and compare each value with max

	if x > maxnum: #everytime x is larger than the maxnum variable renew the maxnum variable with x

		maxnum = x

  

print("Maximum Value in Total Hourly Rate: ", maxnum) #use the max method for determining the meximum method 



if max(total_hourly_rate) > 37.30: #simple conditional statement

	print("[!]WARNING. There is a budget concern!")



underpaid_salaries = []



for i in total_hourly_rate:

	if i > 28.16 and i < 30.65: #simple conditional statement

		underpaid_salaries.append(i)



print("Underpaid Salaries", underpaid_salaries)



company_raises = []



for i in range(0,len(total_hourly_rate)):

	# Using the conditional expressions in python

	# If the hourly rate is between 22 and 24 dollars per hour, raise the current value to 5% by adding the curremt value to the itself multiplied by 0.05

	if 22 < total_hourly_rate[i] < 24: 

		total_hourly_rate[i] = total_hourly_rate[i] + (total_hourly_rate[i]*0.05)

		company_raises.append(total_hourly_rate[i])

	# If the hourly rate is between 24 and 26 dollars per hour, raise the current value to 4% by adding the curremt value to the itself multiplied by 0.04

	elif 24 < total_hourly_rate[i] < 26:

		total_hourly_rate[i] = total_hourly_rate[i] + (total_hourly_rate[i]*0.04)

		company_raises.append(total_hourly_rate[i])

	# If the hourly rate is between 26 and 28 dollars per hour, raise the current value to 3% by adding the curremt value to the itself multiplied by 0.03

	elif 26 < total_hourly_rate[i] < 28:

		total_hourly_rate[i] = total_hourly_rate[i] + (total_hourly_rate[i]*0.03)

		company_raises.append(total_hourly_rate[i])

	# For the other salary values, raise the current value to 2% by adding the curremt value to the itself multiplied by 0.02

	else:

		total_hourly_rate[i] = total_hourly_rate[i] + (total_hourly_rate[i]*0.02)

		company_raises.append(total_hourly_rate[i])





print("Raised Total Hourly Rate: ", total_hourly_rate)

print("company_raises: ", company_raises)