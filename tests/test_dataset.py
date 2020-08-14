import unittest
from iris.dataset import data_to_dict, database


class MyTestCase(unittest.TestCase):
    def test_return(self):
        self.assertEqual("<class 'pandas.core.frame.DataFrame'>", str(type(data_to_dict())))

    def test_data_loading(self):
        self.assertEqual("<class 'sklearn.utils.Bunch'>", str(type(database)))


if __name__ == '__main__':
    unittest.main()
