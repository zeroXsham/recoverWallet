from web3 import Web3
from eth_account import Account
import time

# Record the start time
start_time = time.time()

# Enable unstable API
Account.enable_unaudited_hdwallet_features()

# REPLACE with your words
recovery_words = ['word1', 'UNKNOWN', 'word3',  'word4',  'word5',  'word6', 'word7',  'word8',  'word9',  'word10',  'word11',  'word12']
# REPLACE with your wallet address
wallet_address = '0xc41e0aBa3d182cAE96e1F7DBe043B58860254833'
word_list = []


# Read in words from text file
with open('wordlist.txt', 'r') as file:
    word_list = [line.strip() for line in file if line.strip()]

# Brute force all the words
for word in word_list:

    try:
        recovery_words[1] = word

        # Derive the private key from the recovery words
        private_key = Account.from_mnemonic(" ".join(recovery_words)).key.hex()

        # Use web3.py to derive the public address from the private key
        web3 = Web3()
        account = web3.eth.account.from_key(private_key)
        
        if wallet_address == account.address:
            print(f'The missing word was: {word}')
            break
    except:
        continue


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print("Elapsed Time:", elapsed_time, "seconds")
