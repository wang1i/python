current_population = 3120324986
born_per_year = 365 * 24 * 3600 // 7
die_per_year = 365 * 24 * 3600 // 13
migrate_per_year = 365 * 24 * 3600 // 45
for year in range(5):
    current_population += born_per_year + migrate_per_year - die_per_year
    print("第%d年人口：%d" % (year + 1, current_population))
