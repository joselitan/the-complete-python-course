# numbers = [0,1,2,3,4]
# doubled_numbers = []


# for number in numbers:
#     doubled_numbers.append(number*2)
# print(doubled_numbers)


# numbers = [0,1,2,3,4]
# doubled_numbers = [number * 2 for number in numbers]
# print(doubled_numbers)


# doubled_numbers = [number * 2 for number in range(5)]
# print(doubled_numbers)


# friend_ages = [22, 31, 35, 37]
# age_strings = [f"My friend is {age} year old." for age in friend_ages]
# print(age_strings)


# names = ["Rolf", "Bob", "Jen"]
# lower = [name.lower() for name in names]
# print(lower)


# friend = input("Enter your friend name: ")
# friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
#
# if friend in friends:
#     print(f'{friend} is on of your friends')


friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends")