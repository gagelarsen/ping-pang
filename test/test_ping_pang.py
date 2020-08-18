import unittest
import unittest.mock
from datetime import datetime
from pingpang import ping_logic


class TestPing(unittest.TestCase):
    def test_generate_log(self):
        """Generate a log file with content
        """
        content = """2020-08-15 23:12:38.433752
URL: http://www.google.com
Status Code: 200
Latency (ms): 102.69
"""
        mock_open = unittest.mock.mock_open(read_data=content)
        with unittest.mock.patch('builtins.open', mock_open):
            result = ping_logic.PingPang.generate_log('file.log', content)
        assert content == result

    def test_ping(self):
        """Ping a URL and receive a response
        """
        # TODO: Mock this HTTP call instead as this
        # requires an active internet connection to pass
        url = 'http://www.google.com'
        result = ping_logic.PingPang.ping(url)
        assert isinstance(result[1], datetime)
        assert result[2] == url
        assert result[3] == 200
        assert isinstance(result[4], float)

    def test_run(self):
        """Run the tool
        """
        # TODO: Mock this HTTP call instead as this
        # requires an active internet connection to pass
        url = 'http://www.google.com'
        interval = None
        log_file = None
        csv_file = None
        result = ping_logic.PingPang.run(url, interval, log_file, csv_file)
        assert isinstance(result[1], datetime)
        assert result[2] == url
        assert result[3] == 200
        assert isinstance(result[4], float)

    def test_generate_csv(self):
        """Generate a CSV file with content
        """
        # TODO: Mock generating a real CSV and inserting this content there
        timestamp = '2020-08-15 23:12:38.433752'
        url = 'http://www.google.com'
        status_code = 200
        latency = 102.69
        content = f'{timestamp}, {url}, {status_code}, {latency}'
        mock_open = unittest.mock.mock_open(read_data=content)
        with unittest.mock.patch('builtins.open', mock_open):
            result = ping_logic.PingPang.generate_csv(
                'test.csv', timestamp, url, status_code, latency)
        assert timestamp in result[0]
        assert url in result[0]
        assert status_code in result[0]
        assert latency in result[0]


if __name__ == '__main__':
    unittest.main()
