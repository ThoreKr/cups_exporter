# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- [#7](https://github.com/ThoreKr/cups_exporter/issues/6) Fix a bug where incomplete responses were returned if the list of print jobs was empty.
- [#7](https://github.com/ThoreKr/cups_exporter/issues/7) Do not keep a persistent connection to cups to survive cups restarts.

## [1.0.0] - 2019-09-25

### Added

- Gather on scrape time
- Added `cups_scrape_duration_seconds` metric
- Add Pipfile for dependency management

### Changed

- Renamed some metrics to adhere to naming conventions
  - `cups_printer_status` -> `cups_printer_status_info`
  - `cups_print_jobs` -> `cups_print_jobs_total`
