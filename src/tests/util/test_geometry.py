import unittest

from util.geometry import Vector

class GeometryTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_vector_add_vector(self):
        vec1 = Vector(10, 10, 0)
        vec2 = Vector(10, 20, 0)
        res = vec1 + vec2
        expected = Vector(20, 30, 0)
        self.assertEqual(expected, res)

    def test_vector_add_int(self):
        vec1 = Vector(10, 0)
        res = vec1 + 10
        expected = Vector(20, 10)
        notExpected = Vector(20, 10, 10)
        self.assertEqual(expected, res)
        self.assertNotEqual(notExpected, res)