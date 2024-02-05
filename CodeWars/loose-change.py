def loose_change(cents):
    if cents < 0:
        cents = 0
    change_dict = {}

    quarters = int(cents/25)
    dimes = int((cents - quarters*25)/10)
    nickels = int((cents - quarters*25 - dimes*10)/5)
    pennies = int((cents - quarters*25 - dimes*10 - nickels*5)/1)


    change_dict['Nickels'] = nickels
    change_dict['Pennies'] = pennies
    change_dict['Dimes'] = dimes
    change_dict['Quarters'] = quarters

    return change_dict
