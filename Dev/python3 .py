 


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
                return f"{num_of_days} days are {num_of_days * 24 * 60 } minutes"
    else: 
        return"unsupported unit"


def validate_and_execute(): 
    try:
        user_input_number = int(day_and_unit_dictionary["days"])

        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, day_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    days_to_units = user_input.split(", ")
    print(days_to_units)
    day_and_unit_dictionary = {"days": days_to_units[0],"unit": "hours"}
    print(day_and_unit_dictionary)
    print(type(day_and_unit_dictionary))
    validate_and_execute()


message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20, 40, 20, 100]
list_of_mouths = ["january", "february", "june"]
set_of_days = {20, 45, 100}
