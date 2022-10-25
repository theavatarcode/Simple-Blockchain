from blockchain import Blockchain

block = Blockchain()

print(block.chain[0]['index'], block.chain[0]['proof'], block.chain[0]['previous_hash'])
