import pandas
data={
    "adUN"  : ["admin", "Babu", "Ravi"],
    "adPWD" : ["password", "reddy", "teddy"]
}
dataframe = pandas.DataFrame(data)
print(dataframe)
dataframe.to_csv("sample.csv", index=False)