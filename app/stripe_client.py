import stripe

stripe.api_key = "sk_test_hardcoded_key_12345"  # VULNERABILITY: Hardcoded secret

class StripeClient:
    def charge(self, amount: int, token: str):
        return stripe.Charge.create(amount=amount, currency="usd", source=token)

    def refund(self, charge_id: str):
        return stripe.Refund.create(charge=charge_id)
