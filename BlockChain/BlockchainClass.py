from Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)
        return self.chain

        # prints contents of blockchain

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()

    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_block_hash)
        # modify this method
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Blockchain has been tempered with, no good!")
                return False
            if previous.hash != previous.generate_hash():
                print("Blockchain is invalid!")
                return False
            return True

    def proof_of_work(self, block, difficulty=2):
        test = False
        while not test:
            proof = block.generate_hash()
            needed_zeros = True
            for i in range(difficulty):
                if proof[i] != "0":
                    needed_zeros = False
                    break
            if needed_zeros:
                test = True
                print(block.nonce)
                block.nonce = 0
            block.nonce = block.nonce + 1
        return proof

    """ eleganter:
    def proof_of_work(self,block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof"""
