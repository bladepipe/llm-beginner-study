import unittest
from bigram_scratch import P

class TestBigramProbs(unittest.TestCase):
    def test_h_predicts_e(self):
        self.assertIn('e', P.get('h', {}))
        self.assertGreater(P['h']['e'], 0.5)

    def test_t_predicts_h(self):
        self.assertIn('h', P.get('t', {}))
        self.assertEqual(P['t']['h'], 1.0)

if __name__ == '__main__':
    unittest.main()