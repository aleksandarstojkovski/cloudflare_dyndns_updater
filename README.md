# Cloudflare DynDns Updater

## Description
TODO

## Installation

```
git clone https://github.com/aleksandarstojkovski/cloudflare_dyndns_updater/
```

## Usage

```
Usage: python3 main.py -e <EMAIL> -ak <API_KEY> -d <DOMAIN> -r <DNS_RECORD> -rt <RECORD_TYPE> -i INTERVAL 

      -b backup path, must exist, must be writable by zimbra user
      -r restore path, must exist, must be readable by zimbra user
```

### Backup Zimbra

`
./zimbroski.sh -b <BACKUP_PATH>
`

### Restore Zimbra

`
./zimbroski.sh -r <RESTORE_PATH>
`

## Test

The tool has been successfully tested on the following Zimbra versions:

```
8.8.X
8.7.X
8.6.X
8.5.X
```

## Donations

Donate: <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QF3RUSYRD5XBE&source=url">PayPal</a>
