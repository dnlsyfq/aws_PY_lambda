
# Python

## WINDOWS Setup - Zip
```
mkdir environment
cd environment
py -m venv env
cd env
.\Scripts\activate
pip install pymysql
cd lib/site-packages
```

## WINDOWS WSL Setup - Zip
```
ubuntu1804
cd /mnt/c
sudo apt update
sudo apt-get upgrade
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
sudo apt install python3-pip
python3.8 -m pip install --system --target ./ pandas
sudo python3.8 -m pip install --system --target ./ pandas

```

## WINDOWS WSL Setup - Layers
```
ubuntu1804
cd /mnt/c
mkdir -p build/python/lib/python3.6/site-packages
pip3 install requests -t  build/python/lib/python3.6/site-packages --system
sudo pip3 install pandas -t build/python/lib/python3.6/site-packages --system
pip3 install numpy -t build/python/lib/python3.6/site-packages --system
cd build
zip python

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
