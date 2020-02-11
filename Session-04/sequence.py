from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
body = file_contents.split("\n")[1:]
sequence = ",".join(body).replace(",", "")

print(len(sequence))
