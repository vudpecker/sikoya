
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt = "For only {price} dollars!"
print(txt.format(price = "Three"))


a = "hello"
b = "welcome to the jungle"
c = "10.000"
num = 3415

print(str(num).zfill(8))
d = a.zfill(10)
print(a.zfill(10))
print(b.zfill(25))
print(c.zfill(10))
print(d)


url = (
    'https://e-smartdata.teachable.com/'
    'p/sciezka-data-scientist-machine-learning-engineer'
)

new_str = url.split('/')[-1]
text = new_str.replace("-", " ")
print(text)


