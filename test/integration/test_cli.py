import mock
import sys
from pingpang import ping_logic


def test_cli_good_url():
    # TODO: This test isn't complete. Just an example.
    test_args = [ping_logic.__file__, '-u', 'https://google.com']
    with mock.patch.object(sys, 'argv', test_args):
        ping_logic.run_script('__main__')
        # TODO: Figure out how to verify this.


def test_cli_bad_url():
    # TODO: Test this case.
    assert False


def test_cli_no_interval():
    # TODO: Test this case.
    assert False


def test_cli_interval():
    # TODO: Test this case.
    assert False


def test_cli_no_log_file():
    # TODO: Test this case.
    assert False


def test_cli_log_file():
    # TODO: Test this case.
    assert False


def test_cli_no_csv_file():
    # TODO: Test this case.
    assert False


def test_cli_csv_file():
    # TODO: Test this case.
    assert False
