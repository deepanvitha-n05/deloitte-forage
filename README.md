# Deloitte Forage IIoT Telemetry Project

This project standardizes two different IIoT telemetry data formats into a unified format.

## Objective
Convert telemetry data from two different JSON formats into a single consistent structure.

## Features
- Handles multiple input formats
- Converts ISO timestamps to milliseconds since epoch
- Outputs data in a unified JSON format

## Files
- main.py → contains conversion logic
- data-1.json → input format 1
- data-2.json → input format 2
- data-result.json → expected output format

##  How to Run
python main.py
