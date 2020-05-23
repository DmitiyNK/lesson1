# weather = {
#     "city": "Moscow",
#     "temperature": "20",
#     "wind": "West"
# }
# # print('cuntry' in weather)
# # for key, value in weather.items():
# #     print('{}: {}'.format(key, value))
# weather["date"] = "16.05.2020"
# print(weather)

# a = [11, 5, 9, 7, 8, 2, 6]
#
# # print(a[2:4])
#
# a.sort()
# print(a)



weather_1 = {
    "city": "Moscow",
    "temperature": "20",
    "wind": "West",
    "date": "16.05.50"
}
weather_2 = {
    "city": "Moscow",
    "temperature": "16",
    "wind": "West",
    "date": "15.05.50"
}
weather_3 = {
    "city": "Moscow",
    "temperature": "10",
    "wind": "West",
    "date": "14.05.50"
}

weather_Moscow = []

weather_Moscow.append(weather_1)
weather_Moscow.append(weather_2)
weather_Moscow.append(weather_3)

print(weather_Moscow)



