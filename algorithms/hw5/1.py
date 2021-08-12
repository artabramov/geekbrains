companies_number = int(input('companies number: '))
companies = []

for i in range(1, companies_number + 1):
    company = []
    company.append(input(f'company name {i}: '))
    for j in range (1, 5):
        company.append(int(input(f'income for quarter {j}: ')))
    company.append(sum(company[1:5]) / 4)
    companies.append(company)

income_average = sum([x[5] for x in companies]) / companies_number

print('companies with income lower than average: ', [x[0] for x in companies if x[5] < income_average])
print('companies with income higher than average: ', [x[0] for x in companies if x[5] > income_average])
