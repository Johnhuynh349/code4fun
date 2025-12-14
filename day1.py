def can_enter_club(value):
    #only for people who are at least 20 years old
    result = []
    run_time = 0
    while run_time < len(value):
        if value[run_time] >= 20:
            result.append(True)
            run_time+=1
        else:
            result.append(False)
            run_time+=1
    return result


listofcustomer = [16, 20, 21, 24, 17, 19, 40, 50, 25]
print(listofcustomer)
print(can_enter_club(listofcustomer))
