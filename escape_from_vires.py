#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywaves
import requests

WITHDRAW_ASSET = 'USDC' # asset to withdraw
MAX_WITHDRAW = 1000 # max withdraw amount allowed in usd
FEE_ASSET = 'WAVES' # asset to pay fee with
SEED = 'your seed here' # your wallet seed

MARKETS = {
	'USDC': {'address': '6XtHjpXbs9RRJP2Sr9GUyVqzACcby9TkThHXnjVC5CDJ', 'market': '3PGCkrHBxFMi7tz1xqnxgBpeNvn5E4M4g8S', 'decimals': 6},
	'USDT': {'address': '34N9YcEETLWn93qYQ64EsP1x89tSruJU44RrEMSXXEPJ', 'market': '3PEiD1zJWTMZNWSCyzhvBw9pxxAWeEwaghR', 'decimals': 6},
	'USDN': {'address': 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p', 'market': '3PCwFXSq8vj8iKitA5zrrLRbuqehfmimpce', 'decimals': 6},
	'BTC': {'address': '8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS', 'market': '3PA7QMFyHMtHeP66SUQnwCgwKQHKpCyXWwd', 'decimals': 8},
	'ETH': {'address': '474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu', 'market': '3PPdeWwrzaxqgr6BuReoF3sWfxW8SYv743D', 'decimals': 8},
	'WAVES': {'address': None, 'market': '3P8G747fnB1DTQ4d5uD114vjAaeezCW4FaM', 'decimals': 8},
	'EURN': {'address': 'DUk2YTxhRoAqMJLus4G2b3fR8hMHVh6eiyFx5r29VR6t', 'market': '3PBjqiMwwag72VWUtHNnVrxTBrNK8D7bVcN', 'decimals': 6}
}

DAPP_ADDRESS = '3PAZv9tgK1PX7dKR7b4kchq5qdpUS3G5sYT' # vires dapp

session = requests.session()
wallet = pywaves.Address(seed=SEED)

while True:
	try:
		r = session.get('https://api.vires.finance/markets')
		data = r.json()
	except KeyboardInterrupt:
		break
	except:
		continue

	for market in MARKETS:
		supply = int(data[MARKETS[market]['market']]['supply']) / 10**MARKETS[market]['decimals']
		borrow = int(data[MARKETS[market]['market']]['borrow']) / 10**MARKETS[market]['decimals']
		liquidity = supply - borrow

		if market == WITHDRAW_ASSET and liquidity > MAX_WITHDRAW:

			tx = wallet.invokeScript(
				dappAddress = DAPP_ADDRESS,
				functionName = 'withdraw',
				params = [{"type":"string","value":MARKETS[market]['address']},{"type":"integer","value":int(MAX_WITHDRAW*10**MARKETS[market]['decimals'])}],
				payments = [],
				feeAsset = MARKETS[FEE_ASSET]['address']
			)

			if 'error' in tx:
				print("\033[91mWithdraw failed: ", tx, end='\033[0m')
			else:
				print("\033[92mWithdraw executed successfully: ", tx, end='\033[0m')
