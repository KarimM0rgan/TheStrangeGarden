# Description: This program simulates plants' (Whether A or B) evolution

# Returns the number of small plants (*) in this garden.
# garden: a string containing a row of plants.

#Counts number of small plants denoted as *
def count_small(garden):  
    small_plant_count = 0
    for plant in garden:
        if plant == '*':
            small_plant_count += 1
    return small_plant_count

# Returns the number of big plants (^) in this garden.
# garden: a string containing a row of plants.

#Counts number of big plants denoted as ^
def count_big(garden):
    big_plant_count = 0
    for plant in garden:
        if plant == '^':
            big_plant_count += 1
    return big_plant_count

# Returns the number of dormant plants (.) in this garden.
# garden: a string containing a row of plants.

#Counts number of dormant plants denoted as .
def count_dormant(garden):
    dormant_plant_count = 0
    for plant in garden:
        if plant == '.':
            dormant_plant_count += 1
    return dormant_plant_count


# Creates the next generation of a garden of Plant A from the current generation.
# garden: a string containing a row of plants.
# Returns a string containing the next generation of the garden.  This string should
# be the same length as the previous generation.

def next_generation_A(garden):
    newgarden = ""          #The new garden will be stored and updated here
    for i in range(len(garden)):
        if i == 0 or i == int(len(garden)) - 1:  #Far plant are always dormant.
            newgarden += '.'
        else:
            left = garden[i - 1]  # The plant right before the current plant
            current = garden[i]  # The current plant
            right = garden[i + 1]  # The plant right after the current plant

            # New garden of the plants based on their neighbors
            if current == '*':  # If the current plant is alive
                if left == '*' and right == '*':  # If both neighbors are alive, the plant dies
                    newgarden += '.'
                elif left == '.' and right == '.':  # If both neighbors are dormant, the plant dies
                    newgarden += '.'
                else:
                    newgarden += '*'  # If neighbors are different, the plant stays alive.

            elif current == '.':  # If the current plant is dormant
                if (left == '*' and right == '.') or (left == '.' and right == '*'):  # If one neighbor is alive
                    newgarden += '*'  # The dormant plant becomes alive
                else:
                    newgarden += '.'  # At any other situation, it stays dormant.

    return newgarden 


# Runs the simulation for plant A for the given number of generations, given a
# starting garden. Note that this function doesn't return anything.
def run_garden_A(garden, generations):
    for i in range(generations + 1):  # The +1 is to nclude the starting generation
        num_dormant = count_dormant(garden)  # Count dormant plants in the current garden
        num_alive = count_small(garden)  # Count small plants in the current garden
        print(garden, num_dormant, num_alive)  # Print the garden and the counts
        garden = next_generation_A(garden)  # Generate the next generation and update the garden for the next generation


# Creates the next generation of a garden of Plant B from the current generation.
# garden: a string containing a row of plants.
# nsize: the size of the neighborhood that Plant B will use.
# Returns a string containing the next generation of the garden.  This string should
# be the same length as the previous generation.
def next_generation_B(garden, nsize):
    newgarden = ""   # This string holds the next generation of the garden.
    for i in range(len(garden)):
        if i < nsize or i >= int(len(garden)) - nsize:  # far plants are dormant
            newgarden += '.'
        else:
            neighborhood = garden[i - nsize:i + nsize + 1]  # Extract the neighborhood of the current plant
            total_alive = count_small(neighborhood) + count_big(neighborhood)  # Counts alive plants in the neighborhood
            current = garden[i]  # The current plant.

            # gets next generarion of current plants based on their neighborhood
            if current == '^':  # If the plant is big
                if total_alive % 2 == 0:  # If the number of alive plants is even, the plant becomes small
                    newgarden += '*'
                else:  # If the number of alive plants is odd, the plant becomes big
                    newgarden += '^'
            elif current == '*':  # If the current plant is small
                if total_alive % 2 == 0:  # If the number of alive plants is even, the plant becomes dormant
                    newgarden += '.'
                else:  # If the number of alive plants is odd, the plant becomes big
                    newgarden += '^'
            elif current == '.':  # If the current plant is dormant
                if total_alive % 2 == 0:  # If the number of alive plants is even, the plant becomes dormant
                    newgarden += '.'
                else:  # If the number of alive plants is odd, the plant becomes small
                    newgarden += '*'

    return newgarden


# Runs the simulation for plant B for the given number of generations, given a
# starting garden. nsize is the size of the neighborhood. 
# Note that this function doesn't return anything.
def run_garden_B(garden, nsize, generations):
    for i in range(generations + 1):
        num_dormant = count_dormant(garden)  # Count dormant plants
        num_small = count_small(garden)  # Count small plants
        num_big = count_big(garden)  # Count big plants
        print(garden, num_dormant, num_small, num_big)  # Prints the garden and the counts
        garden = next_generation_B(garden, nsize)  # Generate the next generation and update the garden
    

def main():
    keep_going = "yes"
    while keep_going == "yes":  # While loop to allow re-running the program.
        # Gets inputs
        ptype = input("Are you growing plant A or B? ")
        garden = input("What is the starting garden? ")
        sidenum = int(input("How many dormant plants are on either side? "))
        numgens = int(input("How many generations do you want to see? (not including the first) "))
        neighborhood_size = 1  # for Plant A.
        
        if ptype == "B":
            neighborhood_size = int(input("What is the neighborhood size? "))

        # implant dormant plants on both sides
        garden = ('.' * sidenum) + (garden + '.' * sidenum)

        # Simulate for Plant A
        if ptype == "A":
            print(garden, end='')
            print(' ', count_dormant(garden), end='')
            print(' ', count_small(garden))
            for i in range(numgens):
                garden = next_generation_A(garden)
                print(garden, end='')
                print(' ', count_dormant(garden), end='')
                print(' ', count_small(garden))
        
        # Simulate for Plant B
        elif ptype == "B":
            print(garden, end='')
            print(' ', count_dormant(garden), end='')
            print(' ', count_small(garden), end='')
            print(' ', count_big(garden))
            for i in range(numgens):
                garden = next_generation_B(garden, neighborhood_size)
                print(garden, end='')
                print(' ', count_dormant(garden), end='')
                print(' ', count_small(garden), end='')
                print(' ', count_big(garden))
        else:
            print("Invalid plant type.")

        # Ask if the user wants to continue
        keep_going = input("Would you like to run another simulation? (yes/no): ")
        keep_going = keep_going.lower()
        if keep_going != 'yes':
            print("Thank you for using the plant simulation!")
            break  # Exit the loop if user doesn't want to continue.

if __name__ == "__main__":
    main()
