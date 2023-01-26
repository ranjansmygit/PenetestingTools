#!/bin/bash

# Define the Nessus and Defender scan servers
nessus_server="nessus.example.com"
defender_server="defender.example.com"

# Get the list of devices from Nessus
nessus_devices=`nessus-fetch --list-hosts --server $nessus_server`

# Get the list of devices from Defender
defender_devices=`defender-fetch --list-hosts --server $defender_server`

# Compare the two lists and store the devices only in Nessus
only_nessus_devices=`comm -23 <(echo "$nessus_devices") <(echo "$defender_devices")`

# Loop through the list of devices only in Nessus
for device in $only_nessus_devices; do
  # Perform a scan on the device using Nessus
  nessus-scan --server $nessus_server --target $device
done
