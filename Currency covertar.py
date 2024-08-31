def currency_converter():
    # Define exchange rates
    exchange_rates = {
        'USD': {'EUR': 0.91, 'GBP': 0.77, 'JPY': 149.63, 'CAD': 1.37, 'AUD': 1.50},
        'EUR': {'USD': 1.10, 'GBP': 0.85, 'JPY': 164.91, 'CAD': 1.51, 'AUD': 1.65},
        'GBP': {'USD': 1.30, 'EUR': 1.18, 'JPY': 193.08, 'CAD': 1.77, 'AUD': 1.94},
        'JPY': {'USD': 0.0067, 'EUR': 0.0061, 'GBP': 0.0052, 'CAD': 0.0091, 'AUD': 0.0103},
        'CAD': {'USD': 0.73, 'EUR': 0.66, 'GBP': 0.57, 'JPY': 109.89, 'AUD': 1.13},
        'AUD': {'USD': 0.67, 'EUR': 0.61, 'GBP': 0.52, 'JPY': 97.01, 'CAD': 0.89}
    }

    print("Welcome to the Currency Converter Program!")

    while True:
        # Get source currency
        source_currency = input("Enter source currency: ").upper()
        if source_currency not in exchange_rates:
            print("Invalid currency selection. Please choose from the available currencies.")
            continue

        # Get target currency
        target_currency = input("Enter target currency: ").upper()
        if target_currency not in exchange_rates[source_currency]:
            print("Invalid currency selection. Please choose from the available currencies.")
            continue

        # Get amount to convert
        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")
            continue

        # Perform conversion
        converted_amount = amount * exchange_rates[source_currency][target_currency]
        print(f"{amount} {source_currency} is {converted_amount:.2f} {target_currency}")

        # Check if the user wants to perform another conversion
        another = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Currency Converter Program. Goodbye!")
            break


# Run the program
currency_converter()