count = {}
count_domain = {}
import os
command = "grep \"forward\" /home/manish/dnslogs | grep \"[^ ]\+ to 127.0.0.53\" -o | sed -e \'s/ to 127.0.0.53//g\' > /home/manish/dns_log_requests"
os.system(command)
for _ in open('/home/manish/dns_log_requests', 'r').readlines():
    _ = _.strip()

    if _ not in count:
        count[_] = 0
    count[_] += 1
    
    domain = _.split('.')[-2:]
    domain = '.'.join(domain)

    if domain not in count_domain:
        count_domain[domain] = 0
    count_domain[domain] += 1
    
count_domain = sorted(count_domain.items(), key = lambda(x) : x[1], reverse = True)
print(count_domain)
