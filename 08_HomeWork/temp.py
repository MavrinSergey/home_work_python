prices = [1100, 999, 80, 80, 40000]
floors = [10, 1, 1, 4, 30]
distances = [10, 3, 15, 31, 37]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
					   'Россия, Москва, Болотная набережная, 11с1',
						 'Россия, Москва, Романов переулок, 4',
						 'Россия, Москва, Старая Басманная улица, 20к1',
						 'Россия, Москва, Волгоградский проспект, 32к8']

prices_filtered = []
floors_filtered = []
distances_filtered = []
addresses_filtered = []


for index in range(len(prices)):
    if floors[index] == 1 and distances[index] <= 15 and prices[index] < 1000:
        prices_filtered.append(prices[index])
        floors_filtered.append(floors_filtered[index])
        distances_filtered.append(distances_filtered[index])
        addresses_filtered.append(addresses_filtered[index])


print(prices_filtered)
print(floors_filtered)
print(distances_filtered)
print(addresses_filtered)