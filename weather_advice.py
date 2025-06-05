# Ask the user for the weather
weather = weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Provide clothing recommendation based on weather
if weather.lower() =="sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print("Don't forgrt your umbrella and a raincoat.")
elif weather.lower() :
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, i don't have recommendations for this wearther.")
