domains = ['.com', '.net', '.co', '.org']
with open('/home/manish/domains.txt', 'a') as o:
    output = set()
    for _ in open('/home/manish/custom_block_urls.txt', 'r').readlines():
        if not _.startswith('#'):
            if _.startswith('address='):
                o.write(_)
            else:
                _ = _.strip()
                output.add("address=/"+_+"/0.0.0.0"+'\n')
                #for tld in domains:
                #    parts = _.split('.')
                #    string = '.'.join(parts[0:-1])
                #    output.add("address=/"+string+tld+"/0.0.0.0"+'\n')
    for _ in output:
        o.write(_)
