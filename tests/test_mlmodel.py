import unittest
from iris.mlmodel import ml
import os

test_model = ml()

MODELS_OBJECTS = ['accuracy.txt', 'dtc.sav', 'gnb.sav', 'knc.sav',
                  'lr.sav', 'mnb.sav', 'rfc.sav', 'svm.sav', 'meta.yaml']


# TODO
# [X]Attributes
# [X]Runtime
# Saved stuffs

class MyTestCase(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual("<class 'sklearn.utils.Bunch'>", str(type(test_model.DATASET)))
        self.assertNotEqual(0, len(test_model.ACCURACY))
        self.assertEqual(7, len(test_model.MODELS))
        self.assertEqual("LogisticRegression()", str(test_model.MODELS[0]))
        self.assertEqual("GaussianNB()", str(test_model.MODELS[-1]))
        self.assertEqual(['lr', 'dtc', 'svm', 'rfc', 'mnb', 'knc', 'gnb'], test_model.SHORTCUT)
        self.assertEqual("<class 'tuple'>", str(type(test_model.RUNTIME_RETURN)))

    def test_runtime(self):
        self.assertLess(test_model.RUNTIME_RETURN[-1], 5)

    def test_storage(self):
        self.assertGreater(len(os.listdir('./iris/ML_models')), 1)
        self.assertEqual(sorted(MODELS_OBJECTS), sorted(os.listdir('./iris/ML_models')),
                         msg="Consider rerunning the 'ml' class with save parameter made True.")
        with open('./iris/ML_models/accuracy.txt', 'r') as file:
            self.assertNotEqual(file.read(), "")


if __name__ == '__main__':
    unittest.main()
