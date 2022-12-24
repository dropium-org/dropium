from solana.rpc.api import Client
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.publickey import PublicKey
from solana.rpc.types import TokenAccountOpts
import base64
import struct
import base58
import requests
import json

METADATA_PROGRAM_ID = PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s')

class OnChainVerify():
    def get_sol_balance(self,public_key):
        solana_client = Client("https://api.devnet.solana.com")
        # a = solana_client.get_token_accounts_by_owner(public,opts=TokenAccountOpts(program_id=TOKEN_PROGRAM_ID,encoding='jsonParsed'))
        a = solana_client.get_balance(PublicKey(public_key))
        return a

    def get_token_balance(self,public_key,token_address):
        url = 'https://api.mainnet-beta.solana.com'

        headers= {"Content-Type": "application/json"}
        data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountsByOwner",
        "params": [
        f"{public_key}",
        {
            "mint": f"{token_address}"
        },
        {
            "encoding": "jsonParsed"
        }]
    }
        r = requests.post(url=url,headers=headers,json=data)
        return (json.loads(r.text)['result']['value'][0]['account']['data']['parsed']['info']['tokenAmount']['uiAmount'])
# a = solana_client.get_account_info(public)
# print(a['result']['value']['data'][0])
# result = get_metadata(client=solana_client,mint_key='5yPGvUz6JWKjkViGwTCpygJii1rP2xv5yx146ULtBiYq')
# print(result)
# result = get_metadata(client=solana_client,mint_key='EeBpeuRxkAQWyvGfS3LbpqzR1v8KfB2KvRPDQCPCqZNp')
# print(result)
# with open('test.txt','w') as w:
#     w.write(str(a))
