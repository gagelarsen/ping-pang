<div align="center">

# Ping Pang

Ping a URL and output the status code and latency. Save to a log or CSV on an interval.

[![Build Status](https://travis-ci.com/Justintime50/ping-pang.svg?branch=master)](https://travis-ci.com/Justintime50/ping-pang)
[![Pypi](https://img.shields.io/pypi/v/ping-pang)](https://pypi.org/project/ping-pang)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

I got tired of my internet underperforming and wanted to start correlating data across the span of a day to see what was up. Using this script, you can do just that by pinging a URL on an interval (recommended for short periods) or setting this script up on a cronjob (for long periods) and saving the output to a CSV where you can then builds graphs and charts to view your data. 

It should be noted that Ping does not actually ping but instead does a GET request to the specified URL. This means that responses will appear a bit slower than simply pinging the same URL on the command line.

## Install

```bash
pip3 install ping-pang
```

## Usage

```
Usage:
    ping --url http://google.com --log ~/test.log --csv ~/test.csv --interval 10

Options
    -h, --help                  Show this help message and exit
    -u, --url URL               The URL you would like to ping.
    -i, --interval INTERVAL     The interval to ping the URL again (in seconds). Great to test over a period of time (maxes out to 1000 pings).
    -l, --log LOG               The path to save the output to a log. Will not save to log if flag is not present.
    -c, --csv CSV               The path to save the output to a CSV file. Great to build data that can be manipulated easily.
```

## Development

```bash
pip3 install -e ."[dev]"

pylint pingpang/*.py
```
