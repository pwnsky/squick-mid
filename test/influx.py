import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random

token = "ul3roTgSnu-peh5XQnOia0R-A0y31zwjN-AE9cHpG-w7vZh-yAzgF7v6zNiPY5zVcjAVU3uRWsMHHrsmO3hTqw=="
org = "pwnsky"
url = "http://192.168.54.162:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="grafana"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(1000):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", random.randint(1, 256))
    )
    write_api.write(bucket=bucket, org="pwnsky", record=point)
    time.sleep(1) # separate points by 1 second

query_api = write_client.query_api()
query = """from(bucket: "grafana")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="pwnsky")

for table in tables:
    for record in table.records:
        print(record)
print("ok")