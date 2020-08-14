import unittest
from iris.plot_generator import data_frame, scatter
import os

GRAPHS = ['fig_3d.html',
          'fig_pl_pw.html',
          'fig_pl_sl.html',
          'fig_pl_sw.html',
          'fig_pw_pl.html',
          'fig_pw_sl.html',
          'fig_pw_sw.html',
          'fig_sl_pl.html',
          'fig_sl_pw.html',
          'fig_sl_sw.html',
          'fig_sw_pl.html',
          'fig_sw_pw.html',
          'fig_sw_sl.html',
          'file.html',
          'meta.yaml']


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual("<class 'pandas.core.frame.DataFrame'>",
                         str(type(data_frame)))
        self.assertEqual(scatter(), "Done")

    def test_storage(self):
        self.assertEqual(GRAPHS,
                         os.listdir('./iris/static/graphs'))


if __name__ == '__main__':
    unittest.main()
