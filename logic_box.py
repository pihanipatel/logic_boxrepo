# print("Welcom to the Pattern Generator and Number Analyzer!")


# print("Select an option:\n1. Generate a Pattern\n2. Analyze a Range of Numbers\n3. Exit")
# num = int(input("Enter your choice: "))

# rows = int(input("Enter the number of rows for the pattern: "))
# print("\nPattern: \n")
# for i in range (0,rows):
#     for j in range (i+1):
#         if rows <= 0:
#            break
#         if rows <= 0:
#            pass 
#         print("*",end=" ")
#     print()    


# print("Select an option:\n1. Generate a Pattern\n2. Analyze a Range of Numbers\n3. Exit")
# num = int(input("Enter your choice: "))
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# for i in range (start,end):
#     if i % 2 == 0:
#         print("Number", i ,"is Even")
#     else:
#         print("Number", i ,"is Odd")
#     sum += i
# print("Sum of all numbers from", start, "to", end, "is: ",sum)    


# print("Select an option:\n1. Generate a Pattern\n2. Analyze a Range of Numbers\n3. Exit")
# num = int(input("Enter your choice: "))
# print("Exiting the program. Goodbye!")

######
print("Welcom to the Pattern Generator and Number Analyzer!\n")

for i in range (1,4):

    print("\nSelect an option:\n1. Generate a Pattern\n2. Analyze a Range of Numbers\n3. Exit")
    num = int(input("Enter your choice: "))
    match num:
        case 1:
            rows = int(input("Enter the number of rows for the pattern: "))
            print("\nPattern: \n")
            if rows > 0:
                for i in range (0,rows):
                    for j in range (i+1):
                        if rows > 20:
                            break    
                        print("*",end="")
                    print()  
            else: 
                print("\nError Invalide input re-enter input")
        case 2:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            

            sum = 0
            if start < end:
                for i in range (start,end+1):
                    if i % 2 == 0:
                        print("Number", i ,"is Even")
                    else:
                        print("Number", i ,"is Odd")     
                    sum += i
                print("Sum of all numbers from", start, "to", end, "is: ",sum)    
            if start > end:
               print("\nError Invalide input re-enter input")

        case 3:
            print("Exiting the program. Goodbye!")
        case 4:
            pass    
        case _:
            print("Invalid choice")


