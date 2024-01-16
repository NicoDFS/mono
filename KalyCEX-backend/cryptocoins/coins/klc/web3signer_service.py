import requests
import json

class Web3SignerService:
    def __init__(self):
        self.base_url = "http://localhost:9000"

    def sign_transaction(self, from_address, to_address, gas, gas_price, value):
        method = "eth_signTransaction"
        transaction_data = {
            "from": from_address,
            "to": to_address,
            "gas": gas,
            "gasPrice": gas_price,
            "value": value
        }
        params = [transaction_data]
        response = self.send_json_rpc_request(method, params)
        
        if 'result' in response:
            return response['result']
        else:
            raise Exception(f"Failed to sign transaction: {response}")