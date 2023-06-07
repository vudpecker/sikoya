"""intro to Pandas"""

import pandas as pd

data = {
    'CustID' : [1, 2, 3, 4, 5],
    'Name' : ['Doe', 'Jo', 'Tod']
}
df = pd.DataFrame(data)

print(df)
