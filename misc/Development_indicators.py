import numpy as np
import pandas as pd


#Reading the csv files

#1) GDP
#gdp_file = pd.read_csv("data/gdp.csv")
gdp_file = pd.read_csv("gdp.csv")

#2) GDP per capital
#gdp_per_capita_file = pd.read_csv("data/gdp_per_capita.csv")
gdp_per_capita_file = pd.read_csv("gdp_per_capita.csv")

#3) GINI coefficient
#gini_file = pd.read_csv("data/gini_index.csv")
gini_file = pd.read_csv("gini_index.csv")

#4) Rural population as percentage
#rural_pop_file = pd.read_csv("data/rural_pop_perc.csv")
rural_pop_file = pd.read_csv("rural_pop_perc.csv")

#5) Urban population as percentage
#urban_pop_file = pd.read_csv("data/urban_pop_perc.csv")
urban_pop_file = pd.read_csv("urban_pop_perc.csv")

#6) Population
#population_file = pd.read_csv("data/population.csv")
population_file = pd.read_csv("population.csv")

#7) Literacy rate
#literacy_rate_file = pd.read_csv("data/literacy_rate.csv")
literacy_rate_file = pd.read_csv("literacy_rate.csv")

#8) Mortality rate
#mortality_rate_file = pd.read_csv("mortality_rate.csv")
mortality_rate_file = pd.read_csv("mortality_rate.csv")

#9) Population of people aged 0 - 14 as percentage
#pop_14_file = pd.read_csv("data/pop_0_14_perc.csv")
pop_14_file = pd.read_csv("pop_0_14_perc.csv")

#10) Population of people aged 15 - 64 as percentage
#pop_15_64_file = pd.read_csv("data/pop_15_64_perc.csv")
pop_15_64_file = pd.read_csv("pop_15_64_perc.csv")

#11) Population of people aged 65 and older as percentage
#pop_65_file = pd.read_csv("data/pop_65_perc.csv")
pop_65_file = pd.read_csv("pop_65_perc.csv")

#12) Population of females as percentage
#pop_female_file = pd.read_csv("data/pop_female_perc.csv")
pop_female_file = pd.read_csv("pop_female_perc.csv")

#13) Internet usage as percentage
#internet_file = pd.read_csv("data/internet_usage.csv")
internet_file = pd.read_csv("internet_usage.csv")

#14) Surface area
#surface_area_file = pd.read_csv("data/surface_area.csv")
surface_area_file = pd.read_csv("surface_area.csv")

#15) Pverty headcount at $3.2
#poverty_file = pd.read_csv("data/poverty.csv")
poverty_file = pd.read_csv("poverty.csv")

#16) Life expectancy
#life_expectancy_file = pd.read_csv("data/life_expectancy.csv")
life_expectancy_file = pd.read_csv("life_expectancy.csv")



#Corona has been given the year 2018 as the information for the year 2019 is not yet available
virus_start_years = {'corona': '2018', 'ebola': '2014', 'mers': '2012', 'h1n1': '2009', 'sars': '2003'}
headers = ["Country", "gdp", "gdp_per_capita", "gini_index", "population", "rural_pop", "urban_pop"
          , "pop_14", "pop_15_64", "pop_65", "pop_female" , "literacy", "mortality", "life_expec", "poverty", "surface_area", "internet"]
new_headers = []
for h in headers:
    if h == "Country":
        new_headers.append(h)
    else:
        for v in virus_start_years:
            new_headers.append(h+"_"+virus_start_years[v])

new_headers = np.reshape(new_headers, (1, 81))
#countries = pd.read_csv('data/countries.csv')
countries = pd.read_csv('countries.csv')


#Creating the indicator Arrays
gdp = []
gdp_per_capita = []
gini = []
rural_pop = []
urban_pop = []
population = []
literacy = []
mortality = []
pop_14 = []
pop_15_64 = []
pop_65 = []
pop_female = []
life_expec = []
poverty = []
surface_area = []
internet = []



#Appending the list of countries to each indicator
country_list = gdp_file['Country Name']

country_list = [i.split(',')[0] for i in country_list]
gdp.append(country_list)

#Filling the arrays with information we need from the files
for year in virus_start_years:
    gdp.append(gdp_file[virus_start_years[year]])
    gdp_per_capita.append(gdp_per_capita_file[virus_start_years[year]])
    gini.append(gini_file[virus_start_years[year]])
    rural_pop.append(rural_pop_file[virus_start_years[year]])
    urban_pop.append(urban_pop_file[virus_start_years[year]])
    population.append(population_file[virus_start_years[year]])
    literacy.append(literacy_rate_file[virus_start_years[year]])
    mortality.append(mortality_rate_file[virus_start_years[year]])
    pop_14.append(pop_14_file[virus_start_years[year]])
    pop_15_64.append(pop_15_64_file[virus_start_years[year]])
    pop_65.append(pop_65_file[virus_start_years[year]])
    pop_female.append(pop_female_file[virus_start_years[year]])
    life_expec.append(life_expectancy_file[virus_start_years[year]])
    poverty.append(poverty_file[virus_start_years[year]])
    surface_area.append(surface_area_file[virus_start_years[year]])
    internet.append(internet_file[virus_start_years[year]])

gdp = np.array(np.transpose(gdp))
gdp_per_capita = np.array(np.transpose(gdp_per_capita))
gini = np.array(np.transpose(gini))
rural_pop = np.array(np.transpose(rural_pop))
urban_pop = np.array(np.transpose(urban_pop))
population = np.array(np.transpose(population))
literacy = np.array(np.transpose(literacy))
mortality = np.array(np.transpose(mortality))
pop_14 = np.array(np.transpose(pop_14))
pop_15_64 = np.array(np.transpose(pop_15_64))
pop_65 = np.array(np.transpose(pop_65))
pop_female = np.array(np.transpose(pop_female))
life_expec = np.array(np.transpose(life_expec))
poverty = np.array(np.transpose(poverty))
surface_area = np.array(np.transpose(surface_area))
internet = np.array(np.transpose(internet))

files = [gdp, gdp_per_capita, gini, population, rural_pop, urban_pop,
         pop_14, pop_15_64, pop_65, pop_female, literacy, mortality, life_expec, poverty, surface_area, internet]

full = np.concatenate(files, axis=1)
full = np.concatenate([new_headers, full])

#for i in range(1,len(full)):
#     for j in range(len(full[0])):
#         if full[i][16] < 500000.0:
#             np.delete(full[i])
#             print(np.shape(full))

np.savetxt('development_indicators.csv', full, delimiter=',', fmt='%s')

#merging H1N1 data with development_indicators.csv
h1n1 = pd.read_csv("Pandemic_H1N1_200905-200907.csv")
dev_ind = pd.read_csv("development_indicators.csv")
h1n1_dev_join = dev_ind.merge(h1n1, how='left', left_on='Country', right_on='Country')
h1n1_dev_join.to_csv("h1n1_dev_join.csv", index=False)

#merging covid19 data with h1n1 and dev indicator data
covid19 = pd.read_csv("nCoV-cases-byCountry.csv")
h1n1_dev_join = pd.read_csv("h1n1_dev_join.csv")
covid19_h1n1_dev_join = h1n1_dev_join.merge(covid19, how='left', left_on='Country', right_on='Country')
covid19_h1n1_dev_join.to_csv("covid19_h1n1_dev_join.csv", index=False)

#merging SARS data with covid19, h1n1, dev indicator data
SARS = pd.read_csv("Sars_Data.csv")
covid19_h1n1_dev_join = pd.read_csv("covid19_h1n1_dev_join.csv")
SARS_covid19_h1n1_dev_join = covid19_h1n1_dev_join.merge(SARS, how='left', left_on='Country', right_on='Country')
SARS_covid19_h1n1_dev_join.to_csv("SARS_covid19_h1n1_dev_join.csv", index=False)

#merging EBOLA data with ^
Ebola = pd.read_csv("Ebola_dataset.csv")
SARS_covid19_h1n1_dev_join = pd.read_csv("SARS_covid19_h1n1_dev_join.csv")
Ebola_SARS_covid9_h1n1_dev_join = SARS_covid19_h1n1_dev_join.merge(Ebola, how='left', left_on='Country', right_on='Country')
Ebola_SARS_covid9_h1n1_dev_join.to_csv("Ebola_SARS_covid9_h1n1_dev_join.csv", index=False)

np.savetxt('dev_virus_join.csv', full, delimiter=',', fmt='%s')
