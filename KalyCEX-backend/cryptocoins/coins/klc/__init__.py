from cryptocoins.coins.klc.connection import get_w3_connection
from cryptocoins.coins.klc.wallet import klc_wallet_creation_wrapper
from cryptocoins.coins.klc.wallet import is_valid_klc_address
from cryptocoins.utils.register import register_coin


KLC = 3
CODE = 'KLC'
DECIMALS = 8

KLC_CURRENCY = register_coin(
    currency_id=KLC,
    currency_code=CODE,
    address_validation_fn=is_valid_klc_address,
    wallet_creation_fn=klc_wallet_creation_wrapper,
    latest_block_fn=lambda currency: get_w3_connection().eth.get_block_number(),
    blocks_diff_alert=100,
)