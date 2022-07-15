# --------------------Best Practices --------------------------------------------------------------
# Put most code a function or class
# Use __name__ to control execution of your code 
# Create a function called main() to contain the code you want to run 
# Call other functions from main()
#---------------------------------------------------------------------------------------------------

#*********** Summmary of Best Practices **********************************************************
# 1. Put code that takes a long time to run or has other effects on the computer in a function
# or class, so you can control exactly when that code is executed
# 2. Use the different values of __name__ to determine the context and change the behavior of
# code with a conditional statement 

# 3. Name your entry point function main() in order to communicate the intention of the funciton
# even though Python does not assign any special significance to a function named main() 

# 4.If we want to reuse functionality from our code, we should define the logic in functions outside
# main() and call those functions within main()
#*****************************************************************************************************

from time import sleep

print("This is my file to demonstrate best practices. ")

def process_data(data):
    print("Begining data processing...")
    modified_data = data + " that has been modified "
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)
    
def main():
    data = "My data read from the web"
    print(data)
    modified_data = process_data(data)
    write_data_to_database(modified_data)
    
if __name__ == "__main__":
    main()