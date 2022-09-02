import pandas as pd

# train = pd.read_csv("../datasets/classification/train.csv")
test = pd.read_csv("../datasets/classification/test.csv")
# dataset = train.append(test, ignore_index = True)

df = test.sample(n = 10000, random_state = 5, axis = 0)
df.to_csv("./classification_samples_test.csv")
    