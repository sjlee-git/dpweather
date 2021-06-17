import datetime
import logging
import azure.functions as func
import json
import time
from . import run

def main(mytimer: func.TimerRequest, tablePath: func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    tags = run.naver();
    data = {
        "Temp": tags[0],
        "Weather": tags[1],
        "Weather2": tags[2],
        "Lowest": tags[3],
        "Highest": tags[4],
        "Finedust": tags[5],
        "PartitionKey": "weather_check",
        "RowKey": int(time.time()-99999999999)
    }

    tablePath.set(json.dumps(data))