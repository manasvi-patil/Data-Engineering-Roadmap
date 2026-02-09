from rapidfuzz import process

valid_locations = ["vile parle",
    "andheri",
    "byculla",
    "wadala",
    "bandra",
    "borivali",
    "kandivali",
    "chunabhatti",
    "vasai road",
    "koparkhairane",
    "panvel"]

input_value = "New Panvel"
normalized_input = input_value.lower().strip()

match = process.extractOne(normalized_input, valid_locations)
print(match)

threshold = 50

if match and match[1] >= threshold:
    accepted_location = match[0]
else:
    accepted_location = None

print("Accepted: ", accepted_location)
