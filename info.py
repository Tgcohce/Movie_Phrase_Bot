import pandas as pd
from random import seed
from random import randint





mp = pd.read_csv('Catchphrase.csv')

def mane(x):
    phrase = mp.loc[x,"Catchphrase"]
    Mname = mp.loc[x,"Movie Name"]
    Cxt = mp.loc[x,"Context"]
    output = f"{phrase}\n \nMovie: {Mname}\n \nContext: {Cxt}"
    return output

