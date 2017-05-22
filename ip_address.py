# Importing os
import os
# Method to get the IP Address
def get_ip_address ( url ):
    command = "nslookup " + url # command to get the tld
    #command = "host " + url # command to get the tld
    process = os.popen( command )
    results = str( process.read() ) #read process make it string
    marker = results.find( 'Addresses:' )  # search adresses and get the ip
    #marker = results.find( 'Has adresses:' )  # search adresses and get the ip

    print("IP Address done!")
    return results[marker:].splitlines()[0]# return results  only top line because it can have multiple addresses

print(get_ip_address("cnn.gr"))
