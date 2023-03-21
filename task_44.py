'''
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
dctOne = {'robot': 0, 'human':1}
dctTwo = {'robot': 1, 'human':0}
data['whoAmI_human'] = data['whoAmI'].map(dctOne)
data['whoAmI_robot'] = data['whoAmI'].map(dctTwo)
del data[data. columns [0]]
data
