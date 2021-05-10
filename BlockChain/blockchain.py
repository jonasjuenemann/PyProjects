transaction1 = {
    'amount': '30',
    'sender': 'Alice',
    'receiver': 'Bob'}
transaction2 = {
    'amount': '200',
    'sender': 'Bob',
    'receiver': 'Alice'}
transaction3 = {
    'amount': '300',
    'sender': 'Alice',
    'receiver': 'Timothy'}
transaction4 = {
    'amount': '300',
    'sender': 'Rodrigo',
    'receiver': 'Thomas'}
transaction5 = {
    'amount': '200',
    'sender': 'Timothy',
    'receiver': 'Thomas'}
transaction6 = {
    'amount': '400',
    'sender': 'Tiffany',
    'receiver': 'Xavier'}

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

my_transaction = {
    'amount': '400',
    'sender': 'Jonas',
    'receiver': 'Xavier'}

mempool.append(my_transaction)

from hashlib import sha256
# text to hash
text = "I am excited to learn about blockchain!"

# print result
hash_result = sha256(text.encode())
print(hash_result)
print(hash_result.hexdigest())

#s. hier auch Block.py