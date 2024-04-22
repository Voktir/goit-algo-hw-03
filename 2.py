import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min<1 or max>1000 or max<(min+quantity):
        return []
    else:
        lst = []
        min_while = min
        while min_while <= max:
            lst.append(min_while)
            min_while += 1
        dif = max-min
        while dif >= quantity:
            lst.pop(random.randint(0, dif))
            dif -= 1 
    return lst

# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)