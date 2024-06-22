# To calculate a Game Store bar bill.
# Jordan Picton 22/06/2024
print("Welcome to the Picton Games!")

price_terraria = 8.50  # float
price_space_marines_2 = 54.99  # float
price_aska = 29.99  # float
price_eso_golden_road = 33.99  # float
price_elden_ring = 49.99  # float

total = 0.0

number_terraria_units = int(input("How many Terraria units? "))
# print(number_terraria_units)
number_sm2_units = int(input("How many Space Marines 2 units? "))
# print(number_sm2_units)
number_aska_units = int(input("How many ASKA units? "))
# print(number_aska_units)
number_eso_golden_road_units = int(
    input("How many Elder Scrolls Online Golden Road units? ")
)
# print(number_eso_golden_road_units)
number_elden_ring_units = int(input("How many ELDEN RING units? "))
# print(number_elden_rign_units)

terraria_total = number_terraria_units * price_terraria
space_marines_total = number_sm2_units * price_space_marines_2
aska_total = number_aska_units * price_aska
eso_total = number_eso_golden_road_units * price_eso_golden_road
elden_ring_total = number_elden_ring_units * price_elden_ring

total = terraria_total + space_marines_total + aska_total + eso_total + elden_ring_total

print(
    "Thank you for shopping at Picton Games!",
    "Your items and total can be seen below!",
    " Terraria Units: "
    + str(number_terraria_units)
    + " | Total: £"
    + str(terraria_total),
    " Space Marines 2 Units: "
    + str(number_sm2_units)
    + " | Total: £"
    + str(space_marines_total),
    " ASKA Units: "
    + str(number_aska_units)
    + " | Total: £"
    + str(aska_total),
    " Elder Scrolls Online  Units: "
    + str(number_eso_golden_road_units)
    + " | Total: £"
    + str(eso_total),
    " ELDEN RING Units: "
    + str(number_elden_ring_units)
    + " | Total: £"
    + str(elden_ring_total),
    "Your overall total comes to: £" + str(total),
    sep="\n"
)
