import os
import requests
import json
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


def requester(date: str, page: int) -> requests.models.Response:                              # Returning GET Response
    prms: dict = {'date': date, 'page': page}
    response = requests.get(os.getenv('API_URL'), params=prms, headers={'Authorization': os.getenv('AUTH_KEY')})
    return response


@app.route('/', methods=['POST'])
def post_endpoint():
    data = request.get_json()

    page_num: int = 1
    res_json: list = []
    while True:
        resp: requests.models.Response = requester(data['date'], page_num)        # Writing all pages from GET query to res_json

        if resp.status_code != requests.codes.ok:       # Checking on last page
            break
        
        res_json = res_json + json.loads(resp.text)
        page_num = page_num + 1
    

    if not os.path.exists(data['raw_dir']):             # Creating dir if don`t exist`
        os.makedirs(data['raw_dir'])

    filepath: str = data['raw_dir'] + '/file.json'
    with open(filepath, 'w') as f:                      # Writing *.json file
        json.dump(res_json, f)

    return 'Job1 completed!'


if __name__ == '__main__':
    app.run(port=8081)