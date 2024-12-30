hours = [12] + list(range(1, 12))
minutes = ["00", "15", "30", "45"]
times = ["am", "pm"]
for time in times:  
    for hour in hours:
        for minute in minutes:
            print(f"{hour}:{minute} {time}")
