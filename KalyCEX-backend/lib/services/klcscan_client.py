import logging

import requests
from django.conf import settings

from core.consts.currencies import KRC20_CURRENCIES
from core.currency import Currency
from lib.services.etherscan_client import EtherscanClient

log = logging.getLogger(__name__)


class KLCscanClient(EtherscanClient):
    def __init__(self):
        self.url = 'https://api.kalyscan.io/api?'

    def _make_request(self, uri=''):
        res = {}
        try:
            res = requests.get(
                f'{self.url}{uri}&apikey={settings.KLCSCAN_KEY}')
            res = res.json()
        except Exception as e:
            log.exception('Can\'t fetch data from blockchain.info')
        return res

    def get_token_params(self, currency_code):
        return KRC20_CURRENCIES.get(Currency.get(currency_code))
