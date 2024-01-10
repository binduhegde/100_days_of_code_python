import pandas as pd
import random

# gets a random word df from to_learn.csv
class Word:
    def __init__(self) -> None:
        self.df = pd.read_csv('to_learn.csv')
        # there are items in the df
        self.rand_no = random.randint(0, self.df['Spanish'].size)
        self.spanish = self.df.iloc[self.rand_no]['Spanish']
        self.english = self.df.iloc[self.rand_no]['English']

    def known(self):
        print(self.spanish, self.rand_no)
        self.df.drop(self.rand_no, inplace=True, axis=0)
        self.df.to_csv("to_learn.csv", index=False)
