from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker()

products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Smartwatch"
]

cities = [
    "Toronto",
    "Waterloo",
    "Kitchener",
    "Ottawa",
    "London"
]

coupon_codes = [
    "SAVE10",
    "SAVE20",
    "SAVE30",
    None
]

transactions = []

for transaction_id in range(1, 501):

    transaction = {
        "transaction_id": transaction_id,
        "date": fake.date_between(
            start_date="-1y",
            end_date="today"
        ),
        "customer_id": f"CUST{random.randint(1000, 9999)}",
        "product": random.choice(products),
        "price": round(random.uniform(20, 2000), 2),
        "quantity": random.randint(1, 5),
        "coupon_code": random.choice(coupon_codes),
        "shipping_city": random.choice(cities)
    }

    transactions.append(transaction)

df = pd.DataFrame(transactions)

# Introduce controlled dirty data for the cleaning exercise

# Dirty case 1: Missing prices
df.loc[[10, 25, 40], "price"] = None

# Dirty case 2: Inconsistent shipping city formatting
df.loc[15, "shipping_city"] = " toronto "
df.loc[30, "shipping_city"] = "WATERLOO"
df.loc[45, "shipping_city"] = "kitchener"

# Dirty case 3: Missing product names
df.loc[[20, 35], "product"] = None

data_folder = Path(__file__).resolve().parents[1] / "data"
data_folder.mkdir(exist_ok=True)

output_file = data_folder / "ecommerce_transactions.csv"

df.to_csv(output_file, index=False)

print("Dataset created successfully.")
print(df.head())
print(f"Total records: {len(df)}")