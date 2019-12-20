import json
import requests
import time
import random

class CloudFlare:

  email = ''
  apikey = ''
  headers = None
  api_url = 'https://api.cloudflare.com/client/v4/zones'

  def __init__(self, email, api_key):
    self.email=email
    self.apikey=api_key
    self.headers={
      'X-Auth-Key': api_key,
      'X-Auth-Email': email,
      'Content-Type': 'application/json'
    }

  def get_zones(self) -> dict:
    zones = json.loads(requests.get(self.api_url,headers=self.headers).text)
    return zones['result']

  def get_zone_id(self,domain_name) -> dict:
    zone_id = ''
    for zone in self.get_zones():
      if zone['name'] == domain_name:
        zone_id=zone['id']
    return zone_id

  def get_all_records_by_domain(self,domain_name) -> dict:
    zone_id = self.get_zone_id(domain_name)
    data = {
      'name': domain_name 
    }
    url = self.api_url + '/' + zone_id + '/dns_records' 
    return_value = json.loads(requests.get(url, headers=self.headers, data=data).text)
    return return_value['result']
  
  def get_record_id(self,domain_name,record_name,record_type) -> int:
    record_id = ''
    for record in self.get_all_records_by_domain(domain_name):
      if record['name'] == record_name and record['type'] == record_type:
        record_id=record['id']
    return  record_id  

  def update_record(self,domain_name,record_name,record_type,content,ttl=int(1),proxied=bool(False)) -> dict:
    zone_id = self.get_zone_id(domain_name)
    record_id = self.get_record_id(domain_name,record_name,record_type)
    data = {
      'type': record_type,
      'name': record_name,
      'content': content,
      'ttl': ttl,
      'proxied': proxied
    }
    url = self.api_url + '/' + zone_id + '/dns_records/' + record_id 
    return_value = json.loads(requests.put(url, headers=self.headers, json=data).text)
    return return_value

  def get_record_value(self,domain_name,record_name,record_type) -> dict:
    zone_id = self.get_zone_id(domain_name)
    record_id = self.get_record_id(domain_name,record_name,record_type)
    url = self.api_url + '/' + zone_id + '/dns_records/' + record_id
    return_value = json.loads(requests.get(url, headers=self.headers).text)
    return return_value['result']['content']
    
  def get_public_ip(self) -> str:
    ip = ''
    urls = ['https://api.ipify.org?format=json','https://jsonip.com','https://ifconfig.co/json']
    for i in range(10):
      url = random.choice(urls)
      response = requests.get(url)
      if response.ok: break
    if response.ok:
      json_response = json.loads(response.text)
      ip = json_response['ip']
    return ip

  def start_dyndns(self,domain_name,record_name,record_type,ttl=int(1),proxied=bool(False)):
    while(True):
      public_ip = self.get_public_ip()
      record_content = self.get_record_value(domain_name,record_name,record_type)
      if public_ip != record_content:
        self.update_record(domain_name,record_name,record_type,public_ip)
        print("Record updated from: "+record_content+ " to "+public_ip)
      time.sleep(5)
