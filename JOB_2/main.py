from flask import Flask, request
from fastavro import writer, parse_schema
import json
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_endpoint():
    data: dict = request.get_json()   
    
    filepath: str = data['raw_dir'] + '/file.json'
    with open(filepath, 'r') as f:
        file: str = f.read()                                     # Reading JSON file
        json_file: list = json.loads(file)

        schema: dict
        schema_filepath = 'JOB_2/schema_avro.json'
        with open(schema_filepath, 'r') as sf:
            s_file: str = sf.read()
            schema = json.loads(s_file)

        parsed_schema = parse_schema(schema)

        if not os.path.exists(data['stg_dir']):             # Creating dir if don`t exist`
            os.makedirs(data['stg_dir'])

        write_filepath: str = data['stg_dir'] + '/file.avro'
        with open(write_filepath, 'wb') as out:             # Writing *.avro file
            writer(out, parsed_schema, json_file)

    return 'Job2 completed!'


if __name__ == '__main__':
    app.run(port=8082)