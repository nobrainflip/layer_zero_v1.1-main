WAIT_TIME = range(1, 2) # Pause vefore next bot action
MIN_STABLE_FOUND = 0.3 # Minimum amount of stables to be on wallet, that is checked before the swap
NFT_CA = '0x12b241a59b27ce77e5c28abe16eaf4b6909e60c7'
NFT_FEE = 0.0005
ARBITRUM_NODE = 'https://arbitrum.llamarpc.com'

# All activities
NO_ACTIVITY       = 'NO ACTIVITY'
STARGATE          = 'STARGATE'
STARGATE_LIQ      = 'STARGATE_LIQ'
STARGATE_STG      = 'STARGATE_STG'
BTC_BRIDGE        = 'BTC_BRIDGE'
TESTNET_BRIDGE    = 'TESTNET_BRIDGE'
APTOS_BRIDGE      = 'APTOS_BRIDGE'
SWAP_TOKEN        = 'SWAP_TOKEN'
HARMONY_BRIDGE    = 'HARMONY_BRIDGE'
MINT_NFT_2_ME     = 'mint_nft2me'

# Activities, that should be always checked
ACTIVITY_LIST = [
    STARGATE_LIQ,
    STARGATE_STG,
    BTC_BRIDGE,
    TESTNET_BRIDGE,
    SWAP_TOKEN,
    APTOS_BRIDGE,
    HARMONY_BRIDGE,
]

# Chain that could be used to send using STARGATE
STARGATE_CHAIN_LIST = [
    'Avalanche',
    'Polygon',
    'BSC',
    'Arbitrum',
    'Optimism',
    # 'BASE'
]

headers = { "Authorization": "Bearer [ВАШ API-КЛЮЧ БЕЗ ЭТИХ СКОБОК ВОКРУГ!]", "accept": "application/json" } # API вашего 1inch для свапов получать его здесь - https://portal.1inch.dev/dashboard