from tld import get_tld
#import top level domain lib
# Function to get the top level domain
def get_domain_name ( url ):
    #url as argument  and get the url
    domain_name = get_tld(url)
    print("Domain name done!")
    return domain_name#return it
