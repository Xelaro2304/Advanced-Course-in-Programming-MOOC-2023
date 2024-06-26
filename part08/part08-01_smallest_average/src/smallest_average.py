# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]
    lowest_avrg = 1500
    for i in persons:
        avrg = 0
        for key, value in i.items():
            if key == "name":
                continue
            avrg += value
        avrg = avrg/3
        if avrg < lowest_avrg:
            lowest_avrg = avrg
            loser = i
    return loser

