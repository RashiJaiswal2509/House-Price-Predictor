# =========================================
#        HOUSE PRICE PREDICTOR
# =========================================

# Function to calculate house price
def predict_price(size, bedrooms, age, location, parking, garden):

    # Base price calculation
    price = (size * 3000) + (bedrooms * 500000) - (age * 10000)

    # Location price
    if location.lower() == "city":
        price += 1000000
    else:
        price += 300000

    # Parking price
    if parking.lower() == "yes":
        price += 200000

    # Garden price
    if garden.lower() == "yes":
        price += 150000

    return price

print("=================================")
print("     HOUSE PRICE PREDICTOR")
print("=================================")

again = "yes"

while again.lower() == "yes":

    # User Inputs
    size = float(input("\nEnter house size in square feet: "))
    
    bedrooms = int(input("Enter number of bedrooms: "))
    
    age = int(input("Enter age of the house: "))
    
    location = input("Enter location (city/village): ")
    
    parking = input("Parking available? (yes/no): ")
    
    garden = input("Garden available? (yes/no): ")

    # Function Call
    price = predict_price(
        size,
        bedrooms,
        age,
        location,
        parking,
        garden
    )

    # Display Result
    print("\n=================================")
    print(f"Estimated House Price = Rs.{price:,.2f}")
    print("=================================")

    # Save Data in File
    file = open("house_data.txt", "a", encoding="utf-8")

    file.write(f"""
House Size : {size} sq ft
Bedrooms   : {bedrooms}
Age        : {age}
Location   : {location}
Parking    : {parking}
Garden     : {garden}
Price      : Rs.{price:,.2f}
----------------------------------------
""")

    file.close()

    # Continue or Stop
    again = input("\nDo you want to predict again? (yes/no): ")

# Ending Message
print("\nThank You for using House Price Predictor")