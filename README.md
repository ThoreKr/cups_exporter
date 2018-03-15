# Prometheus CUPS Exporter

This exporter provides prometheus metrics for cups by utilizing pycups.

By default it will register on Port 9329 as registered in the [Prometheus Wiki](https://github.com/prometheus/prometheus/wiki/Default-port-allocations)

```
usage: cups-exporter.py [-h] [--cups-host CUPS_HOST] [--cups-port CUPS_PORT]
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

```
# HELP cups_printer_status Status about printer alerts
# TYPE cups_printer_status gauge
cups_printer_status{printer="My-Printer",status="Happy"} 1.0
# HELP cups_print_jobs Number of current print jobs
# TYPE cups_print_jobs gauge
cups_print_jobs 0.0
# HELP cups_up CUPS up
# TYPE cups_up gauge
cups_up 1.0
# HELP cups_printers Number of printers
# TYPE cups_printers gauge
cups_printers 10.0
```
