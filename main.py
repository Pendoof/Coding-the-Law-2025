import pandas as pd

def main():
    # import csv data using pandas
    limits = pd.read_csv("speedlimit.csv")
    df = pd.read_csv("driving_data.csv")

    # initial variable setup
    issued_tickets = 0
    time_index = 0
    last_infraction = -5

    # traverse rows in driving data
    for _, row in df.iterrows():

        # update time, speed, and limit data
        time = row["Time(minutes)"]
        speed = row["Speed(MPH)"]
        limit_start = limits["Time (minutes)"].iloc[time_index]
        speed_limit = limits[" Speed Limit (MPH)"].iloc[time_index]

        # update newest speed limit based on current time
        if time > limit_start and time_index < len(limits) - 1:
            time_index += 1

        # change speed tolerance based on speed limit
        if speed_limit > 30:
            if abs(speed - speed_limit) > 13:
                if time - last_infraction >= 5:
                    issued_tickets += 1
                    last_infraction = time
        else:
            if abs(speed - speed_limit) > 8:
                if time - last_infraction >= 5:
                    issued_tickets += 1
                    last_infraction = time
    
    print(issued_tickets)


        


if __name__ == "__main__":
    main()