"""Import modules"""
import time
from datetime import datetime
import csv
import argparse
from threading import Thread
import requests


class Ping():
    """Ping a URL and get back data.
    """

    def __init__(self):
        """Setup CLI args and init the program.
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
            type=int,
            help="""The interval to ping the URL again (in seconds).
                Great to test over a period of time (maxes out to 1000 pings)."""
        )
        parser.add_argument(
            '-l',
            '--log',
            help="""The path to save the output to a log.
                Will not save to log if flag is not present."""
        )
        parser.add_argument(
            '-c',
            '--csv',
            help="""The path to save the output to a CSV file.
                Great to build data that can be manipulated easily."""
        )
        self.args = parser.parse_args()

    def ping(self):
        """Ping a URL and return the output.
        """
        url = self.args.url
        current_time = datetime.now()
        start_time = time.perf_counter()
        ping = requests.get(url)
        end_time = time.perf_counter() - start_time
        latency = round(end_time * 1000, 2)

        output = f"""\n{current_time}\nURL: {self.args.url}\n
            Status Code: {ping.status_code}\nLatency (ms): {latency}\n"""
        print(output)
        return output, current_time, url, ping.status_code, latency

    def interval(self):  # pylint: disable=R0201
        """Run the Ping program over an interval by starting a new thread for each iteration.
        """
        Thread(target=Ping.run).start()

    def log(self, output):
        """Save the output to a log by appending the data.
        """
        with open(self.args.log, 'a') as log:
            log.write(output)

    def csv(self, current_time, url, status_code, latency):
        """Save the output to a CSV and format correctly.
        """
        row = [[current_time, url, status_code, latency], ]

        with open(self.args.csv, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(row)

    def run(self):
        """Run the script that pings a URL
        """
        if self.args.interval:
            count = 0
            while count < 1000:
                ping = self.ping()
                if self.args.log:
                    self.log(ping[0])
                if self.args.csv:
                    self.csv(ping[1], ping[2], ping[3], ping[4])
                count += 1
                time.sleep(self.args.interval)
        else:
            ping = self.ping()
            if self.args.log:
                self.log(ping)


def main():
    """Run the main program
    """
    Ping().run()


if __name__ == "__main__":
    main()
