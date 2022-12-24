from .base import TaskVerifier, TaskVerifyException
from ..onchain import OnChainVerify

class OnChainVerifier(TaskVerifier):
    def __init__(self):
        super().__init__()

    def handle_verify(self, **kwargs) -> bool:
        onchain = OnChainVerify()
        if kwargs['type'] == 20:
            result = onchain.get_sol_balance(kwargs['public_key'])
            if result >= kwargs['require_balance']:
                return True
            return False
        if kwargs['type'] == 21:
            result = onchain.get_token_balance(public_key=kwargs['public_key'],token_address=kwargs['token_address'])
            if result >= kwargs['require_token_balance']:
                return True
            return False
            
        

