import pandas as pd

class Transaction:
    """Represent and process a single e-commerce transaction."""

    def __init__(
        self,
        transaction_id,
        date,
        customer_id,
        product,
        price,
        quantity,
        coupon_code,
        shipping_city
    ):
        self.transaction_id = transaction_id
        self.date = date
        self.customer_id = customer_id
        self.product = product
        self.price = price
        self.quantity = quantity
        self.coupon_code = coupon_code
        self.shipping_city = shipping_city

    def clean(self, mean_price):
        """Apply cleaning rules to the transaction."""

        # Replace missing product names
        if pd.isna(self.product):
            self.product = "Unknown"
        elif isinstance(self.product, str):
            self.product = self.product.strip().title()

        # Replace missing price with the mean price
        if pd.isna(self.price):
            self.price = mean_price

        # Replace missing coupon codes
        if pd.isna(self.coupon_code):
            self.coupon_code = "NO_COUPON"

        # Standardize shipping city
        if isinstance(self.shipping_city, str):
            self.shipping_city = self.shipping_city.strip().title()

        return self

    def total(self):
        """Calculate the transaction total before discount."""

        if self.price is None:
            return None

        return self.price * self.quantity