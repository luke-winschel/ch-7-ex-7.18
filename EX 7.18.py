#Median and Mode of an array.  Write functions to determine the median and mode of the values in an array.
import numpy as np

#Define Median Function
def median (arr):
    counter = 0
    #For loop that adds up all the values of the array
    for i in range (len(arr)):
        counter += arr[i]
        #Divides the total of all values and divides by the number of items in the arry
    counter = counter/len(arr)
    #Prints the output of the Median
    print ("The median of the numbers entered is: ", counter)
    
#Define mode function
def mode (arr):
  #Sets conditional if the two arrays are the same length after using the set() function
  if len(arr) == len(set(arr)):
      print("There are no duplicate numbers, therefore the mode is all numbers!")
  else:
    print ("The mode of the numbers entered is: ",max(set(arr), key = arr.count))

#Create empty array
arr = []

#For loop that gets input from the user and fills the array
for i in range (0,5):
    number = int(input("Please enter a number: "))
    arr.append(number)

#Calls the two functions after filling the array
median(arr)
mode(arr)

