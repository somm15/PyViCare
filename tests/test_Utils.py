import unittest
from datetime import timedelta

from PyViCare.PyViCareUtils import ViCareTimer
class UtilTests(unittest.TestCase):

    def test_parse_timespan(self):
        self.assertEqual(timedelta(hours=2, minutes=4), ViCareTimer.parse_time_as_delta("02:04"))
        self.assertEqual(timedelta(hours=24, minutes=0), ViCareTimer.parse_time_as_delta("24:00"))
