#Sequencing----- converting celcius to kelvin
celcius = int(input("Please enter the tempurature in celcius "))
kelvin = celcius + 273.15
print("The tempurature in kelvin is ", kelvin ,"K")

#Selection------- checking to see if you are Mrat
name = input("Please Enter your name: ")
name_i_dont_like = "Mrat"
if name == name_i_dont_like:
    print("Bugger off Mrat")
else:
    print("Nice name pal")
        
#Iteration------ tracking process of cleaning wheels
number_of_wheels = int(input("How many wheels are we cleaning?: ")) #This line of code asks for an input value from the user, however it must be an integer value. The value is then assigned to the variable number_of_wheels

number_of_wheels_cleaned = 0 #This is a variable

soap_on_sponge = True #This is a boolean

while soap_on_sponge == True: #This means to exectute the code underneath for while soap_on_sponge = true
    while number_of_wheels_cleaned < number_of_wheels: #This means to execute the code while number_of_wheels_cleaned is less than number_of_wheels
        number_of_wheels_cleaned = number_of_wheels_cleaned + 1 #This means to then add 1 to the value of number_of_wheels
        print(number_of_wheels_cleaned) 
        soap_on_sponge = False
    print("Wheels cleaned")
-----------------------------------------------------------------------------------
aiden = "HURURURURURURURU CHESH HURURURURURU" #This variable is global and can be used in any function
def functionOne(): #This is a function being called
  whostoesarethose = "OO OO AA AA" #This is a local variable, it only exists inside functionOne
  print(whostoesarethose) #This prints the variable
functionOne() #This calls the function so it will do something

def functionTwo(x,y): #This function takes 2 different arguments, x and y
  print(str(x + y)) #This prints x+y
  return x+y #This tells the program to return any relevent information to the function

x = int(input("Enter number: ")) #These 2 inputs assign values to x and y
y = int(input("Enter second number: "))
functionTwo(x,y) #This calls the function functionTwo