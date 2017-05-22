# Importing os
import os
# Function to get the domain information
def get_whois( url ):
    command = "whois " + url # whois commnad
    process = os.popen( command )# open the process
    results = str( process.read() )# convert to string
    # Returning the information
    print("whois done!")
    return results
