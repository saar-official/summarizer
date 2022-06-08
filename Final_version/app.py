import json
import time
import numpy as np
import datetime 
import string
from main_model import Main_model

def lambda_handler(event, context):
    model = Main_model()
    try:
    	text = event['text']
    except:
    	body = json.loads(event)
    	text = body["text"]
    final = {}
    timestamp = time.strftime(str(datetime.datetime.now()))
    final[timestamp] = model.return_response(text)
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predictions": str(final)
            }
        )
    }
    
