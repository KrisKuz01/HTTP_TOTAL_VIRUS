import pyshark
import csv
import requests

# Path to the .pcap file
pcap_file = 'WIRESHARK.pcap'

# Specify the path to TShark
pyshark.tshark.tshark.get_process_path = lambda: r"C:\Program Files\Wireshark\tshark.exe"

# Create a capture object and load the .pcap file
capture = pyshark.FileCapture(pcap_file)

# List to store extracted URLs
urls = []

# Iterate over each packet in the capture
for packet in capture:
    # Check if the packet has an HTTP layer
    if 'http' in packet:
        # Extract the URL from the HTTP layer if host and request_uri are available
        host = packet.http.get_field_value('host')
        request_uri = packet.http.get_field_value('request_uri')
        if host and request_uri:
            url = host + request_uri
            urls.append(url)

# Close the capture file
capture.close()

# Total Virus API endpoint
total_virus_api_endpoint = 'https://totalvirus.com/api/v1/scan'

# Function to scan a URL using the Total Virus API
def scan_url(url):
    params = {'url': url}
    response = requests.get(total_virus_api_endpoint, params=params)
    if response.status_code == 200:
        result = response.json()
        if 'malicious' in result and result['malicious']:
            return 'Malicious'
    return 'Clean'

# Write URLs to a CSV file
csv_file = 'urls.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Total Virus Detection'])  # Write header
    for url in urls:
        detection_result = scan_url(url)
        writer.writerow([url, detection_result])  # Write URL and detection result

print(f"URLs extracted and saved to {csv_file}.")
