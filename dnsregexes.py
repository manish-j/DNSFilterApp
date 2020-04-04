all_but_dot = "[^\.]*"
all_ = ".*"

def a(x):
    return all_ + x + all_

regexes=[ 
#"^clients.\.google\.com$",
"idmb-app" + all_ + "\.ap-south-1\.elb\.amazonaws\.com",
a("xiaomi"),
a("\.apple\."),
a("apple-dns"),
a("facebook"),
a("\.suibyuming\."),
a("\.camscanner\."),
a("\.intsig\."),
a("openinstall\.io\."),
a("\.mi\."),
a("\.runtastic\."),
a("\.qxwz\."),
a("\.emarsys\."),
a("\.miniclippt\."),
a("mtalk\."),
a("firebaseremoteconfig"),
a("update\.google"),
a("apidata\.google"),
a("android\."),
a("ampproject"),
a("adblockplus"),
a("cognito"),
a("^id\."),
a("^id\."),
a("\.id\."),
a("history\."),
a("monitor"),
a("track"),
a("trak"),
a("apple-cloudkit\.com"),
a("\.mapmyindia\."),
a("^fb\."),
a("\.fb\."),
a("\.icloud\."),
a("\.izatcloud\."),
a("quora"),
a("taboola"),
a("outbrain"),
a("licdn"),
a("inmobi"),
"^[^\.]*$".
]

