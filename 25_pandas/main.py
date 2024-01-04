import pandas as pd 

''' GETTING THE TEMP COLUMN OF THE DATA IN A LIST USING CSV LIBRARY'''
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatue = [item[1] for item in data]
#     temperatue = [int(i) for i in temperatue[1:]]
#     print(temperatue)


# df = pd.read_csv('weather_data.csv')
# print(df['temp'])

# df = pd.read_csv('progress.csv')
# # find median of Mins
# print(f"{df['Mins'].median():.2f}")
# # get the row where the Mins is max
# print(df[df['Mins'] == df['Mins'].max()])



# the goal of this challenge is to load squirrel.csv
# then create a new csv file called squirrel_count.csv
# it should have only two rows. 1 is fur color and 2nd is count
# there are only squirrels of 3 colors: grey, cinnamon and black
# it can be found under the column "Primary Fur Color"
# get the count of these squirrels

df = pd.read_csv('squirrel.csv')
#print(df.columns)

new_df = df[['Primary Fur Color']]
new_df = new_df.dropna(subset=['Primary Fur Color'])

gray_count = new_df[new_df['Primary Fur Color'] == 'Gray'].size
cinnamon_count = new_df[new_df['Primary Fur Color'] == 'Cinnamon'].size
black_count = new_df[new_df['Primary Fur Color'] == 'Black'].size

d = {'Fur Color': ['grey', 'cinnamon', 'black'], 'Count':[gray_count, cinnamon_count, black_count]}
result_df = pd.DataFrame(d)
result_df.to_csv('squirrel_count.csv')