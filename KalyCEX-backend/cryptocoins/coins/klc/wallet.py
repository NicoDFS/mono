from django.db import transaction
from web3signer_service import Web3SignerService
from aws_kms_service import AwsKmsService
from core.models.cryptocoins import UserWallet

class TransactionController:
    def __init__(self, web3signer_url):
        self.web3signer_service = Web3SignerService(web3signer_url)

    def create_transaction(self, transaction, key_id):
        from_address = transaction['from']
        to_address = transaction['to']
        gas = transaction['gas']
        gas_price = transaction['gasPrice']
        value = transaction['value']
        signed_transaction = self.web3signer_service.sign_transaction(from_address, to_address, gas, gas_price, value, key_id)
        # Use the signed_transaction to send the transaction

    @transaction.atomic
    def get_or_create_klc_wallet(self, user_id, is_new=False):
        klc_wallet = UserWallet.objects.filter(
            user_id=user_id,
            currency='KLC',
            blockchain_currency='KLC',
        ).first()

        if not is_new and klc_wallet is not None:
            return klc_wallet

        aws_kms_service = AwsKmsService()
        key_id = aws_kms_service.create_new_key()
        # Use the key_id to create a new KLC wallet
        # Return the wallet

    def is_valid_klc_address(self, address):
        # Implement KLC address validation logic here
        pass

    def klc_wallet_creation_wrapper(self, user_id, is_new=False):
        wallet = self.get_or_create_klc_wallet(user_id, is_new=is_new)
        return UserWallet.objects.filter(id=wallet.id)
    
    @transaction.atomic
    def create_krc20_address(self, user_id, token_name, is_new=False):
        krc20_wallet = UserWallet.objects.filter(
            user_id=user_id,
            currency=token_name,
            blockchain_currency='KLC',
        ).first()

        if not is_new and krc20_wallet is not None:
            return krc20_wallet

        aws_kms_service = AwsKmsService()
        key_id = aws_kms_service.create_new_key()
        # Use the key_id to create a new KRC20 wallet
        # Return the wallet

    def is_valid_krc20_address(self, address, token_name):
        # Implement KRC20 address validation logic here
        pass