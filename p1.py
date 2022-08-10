import pandas as pd
mydataset = {
    'cars':['BMW',"Volvo","Food"],
    'passings':[3,7,2]
}
v1 = pd.DataFrame(mydataset)
print(v1)
# pandas vrsion 
print("pandas version used",pd.__version__)