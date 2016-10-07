# Clean up dropbox links

## Setting up

This script requires python dropbox and python-dateutil modules, you can
install them with pip

    pip install python-dateutil dropbox

## Configuration

Generate key for your key for app so:
1. Go to [Dropbox developer portal app console](https://www.dropbox.com/developers/apps),
   create an app. Name is not important, i used cleanuplinks
2. From App settings, section Oauth2, Generate access token
3. Write this key to ~/.dropbox_key.ini file which should look like this:

```
[main]
key = THISISYOURSECRETKEY
```

