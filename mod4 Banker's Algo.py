numCustomers = 5
numResources = 4

available = []
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]] 
need = []

###########################
### Safety Algorithm Needed
###########################


if __name__=="__main__":
    print("There is currently 5 customers and 4 resource types.\n")

    for i in range(numResources):
        print(f"Number of Instances for {i+1}:")
        instance = input("> ")
        available.append(instance)

    def commands(cmd):
        if cmd == "*":
            print(f"Avaiable: \n", available)
            print(f"Maximum: \n", maximum)
            print(f"Allocation: \n", allocation)
            print(f"Need: \n", need)
        #elif cmd == "RL":
            #Not sure how to do this one exactly
        #elif cmd == "RQ":
            #Take input for specific customer as shown in text
            #Take input for that customer's resource types
            #Put through safety algo and output if satisified or denied
        elif cmd == "QUIT":
            quit()
        else:
            print("Invalid Command. Try again.")
            cmd = input ("> ")
            commands(cmd)

    print('''
    ================
    == Command List:
    ================
    RQ = Request Resources
    RL = Release Resources
    * = Output all data structure values
    QUIT = Quit Program 
    ''')

    cmd = input ("> ")
    commands(cmd)
