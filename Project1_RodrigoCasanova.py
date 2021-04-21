#Name: Rodrigo Casa Nova
#Project 1
#Test of hypotesis
from graphics import*
import pandas as pd #import the pandas library to be able to manipulate data from outside source
import numpy as np #import numpy to be able to convert a multidimensional array into a 1D array

#table_car will be the variable in which I will use to read the table_car.csv
table_car = pd.read_csv ("table_car.csv")

#table_car_for_display will used to print the untainted table
table_car_for_display = pd.read_csv("table_car.csv")

#I will use the pandas set_index  method to set a List, Series or Data frame as index of a Data Frame
table_car.set_index("am", inplace=True)

#both manual_list and automatic_list will be used as variables. Which will contain the version of table_car
#where only the mpg and manual or automatic values will appear. Making it easier to convert to a 1D array
#once they are separeted
manual_list = [table_car.loc['Manual','mpg']]
automatic_list = [table_car.loc['Automatic','mpg']]

#I have created a series of functions which will make easier in the future to upgrade the code if necessary
#the flat_arr function will be used to convert the multidimensional array into a 1D array.
#it will receive the list to convert and will return the converted array, to do that I will use the numpy
#reshape() method
def flat_arr(list_to_convert):

    flat_arr = np.reshape(list_to_convert,-1) #the -1 in the reshape() is to make sure it will convert
                                              # any shape of array to 1D array.
    return flat_arr

#after the list is converted to a 1D array, I will use the my_mean function to calculate the mpg mean of both
#manual_list and automatic_list
def my_mean(list_to_sample):
    return sum(list_to_sample) / len(list_to_sample)#it will calculate the sum of all values in the list
                                                    #and divide by it's length to obtain the mean

#I will use the results_calculator function to analize which variable has the highest mean, and present the
#results
def results_calculator(manual_mean, automatic_mean):
    if manual_mean > automatic_mean:
        print("The manual engine has the highest mpg, with a mean of ", manual_mean)
    elif manual_mean < automatic_mean:
        print("The automatic engine has the highest mpg, with a mean of ", automatic_mean)

#the main function is to execute all the other functions in the code
def main():

    #to print the inicial table
    print(table_car_for_display)

    #calling the manual_flat_arr function with the manual_list variable
    manual_flat_arr = flat_arr(manual_list)
    #calling the automatic_flat_arr function with the automatic_list variable
    automatic_flat_arr = flat_arr(automatic_list)

    #outputing the manual and automatic means
    print("Manual mpg mean: ", my_mean(manual_flat_arr))
    print("Automatic mpg mean: ", my_mean(automatic_flat_arr))

    #calling the results_calculator function with manual_flat_arr and automatic_flat_arr variables
    results_calculator(my_mean(manual_flat_arr),my_mean(automatic_flat_arr))

#this code will help to check if the .py was imported from another file
if __name__ == '__main__':
    main()
    print("Project 1 executed when ran directly")
else:
    print("Project 1 executed when imported")

