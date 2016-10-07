#!/usr/bin/env python

import dropbox
import ConfigParser
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

config = ConfigParser.ConfigParser()
config.readfp(open(os.path.expanduser('~/.dropbox_key.ini')))

dbx = dropbox.Dropbox(config.get('main','key'))

shared_links = dbx.sharing_get_shared_links()

shared_link_settings = dropbox.sharing.SharedLinkSettings(expires = datetime.today()+ relativedelta(months=1))

for i in shared_links.links:
    #sharedlink = dbx.sharing_get_shared_link_metadata(i.url)
    print i.url
    if i.expires == None:
      print "link does not expire"
      # Comment this in if you want to set link expiry date
      #dbx.sharing_modify_shared_link_settings(i.url,shared_link_settings)
    #Comment this in if you want to remove link
    #dbx.sharing_revoke_shared_link(i.url)
