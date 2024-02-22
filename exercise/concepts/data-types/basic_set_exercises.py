
text = 'Programming in python.'

vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.replace(" ","")
text = text.replace(".","")
text = text.lower()

letters = set(text)
consonants = letters.difference(vowels)

#TODO
#consta = lambda letters : letters[i for i in range(len(letters))] in vowels

consta = lambda letters: all(i in vowels for i in letters)

print(f'Number of items: {len(consonants)}')

print(type(consta))
#print(f"The constants are{consta}")

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

good_lead = is_clicked.intersection(is_bought)

print("Customer ID of good lead : " + str(good_lead))