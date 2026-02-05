raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print("Raw logs:", raw_logs)
unique_users=set(raw_logs)
print(unique_users)
print("ID05" in unique_users)
print("length of raw_logs:", len(raw_logs))
print("length of unique_users:", len(unique_users))