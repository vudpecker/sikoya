
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')

result = (dji1, dji2)
 
# (('AAPL.US', 'IBM.US', 'MSFT.US'), ('HD.US', 'GS.US', 'NKE.US'))
print(result)

stocks = (
    ('Apple Inc', ('AAPL.US', 310)),
    ('Microsoft Corp', ('MSFT.US', 184)),
)
#APPL.US
print(stocks[0][1][0])

info = (('Monica', 19), ('Tom', 21), ('John', 18))

asce = sorted(info, key = lambda elem: elem[1]) # returns list TODO needs to be type casted

desc = tuple(sorted(info, key = lambda elem: elem[1], reverse=True))
 
print(f'Ascending: {asce}')
print(f'Descending: {desc}')

x = lambda a, b : a * b
print(x(5, 6))