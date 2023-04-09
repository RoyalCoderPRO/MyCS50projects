import requests
import sys

n = sys.argv[1]
    try:
        assert float(sys.argv[1])
    except:
        sys.exit('Invalid Input')