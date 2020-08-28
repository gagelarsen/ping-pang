import time
from datetime import datetime
import csv
import argparse
import requests
import logging


class PingPangCLI():
    def __init__(self):
        """
        Setup CLI args and init the program.
        """
        parser = argparse.ArgumentParser(
            description='Ping a URL and get back data.'
        )
        parser.add_argument(
            '-u',
            '--url',
            required=True,
            type=str,
            help='The URL you would like to ping.'
        )
        parser.add_argument(
            '-i',
            '--interval',
            required=False,
            default=None,
            type=int,
            help=('The interval to ping the URL again (in seconds).'
                  ' Great to test over a period of time'
                  ' (maxes out to 1000 pings).')
        )
        parser.add_argument(
            '-l',
            '--log_file',
            required=False,
            type=str,
            default=None,
            help=('The path to save the output to a log.'
                  ' Will not save to log if flag is not present.')
        )
        parser.add_argument(
            '-c',
            '--csv_file',
            required=False,
            type=str,
            default=None,
            help=('The path to save the output to a CSV file.'
                  ' Great to build data that can be manipulated easily.')
        )
        parser.parse_args(namespace=self)
        logging.basicConfig(level=logging.INFO)

    def run(self):
        PingPang.run(
            url=self.url,
            interval=self.interval,
            log_file=self.log_file,
            csv_file=self.csv_file,
        )


class PingPang():
    @classmethod
    def run(cls, url, interval=None, max_runs=1000, log_file=None, csv_file=None):
        """
        Run the script that pings a URL

        Args:
            url (str): The url that you want to ping.
            interval (int): The amount of time in between requests.
            max_runs (int): The maximum number of repeat requests.
            log_file (str): Path to a file to log info.
            csv_file (str): Path to a file to log statistical info.
        """
        count = 0
        ping = None
        while count < max_runs:
            ping = cls.ping(url)
            if log_file:
                cls.generate_log(log_file, ping[0])
            if csv_file:
                cls.generate_csv(
                    csv_file, ping[1], ping[2], ping[3], ping[4]
                )
            count += 1
            if interval is None:
                break
            time.sleep(interval)

        return ping

    @classmethod
    def ping(cls, url):
        """
        Ping a URL and return the output.

        Args:
            url (str): The url to ping.

        Returns:
            # TODO: Explain the return.
        """
        current_time = datetime.now()
        start_time = time.perf_counter()
        ping = requests.get(url)
        end_time = time.perf_counter() - start_time
        latency = round(end_time * 1000, 2)

        output = (
            f'\n{current_time}\nURL: {url}\n'
            f'Status Code: {ping.status_code}\n'
            f'Latency (ms): {latency}\n'
        )
        logging.debug(f'Ping made to {url}.')
        print(output)

        return output, current_time, url, ping.status_code, latency

    @ classmethod
    def generate_log(cls, log_file, output):
        """
        Save the output to a log by appending the data.

        Args:
            log_file: Path to the log file.
            output: The data to be written to the log file.
            # TODO: Consider adding a flag for append vs. new file?

        Returns:
            The output?  # TODO: Probably don't need to return this... Since you are already passing it in.
        """
        with open(log_file, 'a') as log_file:
            log_file.write(output)
            logging.debug(f'Data written to {log_file}.')

        return output

    @ classmethod
    def generate_csv(cls, csv_file, current_time, url, status_code, latency):
        """
        Save the output to a CSV and format correctly.

        Args:
            csv_file (str): Path to csv file.
            current_time: The current time.
            url (str): URL being pinged.
            status_code: The status code returned by the request.
            latency:

        Returns:
            # TODO: Explain the return.. does it need to be returned?
        """
        row = [[current_time, url, status_code, latency], ]

        with open(csv_file, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(row)
            logging.debug(f'Data written to {csv_file}.')

        return row


# Did it this way so you get the effect you want with main, but makes
# It easier for testing.
def run_script(name):
    if name == "__main__":
        PingPangCLI().run()


run_script(__name__)
