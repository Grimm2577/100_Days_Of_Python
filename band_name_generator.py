#Hi everyone this is my day 1 project and the code that i wrote for the project, Day 1 Officially Completed!

# importing colorama to add some color to the terminal text
from colorama import Fore

# adding a greeting to the program
intro = "Welcome To Band Name Generator."

# printing the intro and setting its color to green
print(Fore.GREEN + intro)

# receiving and storing the city name into a variable and setting the question text color to white
childhood_city = input(Fore.WHITE + "In what city did you grow up?\n")

# receiving and storing the pet name into a variable and setting the question text color to white
pet_name = input(Fore.WHITE + "What is your pets name\n")

# creating a band name string and concatenating the 2 previous variables
band_name = childhood_city + " " + pet_name

# printing the final out put and setting the band name text color to cyan
print("Your band name could be: " + Fore.CYAN + band_name)
