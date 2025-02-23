import CloudFlare


old_ip="178.32.51.118"
new_ip="0.0.0.0"
new_ttl=60
email=""
apikey=""

cf = CloudFlare.CloudFlare(email,apikey)

for zone in cf.get_zones():
    print(zone["name"])
    for record in cf.get_all_records_by_domain(zone["name"]):
        record_name=record["name"]
        record_type=record["type"]
        record_content=record["content"]
        record_ttl=record["ttl"]
        record_id=record["id"]
        if (old_ip in record_content):
            new_content=record_content.replace(old_ip,new_ip)
            cf.update_record(zone["name"],record_name,record_type,new_content, new_ttl)
            print("old -> {} {} {} {}".format(record_name,record_type,record_content, record_ttl))
            print("new -> {} {} {} {}".format(record_name,record_type,new_content, new_ttl))

