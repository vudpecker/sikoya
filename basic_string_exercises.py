
text = 'python is a popular programming language.'

print(text.count('p'))


path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'


print(f"path1: {path1.startswith('youtube')}")
print(f"path2: {path2.startswith('youtube')}")

code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")

path1 = (
    'https://e-smartdata.teachable.com/path-x/'
    'sciezka-data-scientist-machine-learning-engineer'
)
path2 = (
    'https://e-smartdata.teachable.com/source/'
    'data-scientist-deep-learning-engineer'
)

print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")



code1 = 'FVNISJND-20'
print(f"code1: {code1.isalnum()}")

text = '      100 Days of Code   '
new_text = text.strip() # Trim the string
#print(text.lower())
print(new_text.lower())

headers = 'ProductID,ProductName,Category,Price'
header_list = headers.split(",")
print(header_list)

str = "Hello!Welcome to Tutorialspoint.";
suffix = "oint.";
result=str.endswith(suffix, 27)
print("The input string ends with the given suffix:",result)
result=str.endswith(suffix, 28)
print("The input string ends with the given suffix:",result)

#Split attribute of string
print("Hello:Nick:welcome".split(":")[1])
print('Hello Nick welcome'.split())
#Array or List
print(['Hello', 'Nick', 'welcome'][2])
print(len(['Hello', 'Nick', 'welcome'][2]))

text = """Python is a general-purpose language.
Python is popular."""

print(text.splitlines())