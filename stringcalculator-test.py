import unittest
from unittest.mock import patch
from stringcalculator import add
from stringcalculator import NegativesUnsupported

class TestStringCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(''), 0)
        self.assertEqual(add('2'), 2)
        self.assertEqual(add('1,2'), 3)
        self.assertEqual(add('1,3,9,6'), 19)
        self.assertEqual(add('1,4,7,9,8,10,11,23'),72)
        self.assertEqual(add('1,2\n3'),6)
        self.assertEqual(add('2,1\n6,7\n10'), 26)
        self.assertEqual(add('//;\n1;2'),3)
        self.assertEqual(add('//,\n1,2,7,8'),18)
        self.assertEqual(add('//.\n1.2.7.8'),18)
        self.assertRaises(NegativesUnsupported,add,'-1,1,2,-2')
        self.assertRaises(NegativesUnsupported,add,'//.\n-1.-2.7.-8')

    @patch('stringcalculator.logging')
    def test_add_result_logs_info(self, mock_logging):
        add('1,2')
        self.assertTrue(mock_logging.info.called)

    @patch('stringcalculator.logging')
    @patch('stringcalculator.requests')
    def test_add_send_get_to_server_when_logging_exception_occurs(self, mock_requests, mock_logging):
        mock_logging.info.side_effect = Exception('Boom !')
        add('1,2')
        self.assertTrue(mock_requests.get.called)


if __name__ == '__main__':
    unittest.main()