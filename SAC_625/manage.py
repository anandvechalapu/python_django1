# manage.py
import sys

# Define minimum and maximum sum assured, minimum and maximum age limits as defined for each product and master level
MIN_SUM_ASSURED = 0
MAX_SUM_ASSURED = 0
MIN_AGE_LIMIT = 0
MAX_AGE_LIMIT = 0

# Define annual income limit
ANNUAL_INCOME_LIMIT = 40000

# Define sum assured ranges
SUM_ASSURED_RANGES = [50000, 100000, 150000, 200000]

# Define policy tenure ranges
POLICY_TENURE_RANGES = [12, 15, 18, 24]

# Function to validate criteria before issuing the Bajaj Allianz Group Sampoorna Jeevan Suraksha policy
def validate_criteria(sum_assured, age, income, otp):
    if sum_assured < MIN_SUM_ASSURED or sum_assured > MAX_SUM_ASSURED:
        print("Sum assured value is not within the range")
        sys.exit(1)
    if age < MIN_AGE_LIMIT or age > MAX_AGE_LIMIT:
        print("Age is not within the range")
        sys.exit(1)
    if income < ANNUAL_INCOME_LIMIT:
        print("Annual income is less than 40K. Policy cannot be issued")
        sys.exit(1)
    if otp is None:
        print("OTP authentication has not been received. Policy cannot be issued")
        sys.exit(1)

# Function to display sum assured ranges to the Bandhan Bank sales personnel
def display_sum_assured_ranges():
    print("Sum assured ranges:")
    for range in SUM_ASSURED_RANGES:
        print(range)

# Function to display policy tenure ranges to the Bandhan Bank sales personnel
def display_policy_tenure_ranges():
    print("Policy tenure ranges:")
    for range in POLICY_TENURE_RANGES:
        print(range)

# Function to check if spouse is eligible for coverage
def check_spouse_eligibility(income):
    if income < ANNUAL_INCOME_LIMIT:
        print("Spouse is not eligible for coverage")
        sys.exit(1)
    else:
        print("Spouse is eligible for coverage")

def main():
    sum_assured = int(input("Enter sum assured value: "))
    age = int(input("Enter age: "))    
    income = int(input("Enter annual income: "))
    otp = int(input("Enter OTP: "))

    # Validate criteria
    validate_criteria(sum_assured, age, income, otp)

    # Display sum assured and policy tenure ranges
    display_sum_assured_ranges()
    display_policy_tenure_ranges()

    # Check spouse eligibility
    check_spouse_eligibility(income)

if __name__ == '__main__':
    main()