# data frame is a multi dimensional array
import pandas as pd
Entries = {
    "temperature":[32,54,67,88,98],
    "days":["mon","tue","wed","thu","fri"]
}
df=pd.DataFrame(Entries)
# print(df.loc[4])
print(df)