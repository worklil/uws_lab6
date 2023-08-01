'''
Question 3
Create a fully commented program to:
Read in a first name and a surname from the keyboard and output in the format Surname, Initial e.g.
Terry Gilliam becomes Gilliam, T (include the comma).
The user should be able to repeat the process as many times as they wish.

'''
n = int(input("how many times do you want to repeat it? \t"))
for counter in range(n):
    first_name = input("What's your first name? \t")
    surname = input("What's your surname? \t")
    l = list(first_name)
    def count_letters(name):
        letters = len(name)
        return letters


    fname_count = count_letters(first_name)
    sname_count = count_letters(surname)
    print(surname + ",", l[0])