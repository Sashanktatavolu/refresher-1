import pandas as pd
# BS={"day1":12,"day2":13,"day3":14}
# abs=pd.Series(BS)
# print(abs)

Calories={"day1":1200,"day2":1300,"day3":1400,"day4":1500,"day5":1600}
check=pd.Series(Calories, index=["day1","day5"])
print(check)