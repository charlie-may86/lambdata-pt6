
from pandas import DataFrame

from my_lambdata6.my_mod import enlarge

print('hello')

print(enlarge(8))


df = DataFrame({'state': ['CT', 'CO', 'CA', 'TX']})
print(df.head())