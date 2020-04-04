curl --silent -o /home/manish/hostnames.txt https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt
curl --silent -o /home/manish/domains.txt https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt
cat /tmp/dnsmasq.log >> /home/manish/dnslogs
echo >  /tmp/dnsmasq.log
sudo python /home/manish/match_regex.py
sudo python /home/manish/custom_blocking.py
grep "forward" /home/manish/dnslogs | grep "[^ ]\+ to 127.0.0.53" -o | sed -e 's/ to 127.0.0.53//g' | sort| uniq >> /home/manish/dns_requests ; sort /home/manish/dns_requests| uniq > /home/manish/dns_requests1 ; mv /home/manish/dns_requests1 /home/manish/dns_requests
python /home/manish/analytics.py
sudo service dnsmasq stop
sudo service dnsmasq start
