
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

asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
 
 
print(f'Ascending: {asc}')
print(f'Descending: {desc}')