import unittest
from racing.racing_score import read_file


class TestTrackResult(unittest.TestCase):

    def test_load_file(self):
        read_file('logs/racing-results.txt')







if __name__ == '__main__':
    unittest.main()
