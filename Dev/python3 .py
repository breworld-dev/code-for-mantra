calculation_To_units =  24
name_of_unit = "hours"

def days_to_units(num_of_day):
    output=num_of_day * calculation_To_units
    return f"{num_of_day} days are {output} {name_of_unit}"


user_input = input("hey user ,enter a number of day and i will canvert it to hour!\n")


calculated_value = days_to_units(int(user_input))
print(calculated_value)