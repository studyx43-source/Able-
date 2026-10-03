from dataclasses import dataclass

@dataclass
class CryptoVerification:
    verified: bool
    txid: str
    confirmations: int = 0

async def verify_crypto_transaction(txid: str) -> CryptoVerification:
    return CryptoVerification(False, txid, 0)
