import os
import json

filepath = 'JOB_2/schema_avro.json'
with open(filepath, 'r') as f:
    file: str = f.read()
    json_file: list = json.loads(file)

    print(type(json_file))

    print(json_file)