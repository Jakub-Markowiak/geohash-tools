import sys
sys.path.insert(0, './src')

import geohash_tools as gh
import unittest

class TestEncoding(unittest.TestCase):
    def test_encode(self):
        geohash = 'u3h4g07xwp85'
        geohash_precision = [gh.encode(51.1111, 17.0119, precision=x) for x in range(2,10)]
        for index, x in enumerate(range(2,10)):
            self.assertEqual(geohash_precision[index], geohash[:x])
    
    def test_deocde(self):
        geohash = 'u3h4g07xwp85'
        lat, lon = gh.decode(geohash)
        self.assertAlmostEqual(51.1111, lat, places=4)
        self.assertAlmostEqual(17.0119, lon, places=4)

class TestNeighbours(unittest.TestCase):
    def test_adjacent(self):
        geohash = 'gbsuv'
        geohash_top = gh.adjacent(geohash, 'top')
        self.assertEqual(geohash_top, 'gbsvj')
    
    def test_neighbours(self):
        geohash = 'gbsuv'
        geohash_neigbhours = gh.neighbours(geohash)
        self.assertEqual(set(geohash_neigbhours), {'gbsvh', 'gbsvj', 'gbsvn', 'gbsuu', 'gbsuv', 'gbsuy', 'gbsus', 'gbsut', 'gbsuw'})

class TestDistance(unittest.TestCase):
    def test_distance(self):
        geohash_1, geohash_2 = 'gbsuv', 'gbsus'
        calculated_distance = gh.distance(geohash_1, geohash_2)
        distance = 296936.29
        self.assertAlmostEqual(calculated_distance, distance, places=1)

if __name__ == '__main__':
    unittest.main()