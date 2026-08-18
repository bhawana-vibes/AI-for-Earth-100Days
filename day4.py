import pandas as pd
data ={
    "student" : ["aayushi" , "bhawana" , "piyush" , "shourya"],
    "marks" : [96,78,86,96],
    "subjects" : ["maths" , "english" , "himdi" , "science"],
    "status" :["pass" , "pass" , "pass" , "fail"]
}
df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.info())
print(df[["subjects" , "status"]])
print(df.iloc[0:2, 0:2])
print(df.iloc[1,2])
print(df.iloc[2,1])