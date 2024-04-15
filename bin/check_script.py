import os
import time
import requests

from dotenv import load_dotenv
load_dotenv()


BASE_DIR = os.getenv("BASE_DIR")

JOB1_PORT = 8081
JOB2_PORT = 8082

rep_date = "2022-08-11"

RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", rep_date)
STG_DIR = os.path.join(BASE_DIR, "stg", "sales", rep_date)

def run_job1():
    print(f"Starting job1. Date: {rep_date}")
    resp = requests.post(
        url=f'http://localhost:{JOB1_PORT}/',
        json={
            "date": rep_date,
            "raw_dir": RAW_DIR
        }
    )

    assert resp.status_code == 200
    print(f"job1 completed. Date: {rep_date}")


def run_job2():
    print(f"Starting job2. Date: {rep_date}")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": RAW_DIR,
            "stg_dir": STG_DIR
        }
    )
    assert resp.status_code == 200
    print(f"job2 completed. Date: {rep_date}")


if __name__ == '__main__':
    run_job1()
    time.sleep(3)
    run_job2()