import libConfig
import unittest


class TestLibConfig(unittest.TestCase):
    def test_args_conf(self):
        conf = libConfig.args_conf("a=1&b=2")
        self.assertEqual(conf.get("a"), "1")
        self.assertEqual(conf.get("b"), "2")

    def test_ini_file_conf(self):
        conf = libConfig.ini_file_conf("../test.ini")
        self.assertEqual(conf.get("a"), "1")
        self.assertEqual(conf.get("b"), "2")

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestLibConfig())
        return self.suite

if __name__ == "__main__":
    unittest.main()