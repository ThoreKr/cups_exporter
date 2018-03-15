#!/usr/bin/env python3
import cups
import json
import time
from prometheus_client import start_http_server, Gauge
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--cups-host", help="The cups host to connect to", default="localhost")
parser.add_argument("--cups-port", type=int, help="The cups port to use", default=631)
parser.add_argument("--cups-user", help="The user to connect with", default="default")
args = parser.parse_args()


# Define Metrics
printJobsNum = Gauge('cups_print_jobs', 'Number of current print jobs')
printersNum = Gauge('cups_printers', 'Number of printers')
printersStatus = Gauge('cups_printer_status', 'Status about printer alerts', ['printer', 'status'])
dhcpUp = Gauge('cups_up', 'CUPS up')


#@printersNum
def getPrinterData(conn):
  printers = conn.getPrinters()
  printersNum.set(len(printers))
  return printers

#@printJobsNum
def getJobData(conn):
  jobs = conn.getJobs()
  printJobsNum.set(len(jobs))

#@printersStatus
def getPrinterStatus(printers):
  for key, value in printers.items():
    if value['printer-state-reasons'][0] != 'none':
      printersStatus.labels(printer=value['printer-make-and-model'], status=value['printer-state-reasons'][0]).set(0)
    else:
      printersStatus.labels(printer=value['printer-make-and-model'], status='happy').set(1)


if __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(8000)

  cups.setServer(args.cups_host)
  cups.setPort(args.cups_port)
  cups.setUser(args.cups_user)

  while True:
    try:
      conn = cups.Connection()
      printers = getPrinterData(conn)
      getJobData(conn)
      getPrinterStatus(printers)
      dhcpUp.set(1)
    except Exception as e:
      dhcpUp.set(0)
      print(e)

    time.sleep(5)
