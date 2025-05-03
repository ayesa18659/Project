# Currency Converter to BDT as of May 3, 2025

# Exchange rates: 1 unit of foreign currency to BDT
exchange_rates = {
    'USD': 119.53,   # US Dollar
    'EUR': 139.69,   # Euro
    'GBP': 157.97,   # British Pound
    'JPY': 0.8309,   # Japanese Yen
    'AUD': 72.26,    # Australian Dollar
    'CAD': 83.21,    # Canadian Dollar
    'CHF': 135.00,   # Swiss Franc (approximate)
    'CNY': 16.38,    # Chinese Yuan
    'INR': 1.44,     # Indian Rupee
    'SGD': 91.40     # Singapore Dollar
}

def convert_to_bdt(amount, currency_code):
    """
    Converts the given amount from the specified currency to BDT.
    
    Parameters:
    - amount (float): The amount in the foreign currency.
    - currency_code (str): The 3-letter currency code (e.g., 'USD', 'EUR').
    
    Returns:
    - float: The equivalent amount in BDT.
    """
    rate = exchange_rates.get(currency_code.upper())
    if rate:
        return amount * rate
    else:
        raise ValueError(f"Unsupported currency code: {currency_code}")

def main():
    print("Currency Converter to Bangladeshi Taka (BDT)")
    print("Supported currencies:", ', '.join(exchange_rates.keys()))
    try:
        currency = input("Enter the currency code (e.g., USD, EUR): ").strip().upper()
        amount = float(input(f"Enter the amount in {currency}: "))
        bdt_amount = convert_to_bdt(amount, currency)
        print(f"{amount} {currency} = {bdt_amount:.2f} BDT")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()