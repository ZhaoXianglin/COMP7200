from TxIn import TxIn
from TxOut import TxOut
from Crypto.Hash import SHA256

class Transaction(object):
    def __init__(self, txins, txouts, timestamp):
        """
        :param txid: <str> 交易id
        :param txIns: <TxIn> 数组
        :param txOut: <TxOut> 数组
        """
        self.txIns = txins
        self.txOuts = txouts
        self.timestamp = timestamp
        self.txid = self.get_txid()


    def get_txid(self):
        in_str = "".join([(i.txOutId + i.txOutIndex) for i in self.txIns])
        out_str = "".join([(o.address + o.amount) for o in self.txOuts])
        hash_str = (in_str+out_str).encode("utf-8")
        return SHA256.new(hash_str).hexdigest()