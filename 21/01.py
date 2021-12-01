import pandas as pd
n = pd.Series([int(x) for x in open("01.in")])
print((n.diff() > 0).sum())
print((n.rolling(3).sum().diff() > 0).sum())
