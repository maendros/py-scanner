# Importing urllib.request  downloads files from the internet
import urllib.request
# Importing io for encoding
import io
# Function to get robots.txt file
def get_robots_txt( url ):
    if url.endswith( '/' ):
        path = url #leave it as it is
    else:
        path = url + "/"
    req = urllib.request.urlopen( path + "robots.txt", data = None ) #get the file robots.txt
    data = io.TextIOWrapper( req, encoding = 'utf­8' )# data encoded properly
    print("Robots.txt done!")
    return data.read()
