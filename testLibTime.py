import libTime
import unittest
import pytz
import time
import datetime


class TestLibTime(unittest.TestCase):
    def test_get_timezone(self):
        self.assertEqual(libTime.get_timezone(), pytz.timezone('Asia/Shanghai'))

    def test_simple_format_detect(self):
        self.assertEqual(libTime.simple_format_detect("230.2.2"), "unknown")
        self.assertEqual(libTime.simple_format_detect("2015-12-23"), "%Y-%m-%d")
        self.assertEqual(libTime.simple_format_detect("20151223"), "%Y%m%d")
        self.assertEqual(libTime.simple_format_detect("12:12:23"), "%H:%M:%S")
        self.assertEqual(libTime.simple_format_detect("12:12"), "unknown")
        self.assertEqual(libTime.simple_format_detect("121223"), "unknown")
        self.assertEqual(libTime.simple_format_detect("1212"), "unknown")
        self.assertEqual(libTime.simple_format_detect("12:12:23:23"), "unknown")
        self.assertEqual(libTime.simple_format_detect("2015-12-23 12:12:23"), "%Y-%m-%d %H:%M:%S")
        self.assertEqual(libTime.simple_format_detect("201512"), "unknown")

    def test_str_to_timestamp(self):
        self.assertEqual(libTime.str_to_timestamp("20151203"), 1449072000)

    def test_str_to_datetime(self):
        self.assertEqual(libTime.str_to_datetime("20151203"), datetime.datetime.strptime("20151203", "%Y%m%d"))

    def test_str_to_time(self):
        self.assertEqual(libTime.str_to_time("20151203"), time.strptime("20151203", "%Y%m%d"))

    def test_timestamp_to_datetime(self):
        self.assertEqual(libTime.timestamp_to_datetime(1449072000), datetime.datetime.strptime("20151203", "%Y%m%d"))

    def test_str_convert_by_defined(self):
        self.assertEqual(libTime.str_convert_by_defined("20151203", "%Y-%m"), "2015-12")

    def test_str_to_dateflag(self):
        self.assertEqual(libTime.str_to_dateflag("20151203 12:12:23"), "20151203")

    def test_str_to_dateint(self):
        self.assertEqual(libTime.str_to_dateint("20151203 12:12:23"), "2015-12-03")

    def test_str_to_datetimeflag(self):
        self.assertEqual(libTime.str_to_datetimeflag("20151203 12:12:23"), "201512031212")

    def test_str_to_fulldatetime(self):
        self.assertEqual(libTime.str_to_fulldatetime("20151203 12:12:23"), "2015-12-03 12:12:23")

    def test_str_to_timeflag(self):
        self.assertEqual(libTime.str_to_timeflag("20151203 12:12:23"), "1212")

    def test_str_to_timeonly(self):
        self.assertEqual(libTime.str_to_timeonly("20151203 12:12:23"), "12:12:23")

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestLibTime())
        return self.suite

if __name__ == "__main__":
    unittest.main()