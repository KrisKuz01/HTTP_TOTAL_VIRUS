# URL Scanner using Total Virus API

THIS WILL ONLY DETECT HTTP URLS

This script extracts URLs from a Wireshark `.pcap` file and scans them for malicious content using the Total Virus API. It utilizes the `pyshark` library to parse the `.pcap` file and the `requests` library to interact with the Total Virus API.

## Prerequisites

Before running the script, ensure that you have the following prerequisites installed:

- Python 3.x
- `pyshark` library (`pip install pyshark`)
- `requests` library (`pip install requests`)

You also need to have Wireshark installed on your system and the path to `tshark` properly set in the script.

## Usage

1. Place the Wireshark `.pcap` file you want to scan in the same directory as the script.

2. Update the `pcap_file` variable in the script with the name of your `.pcap` file.

3. If necessary, update the `pyshark.tshark.tshark.get_process_path` line to match the correct path to your `tshark` executable.

4. Run the script using the command: python run.py


5. After the script finishes running, it will generate a `urls.csv` file in the same directory. This file will contain the extracted URLs and their detection results.

## Notes

- The script checks each packet in the `.pcap` file for an HTTP layer. If an HTTP layer is present, it extracts the URL from the host and request_uri fields.

- The script sends GET requests to the Total Virus API endpoint (`https://totalvirus.com/api/v1/scan`) with each extracted URL as a parameter.

- The Total Virus API endpoint used in the script does not require an API key for access.

- If a URL is detected as malicious by the Total Virus API, it is marked as "Malicious" in the `urls.csv` file. Otherwise, it is marked as "Clean".

- The script requires an active internet connection to communicate with the Total Virus API.

## Limitations

- This script solely relies on the Total Virus API for scanning URLs. It does not perform any local analysis or checks for malicious content.

- The effectiveness and accuracy of the scanning process depend on the Total Virus API's capabilities and reliability.

- The script assumes that the Wireshark `.pcap` file provided contains HTTP traffic with URLs to be scanned.

- The URLs extracted from the `.pcap` file are concatenated without further validation. It is recommended to exercise caution when using the extracted URLs.

