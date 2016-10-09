import random, string
letter_input_1 = input("What letter do you want? Enter 'v' for Vowels, 'c' for Consonants, 'l' for any Letters")
letter_input_2 = input("What letter do you want? Enter 'v' for Vowels, 'c' for Consonants, 'l' for any Letters")
letter_input_3 = input("What letter do you want? Enter 'v' for Vowels, 'c' for Consonants, 'l' for any Letters")

def generator():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return (name)
print (generator())