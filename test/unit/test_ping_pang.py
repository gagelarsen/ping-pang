import mock
from datetime import datetime
from pingpang import ping_logic


def _mock_response(
        status=200,
        content="CONTENT",
        json_data=None,
        raise_for_status=None):
    """
    since we typically test a bunch of different
    requests calls for a service, we are going to do
    a lot of mock responses, so its usually a good idea
    to have a helper function that builds these things
    """
    mock_resp = mock.Mock()
    # mock raise_for_status call w/optional error
    mock_resp.raise_for_status = mock.Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status
    # set status code and content
    mock_resp.status_code = status
    mock_resp.content = content
    # add json data if provided
    if json_data:
        mock_resp.json = mock.Mock(
            return_value=json_data
        )
    return mock_resp


def test_ping():
    """
    Test pinging a URL and receive a response
    """
    # TODO: Mock this HTTP call instead as this
    # requires an active internet connection to pass
    url = 'http://www.google.com'
    result = ping_logic.PingPang.ping(url)
    assert isinstance(result[1], datetime)
    assert result[2] == url
    assert result[3] == 200
    assert isinstance(result[4], float)


def test_ping_bad_url():
    """
    Test pinging a bad URL and receive a response
    """
    # TODO: Test this case.
    assert False


def test_run():
    """
    Test running the tool
    """
    # TODO: Mock this HTTP call instead as this
    # requires an active internet connection to pass
    url = 'https://www.google.com'
    interval = None
    log_file = 'test.log'
    csv_file = 'test.csv'
    mock_open = mock.mock.mock_open(read_data=url)
    with mock.mock.patch('builtins.open', mock_open):
        result = ping_logic.PingPang.run(url=url, interval=interval, log_file=log_file, csv_file=csv_file)
    assert isinstance(result[1], datetime)
    assert result[2] == url
    assert result[3] == 200
    assert isinstance(result[4], float)


@mock.patch('time.sleep', return_value=None)
@mock.patch('requests.get', return_value=_mock_response(status=200))
def test_run_on_interval(mock_sleep, mock_get):
    """
    Test running the tool with a set interval
    """
    # TODO: Mock this HTTP call instead as this
    # requires an active internet connection to pass
    url = 'https://www.google.com'
    interval = 1
    log_file = 'test.log'
    csv_file = 'test.csv'
    mock_open = mock.mock.mock_open(read_data=url)
    with mock.mock.patch('builtins.open', mock_open):
        result = ping_logic.PingPang.run(url=url, interval=interval, log_file=log_file, csv_file=csv_file)
    assert isinstance(result[1], datetime)
    assert result[2] == url
    assert result[3] == 200
    assert isinstance(result[4], float)
    assert mock_get.call_count == 1000


def test_generate_csv():
    """
    Test generating a CSV file with content
    """
    # TODO: Mock generating a real CSV and inserting this content there
    timestamp = '2020-08-15 23:12:38.433752'
    url = 'https://www.google.com'
    status_code = 200
    latency = 102.69
    content = f'{timestamp}, {url}, {status_code}, {latency}'
    mock_open = mock.mock.mock_open(read_data=content)
    with mock.mock.patch('builtins.open', mock_open):
        result = ping_logic.PingPang.generate_csv(
            'test.csv', timestamp, url, status_code, latency)
    assert timestamp in result[0]
    assert url in result[0]
    assert status_code in result[0]
    assert latency in result[0]


def test_unable_to_open_csv_file():
    """
    Test generating a CSV file with content when you can't open the specified csv file
    """
    # TODO: Test this case.
    assert False


def test_generate_log():
    """
    Test generating a log file with content
    """
    content = """2020-08-15 23:12:38.433752
    URL: http://www.google.com
    Status Code: 200
    Latency (ms): 102.69
    """
    mock_open = mock.mock.mock_open(read_data=content)
    with mock.mock.patch('builtins.open', mock_open):
        result = ping_logic.PingPang.generate_log('file.log', content)
    assert content == result


def test_unable_to_open_log_file():
    """
    Test generating a log file with content where you are unable to open the log file
    """
    # TODO: Test this case.
    assert False
