<div align="center">

# Ping Pang

Ping a URL and output the status code and latency. Save to a log or CSV on an interval.

[![Build Status](https://travis-ci.com/Justintime50/ping-pang.svg?branch=master)](https://travis-ci.com/Justintime50/ping-pang)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/ping-pang/badge.svg?branch=master)](https://coveralls.io/github/Justintime50/ping-pang?branch=master)
[![PyPi](https://img.shields.io/pypi/v/ping-pang)](https://pypi.org/project/ping-pang)
[![Licence](https://img.shields.io/github/license/justintime50/ping-pang)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

I got tired of my internet underperforming and wanted to start correlating data across the span of a day to see what was up. Using this script, you can do just that by pinging a URL on an interval (recommended for short periods) or setting this script up on a cronjob (for long periods) and saving the output to a CSV where you can then builds graphs and charts to view your data. 

It should be noted that Ping Pang does not actually ping but instead does a GET request to the specified URL. This means that responses will appear a bit slower than simply pinging the same URL on the command line.

Ping Pang maxes out at `1000` pings in any given run of this tool.

## Install

```bash
# Install tool
pip3 install ping-pang

# Install locally
make install

# Get Makefile help
make help
```

## Usage

```
Usage:
    ping-pang --url https://www.google.com --log ~/test.log --csv ~/test.csv --interval 10

Options
    -h, --help            show this help message and exit
    -u URL, --url URL     The URL you would like to ping.
    -i INTERVAL, --interval INTERVAL
                            The interval to ping the URL again (in seconds). Great to test over a period of time (maxes out to 1000 pings).
    -l LOG_FILE, --log_file LOG_FILE
                            The path to save the output to a log. Will not save to log if flag is not present.
    -c CSV_FILE, --csv_file CSV_FILE
                            The path to save the output to a CSV file. Great to build data that can be manipulated easily.
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run the tool locally
venv/bin/python pingpang/ping_logic.py --help
```
