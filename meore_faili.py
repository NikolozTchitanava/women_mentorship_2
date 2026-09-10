import os

# ვამოწმებთ ფაილი არსებობს, თუ არა
if not os.path.exists("log.txt"):
    with open("log.txt", "w") as f:
        f.write("Initial log created.\n")

# Reading
with open("log.txt", "r") as f:
    data = f.read()
print(data)

# Writing (ქმნის ან გადააწერს არსებულს)
with open("report.txt", "w") as f:
    f.write("Suspicious activity detected.\n")

# Appending (ქმნის ან ამატებს არსებულს)
with open("report.txt", "a") as f:
    f.write("Added more info.\n")
