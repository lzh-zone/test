foimport time

def start_concentration_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = round(end_time - time.time())

        if remaining_time >= 60:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print(f"Remaining time: {minutes} minutes {seconds} seconds")
        else:
            print(f"Remaining time: {remaining_time} seconds")

        time.sleep(1)

    print("Time is up! Your concentration time is over.")

# 设置专注时间（单位：分钟）
concentration_duration = 10000000000000000000000000000000000

start_concentration_timer(concentration_duration)
