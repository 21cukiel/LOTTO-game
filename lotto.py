import random


def lotto():
    """Function compare our numbers with the drawn numbers"""
    try:
        user_numbers = []
        """User input 6 numbers, function add them to the table"""
        while len(user_numbers) <= 5:
            i = int(input("Please input numbers from 1 to 49: "))

            if i in user_numbers:
                print("You can't insert 2 same numbers!")
                continue
            elif i > 49:
                print(f"{i} is bigger then 49!")
                continue
            elif isinstance(i, (str, float, bool)):
                print("It,s not a number!")
            user_numbers.append(i)
        random_numbers = []
        """Computer drawn 6 numbers from range 1-49 and add them to table"""
        while len(random_numbers) <= 5:
            i = random.randint(1, 49)
            if i in random_numbers:
                continue
            random_numbers.append(i)

        user_numbers.sort()
        random_numbers.sort()
        goals = []
        """Function compare user numbers with computer numbers and displays common numbers on the screen"""
        for i in user_numbers:
            if i in random_numbers:
                goals.append(i)
        user_list = ''.join(str(user_numbers))
        random_list = ''.join(str(random_numbers))
        goals_list = ''.join(str(goals))
        return f"Computer numbers: {random_list}\n Your numbers: {user_list} \n Numbers hit: {goals_list}"
    except ValueError:
        """When input value isn't number, print "It's not a number" """
        return "It,s not a number!"


if __name__ == "__main__":
    print(lotto())
