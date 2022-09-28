import pandas as pd
import numpy as np

train = pd.read_csv("./train.csv")
train["rowtype"] = ["TRAIN" for i in range(train.shape[0])]
val_indexes = np.random.choice(range(train.shape[0]), int(train.shape[0] * 0.2), replace = False)

print(len(val_indexes[:int(train.shape[0] * 0.1) + 1]))
print(len(["VALIDATE" for i in range(int(train.shape[0] * 0.1))]))

train.loc[val_indexes[:int(train.shape[0] * 0.1) + 1], "rowtype"] = ["VALIDATE" for i in range(int(train.shape[0] * 0.1) + 1)]

train.loc[val_indexes[int(train.shape[0] * 0.1) + 1:], "rowtype"] = ["TEST" for i in  range(int(train.shape[0] * 0.1) + 1, int(train.shape[0] * 0.2))]

train.to_csv("./regression.csv")

