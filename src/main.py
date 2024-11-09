# BirdfeedersForest app
#
# to start go to folder birdfeeders and type
#     python.exe .\src\main.py
#
# Copyright (c) by  Shilyn Makin
#



# variable declaration

birdfeeders: int = 0 # number of birdfeeders in the forest
survivalrate: float = 0.0 # the input data given to the program
birdsurvivalrate: float = 0.0 # the calculated survival rate as function of number of feeders
forestattractiveness: str = " The forest is considered more healthy and attractive for visitors due to the increased number of birds"

# Function to classify bird feeder segments
def classify_bird_feeders(feeders):

    if feeders<1
    return 'O' # segment O
    if 1 <= feeders <= 3:
        return 'A'  # Segment A
    elif 4 <= feeders <= 6:
        return 'B'  # Segment B
    elif feeders >= 7:
        return 'C'  # Segment C
    else:
        return 'Invalid'

# Function to classify the survival rate level
def classify_survival_rate_level(survivalrate):
    
    if 0.1 <= survivalrate <= 0.3:
        return 'A'  # Segment A
    elif 0.3 < survivalrate <= 0.6:
        return 'B'  # Segment B
    elif 0.6 < survivalrate <= 0.9:
        return ''  # Segment C
    else:
        return 'Invalid'

# Function to determine the forest attractiveness
def calculate_attractiveness(feeders_segment, survival_rate_level):
    attractiveness_mapping = {
        ('0') :"Not very attractive"
        
        ('A') "Slightly attractive",

        ('B'): "Quite attractive",
        
        ('C'): "Highly attractive",

# Return the attractiveness level based on the mapping
    return attractiveness_mapping.get((feeders_segment, survival_rate_level), "Unknown")
       
    
# function to deterimne the potential survival rate of birds 
# as function of initial presence  of feeders
def calculate_survival_rate(feeders, survivalrate):
    if feeders <= 1:
        return survivalrate
    else:
        return survivalrate * 1.38


# procedure to print results
def print_results(attractiveness, survivalrate):
    print("The forest is considered: ", attractiveness)
    print("Survival rate for birds in areas with feeders: ", survivalrate )
    print('\n')
    
# Example usage
# Input values
birdfeeders = 5  # Change this value for testing
survivalrate = 0.2  # Change this value for testing

# Calculate the bird survival rate
birdsurvivalrate = calculate_survival_rate(birdfeeders, survivalrate)

# Classify bird feeders and survival rate level
feeders_segment = classify_bird_feeders(birdfeeders)
survival_rate_level = classify_survival_rate_level(birdsurvivalrate)

# Determine the forest attractiveness
attractiveness = calculate_attractiveness(feeders_segment, survival_rate_level)

# Output the results
print(f"Number of Bird Feeders: {birdfeeders}")
print(f"Initial Survival Rate: {survivalrate}")
print(f"Calculated Bird Survival Rate: {birdsurvivalrate:.2f}")
print(f"Feeders Segment: {feeders_segment}")
print(f"Survival Rate Level: {survival_rate_level}")
print(f"Forest Attractiveness: {attractiveness}")





# main function to control the app
def main():
    print("\nWelcome to the Forest Attractiveness Calculator!")
    # major loop to read in user input
    while True:
        # try to catch eventually ocurring input mistakes
        try:
            birdfeeders = int(input("Enter the number of bird feeders in the forest: "))
            if birdfeeders < 0:
                print("Number of feeders cannot be negative. Please try again.")
                continue
            if birdfeeders>20:
                print ("Allowed number of feeders is 1-20")
                continue
            forestattractiveness = calculate_attractiveness(birdfeeders)
            survivalrate = float(input("Enter the local survival rate of birds: "))
            if survivalrate <= 0:
                print("Survival rate need to be positive. Please try again.")
                continue
            if survivalrate > 100:
                print ("survivalrate cannot exceed 100%" )
                continue
            birdsurvivalrate = calculate_survival_rate(birdfeeders, survivalrate)
            print_results(forestattractiveness, birdsurvivalrate)
            if input("new calculation (y or n)? ") == "n":
                break
            else:
                print('\n')
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
