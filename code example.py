# Example code to find index associated with a key using the
# enumerate function

records = [ ('bobpage12@example.com','A prototype'),
            ('traceryong@example.com','retrieve the sword'),
            ('nicoletteduclare@example.com', 'Theres a pill for that')
            ]

for index, record in enumerate(records):
    key, value = record
    if key == "johndoe@example.com":
        break

print(records[index])