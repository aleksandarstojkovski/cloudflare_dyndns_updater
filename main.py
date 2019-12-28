import argparse
import CloudFlare
import sys

if __name__== "__main__":
  
  parser = argparse.ArgumentParser("Dynamic DNS using Cloudflare!")
  parser.add_argument("-e", type=str, help="CloudFlare email address", required=True,  dest='email')
  parser.add_argument("-ak", type=str, help="CloudFlare ApiKey", required=True, dest='apikey')
  parser.add_argument("-d", type=str, help="Domain name to be updated eg. test.com", required=True, dest='domain')
  parser.add_argument("-r", type=str, help="Record to be updated eg. myrecord.test.com", required=True, dest='record')
  parser.add_argument("-rt", type=str, help="Record type eg. A", required=True, dest='rtype')
  parser.add_argument("-i", type=int, help="Check interval in seconds eg. 10", required=True, dest='interval')

  try:
    args = parser.parse_args()
  except:
    parser.print_help
    sys.exit(1)

  print("Starting ddns update...")

  cf = CloudFlare.CloudFlare(args.email,args.apikey)
  cf.start_dyndns(args.domain,args.record,args.rtype,args.interval)
