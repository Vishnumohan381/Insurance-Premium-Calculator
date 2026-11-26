
# ==========================================
# INSURANCE PREMIUM CALCULATOR
# Project 1 - Python Mini Project
# ==========================================

import random

# Display application title

print("\n========================================")
print("       INSURANCE PREMIUM CALCULATOR")
print("========================================")

# Step 1: Collect customer information

customer_name = input("Enter Customer Name: ").strip()

if not customer_name:
    print("Error: Customer name cannot be empty.")

else:

    # Step 2: Collect insurance type

    insurance_type = input(
        "Enter Insurance Type (Auto/Home): "
    ).strip().lower()

    if insurance_type not in ["auto", "home"]:

        print("Error: Please enter Auto or Home.")

    else:

        # Step 3: Collect coverage amount

        try:

            coverage_amount = float(
                input("Enter Coverage Amount: ")
            )

            if coverage_amount <= 0:
                print("Error: Coverage must be greater than zero.")

            else:

                # Step 4: Define premium rates

                if insurance_type == "auto":
                    premium_rate = 0.02

                elif insurance_type == "home":
                    premium_rate = 0.01

                # Step 5: Calculate base premium

                base_premium = coverage_amount * premium_rate

                # Step 6: Calculate illustrative tax

                tax_rate = 0.18

                tax_amount = base_premium * tax_rate

                # Step 7: Calculate total premium

                total_premium = base_premium + tax_amount

                # Step 8: Generate policy reference number

                policy_number = "POL" + str(
                    random.randint(100000, 999999)
                )

                # Step 9: Display insurance quotation

                print("\n========================================")
                print("          INSURANCE QUOTATION")
                print("========================================")

                print("Policy Number:", policy_number)
                print("Customer Name:", customer_name.title())
                print("Insurance Type:", insurance_type.upper())

                print("----------------------------------------")

                print("Coverage Amount: Rs.", round(coverage_amount, 2))
                print("Premium Rate:", premium_rate * 100, "%")
                print("Base Premium: Rs.", round(base_premium, 2))
                print("Tax Rate:", tax_rate * 100, "%")
                print("Tax Amount: Rs.", round(tax_amount, 2))

                print("----------------------------------------")

                print("TOTAL PREMIUM: Rs.", round(total_premium, 2))

                print("========================================")
                print("Thank you for using our calculator!")

        except ValueError:

            print("Error: Please enter a valid numerical amount.")

