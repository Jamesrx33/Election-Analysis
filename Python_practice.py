print("Hello World")

print(type(""))

counties = ["Arapahoe", "Denver", "Jefferson"]

my_integer = int()

my_integer = 3

print(my_integer)

counties[2]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")