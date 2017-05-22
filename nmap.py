# Importing os
import os
# Function to get Nmap Port Scan
def get_nmap ( options, ip ):
    command = "nmap " + options + " " + ip # run nmp with options and the ip
    process = os.popen( command )#open process
    results = str( process.read() )# make it string
    # Returning the final result
    print("Nmap Scan done!")
    return results
