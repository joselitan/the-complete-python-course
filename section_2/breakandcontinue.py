
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# for status in cars:
#     if status == "faulty":
#         print("Stopping the production line!")
#         break
#     print(f"This car is {status}")
#     print("Shipping new car to customer!")

# for status in cars:
#     if status == "faulty":
#         print("Found faulty car, skipping...")
#         continue
#     print(f"This car is {status}")
#     print("Shipping new car to customer!")

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")
