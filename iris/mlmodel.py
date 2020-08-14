import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from utile.Timer import timer
import joblib


class ml:

    def __init__(self, save=False):
        self.DATASET = load_iris()
        self.INPUTS = pd.DataFrame(self.DATASET.data, columns=self.DATASET.feature_names)
        self.TARGETS = self.DATASET.target
        self.MODELS = [LogisticRegression(), DecisionTreeClassifier(), SVC(), RandomForestClassifier(), MultinomialNB(),
                       KNeighborsClassifier(), GaussianNB()]
        self.ACCURACY = list()
        self.SHORTCUT = ['lr', 'dtc', 'svm', 'rfc', 'mnb', 'knc', 'gnb']
        self.RUNTIME_RETURN = self.run_workflow(save=save)

    def train_all(self):  # train all models in the models list
        x_train, _, y_train, _ = train_test_split(self.INPUTS, self.TARGETS, test_size=0.2)
        for model in self.MODELS:
            model.fit(x_train, y_train)

    def test_all(self):  # test all models in the models list
        for model in self.MODELS:
            self.ACCURACY.append(str(round(sum(cross_val_score(model, self.INPUTS, self.TARGETS, cv=5)) / 5, 3)))

    @timer(round_off=3)
    def save_all(self):  # save all models from the models list

        for i in range(7):
            joblib.dump(self.MODELS[i], f'ML_models/{self.SHORTCUT[i]}.sav')
        with open('ML_models/accuracy.txt', 'w') as file:
            file.write("\n".join(self.ACCURACY))

    @timer(round_off=3, store=True)
    def run_workflow(self, save=False):
        self.train_all()
        self.test_all()
        if save is True:
            self.save_all()


if __name__ == '__main__':
    pass
    # ml(True)
