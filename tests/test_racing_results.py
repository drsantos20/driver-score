import unittest
from racing.racing_score import read_file


class TestTrackResult(unittest.TestCase):

    def setUp(self):
        self.classification = read_file('../logs/racing-results.txt')

    def test_get_positions_by_driver(self):
        self.assertEqual(
            self.classification[0], ('038 F.MASSA', 251.578),
        )
        self.assertEqual(
            self.classification[1], ('002 K.RAIKKONEN', 255.153),
        )
        self.assertEqual(
            self.classification[2], ('033 R.BARRICHELLO', 256.08),
        )
        self.assertEqual(
            self.classification[3], ('023 M.WEBBER', 257.722),
        )
        self.assertEqual(
            self.classification[4], ('015 F.ALONSO', 294.221),
        )


if __name__ == '__main__':
    unittest.main()
