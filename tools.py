from Crypto.Hash import SHA256

# 计算区块hash
def get_blockhash(index, previous_hash, timestamp, merkleroot, nonce, difficulty):
    hash_str = str(index) + previous_hash + str(timestamp) + merkleroot + str(nonce) + str(difficulty)
    sha = SHA256.new(hash_str.encode('utf-8'))
    return sha.hexdigest()



