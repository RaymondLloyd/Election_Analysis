counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "ElPaso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is NOT in the list of counties.")
                  
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
       print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
