from dataclasses import dataclass

@dataclass
class PaymentResult:
    verified: bool
    reference: str | None = None
    reason: str | None = None

async def verify_payment(reference: str) -> PaymentResult:
    return PaymentResult(False, reference=reference, reason="Payment provider not configured")
