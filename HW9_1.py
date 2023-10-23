source_file = "test.txt"
with open(source_file, "r") as source:
    data = source.read()

target_file = "test_1.txt"
with open(target_file, "w") as target:
    target.write(data)

print('The data was successfully copied to a new file.')
