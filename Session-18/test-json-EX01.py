import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()
person = json.loads(jsonstring)

for element in person:

    # Print the information on the console, in colors
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(element['Firstname'], element['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(element['age'])

    # Get the phoneNumber list
    phoneNumbers = element['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])