import pandas as pd
import numpy as np

train = pd.read_csv("./train.csv")
train["rowtype"] = ["TRAIN" for i in range(train.shape[0])]
val_indices = np.random.choice(range(train.shape[0]), int(train.shape[0] * 0.1), replace = False)

train.loc[val_indices, "rowtype"] = ["VALIDATE" for i in range(int(train.shape[0] * 0.1))]

test = pd.read_csv("./test.csv")
test["rowtype"] = ["TEST" for i in range(test.shape[0])]

dataset = train.append(test, ignore_index = True)

dataset.to_csv("./classification.csv")

