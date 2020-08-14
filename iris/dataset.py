from sklearn.datasets import load_iris
import pandas as pd

database = load_iris()


def data_to_dict(num=6):
    data = pd.DataFrame(database.data, columns=database.feature_names)
    data["targets"] = database.target
    return data.head(num)


if __name__ == '__main__':
    pass
    # data_to_dict()
