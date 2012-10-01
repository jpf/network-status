import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from avg import simple_average, cumulative_average, windowed_average

class avgTest(unittest.TestCase):
    elements = [1, 1, 2, 3, 5, 8, 13]

    # def test_true(self):
    #     self.assertEquals(True, True)

    # def test_state_not_persisted(self):
    #     gform = GForm('dG02c3hqdEZBaWZMN1NBdnBCZkVzdWc6MQ')
    #     self.assertIn('SmsSid', gform.labels)
    #     self.assertNotIn('One', gform.labels)
    #     gform = GForm('dHk3N2M5NlAtZV9mMlAyOEU5VE05dEE6MQ')
    #     self.assertNotIn('SmsSid', gform.labels)
    #     self.assertIn('One', gform.labels)

    def test_simple_average(self):
        average = simple_average()
        rv = 0
        for element in self.elements:
            rv = average.calculate(element)
        self.assertEquals(rv, 4.714285714285714)

    def test_simple_average_has_count(self):
        count = 10
        average = simple_average()
        for element in range(0,count):
            average.calculate(element)
        self.assertEquals(average.count, count)

    def test_cumulative_average(self):
        average = cumulative_average()
        rv = 0
        for element in self.elements:
            rv = average.calculate(element)
        self.assertEquals(rv, 4.714285714285714)

    def test_cumulative_average_has_count(self):
        count = 10
        average = cumulative_average()
        for element in range(0,count):
            average.calculate(element)
        self.assertEquals(average.count, count)

    def test_windowed_average(self):
        average = windowed_average(len(self.elements))
        rv = 0
        for element in self.elements:
            rv = average.calculate(element)
        self.assertEquals(rv, 4.714285714285714)

    def test_windowed_average_has_count(self):
        count = 10
        average = windowed_average()
        for element in range(0,count):
            average.calculate(element)
        self.assertEquals(average.count, count)

    def test_windowed_average_uses_correct_length(self):
        tests = [(1, 1), (1, 1), (4, 2), (6, 3.0), (1, 2.6), (3, 2.6666666666666665), (6, 3.142857142857143)]
        average = windowed_average()
        for (element, expected) in tests:
            rv = average.calculate(element)
            self.assertEquals(rv, expected)
            

