import pandas as pd

class DataCorruptionError(Exception):
    pass



def validate_data():
    df = pd.read_csv('data.csv')
    if any(df.isnull()):
        raise DataCorruptionError("Data have missing value")
    
def validate_data1(data):
    if not data:
        raise DataCorruptionError("Data have missing value")
    for item in data:
        if not item:
            raise DataCorruptionError("Data have missing value")
        
    print("Average value: ", sum(data)/len(data))
    
try:
    validate_data1([1,2,3,None])
    validate_data()
except Exception as e:
    print("Error:",e)



