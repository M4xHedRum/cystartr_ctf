#dirtyscript
import requests
from time import sleep

def find_match():
   """
   Iterates through every block from block 0 until
   block with at least one transaction is spotted 
   """
   headers = {'Content-Type': 'application/json'}
   
   # Infura has a 100,000 requests limit per day for free accounts
   # Endpoint allows multi-call, limit isn't explicitly stated for it
   # Playing safe by making 100 queries per request
   for req_no in range(0, 100000, 100):
      print(req_no)
      # List to contain 100 query
      data = []
      
      # Create 100 queries for every request
      for query in range(0,100):
         json_data = {'jsonrpc': '2.0',
            'method': 'eth_getBlockByNumber',
            # API only receives hex value as parameter
            'params': [hex(req_no + query),False],
         'id': 1,
         }
         # Append to list
         data.append(json_data)
      # Send the request
      response = requests.post('', headers=headers, json=data)

      # Appease the rate-limit gods 
      sleep(0.2)
   
      if response.status_code == 200:
         for resp in response.json():
            # If any of the blocks has a transaction
            # Return the request number and query number
            if len(resp["result"]["transactions"]) > 0:
               rez = response.json()
               return (req_no + rez.index(resp))
            print(resp["result"]["transactions"])
      else:
         # If response code isn't 200, must be error
         print(req_no) 
         print(response.text)
         exit(1)
         
if __name__ == "__main__":
   oldest_block = find_match()
   print(f"Oldest block on Goerli with non-zero transaction is {oldest_block}")

# 5644 was the first block with non zero transactions on Goerli
