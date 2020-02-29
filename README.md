# Cloudflare DynDns Updater

## Description
This tool transofrms a traditional DNS record into a DynamicDNS record. Once started, the tool checks if the value of the specified record matches the current external ip of the network. If the ip address does not match the tool will update it.

## Installation

```
git clone https://github.com/aleksandarstojkovski/cloudflare_dyndns_updater/
```

## Usage

```
Usage: python3 main.py -e <EMAIL> -ak <API_KEY> -d <DOMAIN> -r <DNS_RECORD> -rt <RECORD_TYPE> -i <INTERVAL>

      -e  cloudflare email address
      -ak cloudFlare apikey
      -d  domain name to be updated eg. test.com
      -r  record to be updated eg. myrecord.test.com
      -rt record type eg. A
      -i  check interval in seconds (minimum is 10s)
```

## Donations

Donate: <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QF3RUSYRD5XBE&source=url">PayPal</a>
