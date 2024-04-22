import re

def normalize_phone(phone_number: str) -> str:
    plus_split = []
    pat_split = r"\+"
    plus_split = re.split(pat_split, phone_number)
    try:
        plus_split[1] = re.sub(r"\D", "", plus_split[1])
        plus_split[1] = plus_split[1] if re.search("38..........", plus_split[1]) else f"38{plus_split[1]}"
        result = f"+{plus_split[1]}"
    except IndexError:
        plus_split[0] = re.sub(r"\D", "", plus_split[0])
        plus_split[0] = plus_split[0] if re.search("38..........", plus_split[0]) else f"38{plus_split[0]}"
        result = f"+{plus_split[0]}"
   
    return   result 

# raw_numbers = [
#     "067\\t123 3867",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)