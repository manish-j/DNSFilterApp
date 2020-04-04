import re
import dnsregexes
pf = "/home/manish/"
added = set([ _.strip() for _ in open(pf + 'block_urls.txt', 'r').readlines()])
for _ in open(pf + 'dnslogs','r').readlines():
	if ' to ' in _:
		_ = _.strip()
		_ = re.sub(r'^.*( [^ ]+ to [^ ]+)$',r'\1',_).strip()
		_ = _.split()[0].strip()
		for regex in dnsregexes.regexes:
			if re.search(r''+regex, _, re.IGNORECASE) is not None:
				if _ not in added:
					added.add(_)

with open(pf  + 'custom_block_urls.txt', 'w') as block_file:
    for _ in added:
	block_file.write(_+'\n')
