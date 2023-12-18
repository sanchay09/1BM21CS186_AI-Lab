def vacuum_world():
    # Initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': 0, 'B': 0}
    cost = 0

    location_input = input("Enter Location of Vacuum")  # User input of the location the vacuum is placed
    status_input = int(input("Enter status of " + location_input))  # User input if the location is dirty or clean
    status_input_complement = int(input("Enter status of the other room"))
    print("Initial Location Condition" + str(goal_state))

    if location_input == 'A':
        # Location A is Dirty.
        print("Vacuum is placed in Location A")
        if status_input == 1:
            print("Location A is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['A'] = 0
            cost += 1  # Cost for suck
            print("Cost for CLEANING A " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == 1:
                # If B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B. ")
                cost += 1  # Cost for moving right
                print("COST for moving RIGHT " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['B'] = 0
                cost += 1  # Cost for suck
                print("COST for SUCK " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action " + str(cost))
                # Suck and mark clean
                print("Location B is already clean.")

        if status_input == 0:
            print("Location A is already clean ")
            if status_input_complement == 1:  # If B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to Location B. ")
                cost += 1  # Cost for moving right
                print("COST for moving RIGHT " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['B'] = 0
                cost += 1  # Cost for suck
                print("Cost for SUCK " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print(cost)
                # Suck and mark clean
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in Location B")
        # Location B is Dirty.
        if status_input == 1:
            print("Location B is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['B'] = 0
            cost += 1  # Cost for suck
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == 1:
                # If A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A. ")
                cost += 1  # Cost for moving right
                print("COST for moving LEFT " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['A'] = 0
                cost += 1  # Cost for suck
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)
            # Suck and mark clean
            print("Location B is already clean.")

            if status_input_complement == 1:  # If A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A. ")
                cost += 1  # Cost for moving right
                print("COST for moving LEFT " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['A'] = 0
                cost += 1  # Cost for suck
                print("Cost for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                # Suck and mark clean
                print("Location A is already clean.")

    # Done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()