def is_year_leap(year):
    return year % 4 == 0


year = 1992
result = is_year_leap(year)
print(f"год {year}: {result}")
