import pandas as pd
print("version:",pd.__version__) # check version of pandas 

# Read operation 
df = pd.read_csv('pokemon_data.csv')
print("csv file ",df)
# head(n) print first n rows 
print("first five: ",df.head(5))
#tail(n) print last n rows 
print("last five: ",df.tail(5))









  
    