# LayerZero customazible Software

## What the script does:

- Bridges all available USDT/USDC from any network to any network (except ETH, FTM).
- Buys STG on POLYGON and stakes them.
- Buys BTC on AVALANCHE, bridges them through btcbridge to POLYGON, bridges them back, and sells them.
- Swaps ETH to ARBITRUM or OPTIMISM on GoerliETH through https://testnetbridge.com/, one way.
- Bridges USDT to Aptos through https://theaptosbridge.com/bridge, one way.
- Bridges USDT to Harmony through https://bridge.harmony.one/erc20, one way.
- Dilutes transaction activities with approvals in different networks.
- Dilutes transaction activities with swaps in different networks.
- Works in multi-threaded mode.
- Chooses random wallets and performs activities in a random order.
- Records general logs of all actions and separately for each wallet.

# Preparation for Use

### main_config.py

WAIT_TIME = range(5, 10) - delay between actions, in minutes.
RATIO_STARGATE_SINGLE = 0.5 - percentage of the USDT/USDC balance that will be used for bridging from single networks (1 = 100%, 0.5 = 50%)
STARGATE_CHAIN_LIST - list of non-single networks.

### max_setting.csv

Table with commission settings (in bucks)
Activity - activity
MAX_GAS - maximum transaction fee (gas)
MAX_VALUE - maximum value for Stargate

### RPCs.py

Fill in with your own or public RPCs.

Free private RPCs:

https://www.alchemy.com/
https://www.quicknode.com/

### data.csv

The heart of the script! Pay special attention to filling out this table.
Use a period (".") as the decimal separator in all decimal numbers (e.g., 17.89), not a comma.

DO - whether to run this wallet. To start the script processing it, write "X" in English. Without "X," it doesn't matter which activities are selected below. After completing all selected wallet activities, "X" will change to "DONE."
Name - wallet name (necessary for logs).
Wallet - wallet address in an EVM network.
Private_key - private key for the wallet.
Proxy - field for a proxy. Currently not working, leave it empty.
Stargate - the total number of bridges through Stargate after running the script, do not change anything, it's for your reporting purposes. Initially = 0.
Stargate_range - amount range - how much USDT/USDC to buy.
STARGATE_FIRST_SWAP - specify "DONE" if buying USDT/USDC in non-single networks is not required (assuming that there are stablecoins on one of the networks for processing). If purchasing stablecoins is necessary, leave it empty.
STARGATE_POLYGON/AVALANCHE - how many bridges to make from this network through StarGate. Initially 0. IMPORTANT! It should be 0, not an empty field, otherwise it will throw an error.
STARGATE_BSC - similar to STARGATE_POLYGON/AVALANCHE, but for BSC.
STARGATE_BSC_RANGE - value, how much to buy USDT/USDC in BSC, similar to STARGATE_RANGE.
STARGATE_BSC_FIRST_SWAP - similar to STARGATE_FIRST_SWAP, but for BSC.
STARGATE_ARBITRUM - similar to STARGATE_POLYGON/AVALANCHE, but for ARBITRUM.
STARGATE_ARBITRUM_RANGE - similar to STARGATE_POLYGON/AVALANCHE, but for ARBITRUM.
STARGATE_ARBITRUM_FIRST_SWAP - similar to STARGATE_FIRST_SWAP, but for ARBITRUM.
STARGATE_LIQ - adding liquidity, currently not working.
STARGATE_LIQ_VALUE - how much liquidity to add to Stargate, currently not working.
STARGATE_STG - whether to buy and stake STG. The module works on POLYGON.
STARGATE_STG_RANGE - amount range in $, range of how much STG to buy for staking.
BTC_BRIDGE - how many bridges to make from AVALANCHE to POLYGON and back with BTC.b buying and selling. IMPORTANT! It should be 0, not an empty field, otherwise it will throw an error.
BTC_BRIDGE_RANGE - in which range to buy BTC.b in $ equivalent for processing.
BTC_BRIDGE_STEP - stages of BTC_BRIDGE, do not touch. Initially empty. With each stage, an "X" will appear, indicating which stage the script is at:
One X - bought BTC.b. Two X - bridged BTC.b from Avalanche to Polygon. Three X - bridged BTC.b from Polygon to Avalanche. Empty field - the script completed the BTC.b sale and subtracted 1 (one) from the BTC_BRIDGE column.
TESTNET_BRIDGE - how many times to swap ETH to GETH through testnetbridge.
TESTNET_BRIDGE_RANGE - range to buy GETH in $ equivalent.
TESTNET_BRIDGE_CHAINS - which networks to use in testnetbridge. Choose randomly and write with capital letters, separated by commas.
APTOS_BRIDGE - how many times to bridge USDT from BSC to APTOS.
APTOS_BRIDGE_RANGE - in which range to buy USDT/USDC.
APTOS_BRIDGE_WALLET - Unique Aptos wallet to which USDT will be bridged. (Generate it on Cointool for convenience).
HARMONY_BRIDGE - how many times to bridge USDT from BSC to HARMONY.
HARMONY_BRIDGE_RANGE - in which range to buy USDT/USDC for bridging.
SWAP_TOKEN - random swaps to confuse activity detection algorithms. (Optional)
SWAP_TOKEN_RANGE - in which range to swap random tokens. (Optional)
SWAP_TOKEN_CHAINS - in which networks to perform random swaps. (Optional)
APPROVE_DO - whether to perform random token approvals for your wallet. Similar to token swaps, but cheaper. If yes, write "X."
APPROVE - log - number of approvals, do not change anything, it's for your reporting purposes. Initially = 0.
APPROVE_CHAINS - in which networks to perform approvals.
APPROVE_TIMES - random number of approvals to perform between activities.

### Logs

Text files with logs for specific wallets will appear in the log_wallet folder. This is necessary for convenient tracking of possible bugs and errors.
The log.csv file contains the complete log of activities. If "True" is written at the end of a row, it means that the activity was completed successfully. If "False" is written, it means that the activity ended with an error. The encountered error will also be indicated in the cell with "False"
The main.txt file duplicates the log from the command line / IDE. In log_wallet, it's the same, but with breakdowns by wallets.

### Notes

In case an error occurs during the script's execution, the script will continue to the next activity until it completes all selected activities and only those activities remain that it cannot execute (insufficient funds, pool issues, etc.). All errors can be viewed in the logs.

Try not to stop the script during execution. If you must stop it without waiting for the completion of an activity, wait for the message "Launching in..." and then stop the script with the Ctrl+Pause Break key combination. Otherwise, you will need to figure out at which stage you stopped the script and edit data.csv

Built by @sybil-v-zakone