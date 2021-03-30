calculation_To_units =  24
name_of_unit = "hours"

def days_to_units(num_of_day):
    if num_of_day > 0:
        return f"{num_of_day} days are {num_of_day * calculation_To_units} {name_of_unit}"

    elif num_of_day == 0:
        return"you entered a 0, please enter a valid positive number "

    else:
        return"you entered a negative value, so no conversion for you!"
    
user_input = input("hey user ,enter a number of day and i will canvert it to hour!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(int(user_input))
print(calculated_value)