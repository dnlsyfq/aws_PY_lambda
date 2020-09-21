
# Python

## WINDOWS Setup
```
mkdir environment
cd environment
py -m venv env
cd env
.\Scripts\activate
pip install pymysql
cd lib/site-packages
```

## MAC Setup
```
mkdir environment
cd environment
python3 -m venv env
source ./bin/activate
cd env
pip3 install numpy 
cd lib/python3.7/site-packages
zip -r zip.zip .
```

---

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
