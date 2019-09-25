# Prometheus CUPS Exporter

This exporter provides prometheus metrics for cups by utilizing pycups.

By default it will register on Port 9329 as registered in the [Prometheus Wiki](https://github.com/prometheus/prometheus/wiki/Default-port-allocations)

```text
usage: cups_exporter.py [-h] [--cups-host CUPS_HOST] [--cups-port CUPS_PORT]
                        [--cups-user CUPS_USER] [--listen-port LISTEN_PORT]

optional arguments:
  -h, --help            show this help message and exit
  --cups-host CUPS_HOST
                        The cups host to connect to (default: localhost)
  --cups-port CUPS_PORT
                        The cups port to use (default: 631)
  --cups-user CUPS_USER
                        The user to connect with (default: default)
  --listen-port LISTEN_PORT
                        The port the exporter will listen on (default: 9329)
```

The metrics exported are:

```text
# HELP cups_print_jobs_active Number of current print jobs
# TYPE cups_print_jobs_active gauge
cups_print_jobs_active 0.0
# HELP cups_print_jobs_total Total number of print jobs
# TYPE cups_print_jobs_total counter
cups_print_jobs_total 1000.0
# HELP cups_printers Number of printers
# TYPE cups_printers gauge
cups_printers 20.0
# HELP cups_printer_status_info Status about printer alerts
# TYPE cups_printer_status_info gauge
cups_printer_status_info{model="Good Printers Inc. Printer",printer="My-Printer",status="happy"} 1.0
# HELP cups_up CUPS status
# TYPE cups_up gauge
cups_up 1.0
# HELP cups_scrape_duration_seconds Amount of time each scrape takes
# TYPE cups_scrape_duration_seconds gauge
cups_scrape_duration_seconds 0.04441666603088379
```
