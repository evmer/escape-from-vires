# escape-from-vires
Withdraw liquidity from Vires Finance as soon as somebody make a new deposit

## Dependences
`pip3 install requests pywaves`

## Edit fields
```
WITHDRAW_ASSET = 'USDC' # asset to withdraw  
MAX_WITHDRAW = 1000 # max withdraw amount allowed in usd  
FEE_ASSET = 'WAVES' # asset to pay fee with  
SEED = 'your seed here' # your wallet seed
```
## Run
`python3 escape_from_vires.py`
