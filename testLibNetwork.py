import libNetwork
import unittest


class TestLibNetwork(unittest.TestCase):
    def test_get_local_ip(self):
        self.assertEqual(libNetwork.get_local_ip(), "10.139.36.108")

    def test_is_valid_ip_from_arr(self):
        ip_arr = ["10.139.36.108"]
        self.assertEqual(libNetwork.is_valid_ip_from_arr(ip_arr), True)

    def test_ip_str_to_arr(self):
        self.assertEqual(libNetwork.ip_str_to_arr("10.139.36.108"), ["10", "139", "36", "108"])

    def test_ip_str_to_num(self):
        self.assertEqual(libNetwork.ip_str_to_num("10.139.36.108"), 176890988)

    def test_ip_str_compare(self):
        self.assertEqual(libNetwork.ip_str_compare("10.139.36.108", "10.136.128.56"), 1)

    def test_ip_num_compare(self):
        self.assertEqual(libNetwork.ip_num_compare(176890988, 176717880), 1)

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestLibNetwork())
        return self.suite

if __name__ == "__main__":
    unittest.main()