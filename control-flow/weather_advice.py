# weather_advice.py
 #Ask user to input weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()


#Providing weather advice
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

 #else statement   
else:
    print("Sorry, I don't have recommendations for this weather.")