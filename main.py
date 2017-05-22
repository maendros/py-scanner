from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'results'
create_dir ( ROOT_DIR )
#call all the functions
print("Scan Done111111!!")
def gather_info( name, url ):
    print("Scan Done!!")
    robots_txt = get_robots_txt ( url )
    domain_name = get_domain_name ( url )
    whois = get_whois ( domain_name )
    ip_address = get_ip_address ( domain_name )
    nmap = get_nmap ("­F", ip_address )#
    create_report( name, url, domain_name, nmap, robots_txt, whois )#create report of them

def create_report( name, url, domain_name, nmap, robots_txt, whois ):
    project_dir = ROOT_DIR + "/" + name
    create_dir( project_dir )
    write_file( project_dir + "/full_url.txt", url )
    write_file( project_dir + "/domain_name.txt", domain_name )
    write_file( project_dir + "/nmap.txt", nmap )
    write_file( project_dir + "/robots.txt", robots_txt )
    write_file( project_dir + "/whois.txt", whois )

    print("Scan Done!!")
gather_info("athinorama","http://www.athinorama.gr/")
