


```
import json 
import pandas as pd 

def lambda_handler(event, context):
    print(pd.__version__)
    pd.show_versions()
    return {
        'statusCode':200,
        'body':json.dumps('Hello from Lambda!')
    }
    

```
