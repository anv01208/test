# 1

s = 'hello world from justcode, not from ulan'

words = list(map(lambda word: word.strip(".,"), s.split(' ')))

print(f"{words = }")

result = {}

# for word in words:
#     if word in result.keys():
#         result[word] = result[word] + 1
#     else:
#         result[word] = 1

for word in words:
    result[word] = result.get(word, 0) + 1

print(result)


# 2

countries = {
    'Russia': {'population': 143400000, 'area': 17098242},
    'China': {'population': 1412000000, 'area': 9596960},
    'India': {'population': 1408000000, 'area': 3287263},
}


def density(countries):
    for country, data in countries.items():
        population = data['population']
        area = data['area']
        density = population / area
        print(f"The population density of {country} is: {density}")


def the_most_density(countries):
    max_density = 0
    most_dense_country = None

    for country, data in countries.items():
        population = data['population']
        area = data['area']
        density = population / area

        if density > max_density:
            max_density = density
            most_dense_country = country

    print(f"\nThe most densely populated country is: {most_dense_country}")


density(countries)
the_most_density(countries)