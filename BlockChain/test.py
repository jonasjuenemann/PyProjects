from BlockchainClass import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain =  Blockchain()

my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = "fake_transactions"
my_blockchain.print_blocks()
my_blockchain.validate_chain()

new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]

# import sha256
from hashlib import sha256

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0
# creating the proof
"""string = str(nonce) + str(new_transactions)
proof = sha256(string.encode()).hexdigest()
# printing proof
print(proof)"""

"""# finding a proof that has 2 leading zeros
test = False
while not test:
    string = str(nonce) + str(new_transactions)
    proof = sha256(string.encode()).hexdigest()
    needed_zeros = True
    for i in range(difficulty):
        if proof[i] != "0":
            #print("Index " + str(i) + " ist nicht 0!")
            needed_zeros = False
            break
    if needed_zeros == True:
        test = True
        print(nonce)
        print(proof)
    nonce = nonce + 1"""
