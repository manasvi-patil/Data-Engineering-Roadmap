#Find and print duplicates

def find_all_duplicates(num):
    seen = set()
    duplicates = set()
    for nums in num:
        if nums in seen:
            duplicates.add(nums)
        else:
            seen.add(nums)
    return duplicates

list1 = [1,2,3,4,5,6,6,7,7,7,7]

duplicates = find_all_duplicates(list1)
if duplicates:
    print(f"Duplicate found: {duplicates}")
else:
    print(f"No duplicates found")


#Find unique character in a string
def find_unique_char(letter):
    seen = []
    unique = []
    for letters in letter:
        if letters in seen:
            unique.append(letters)
        else:
            seen.append(letters)
    return seen

a = "leetcode"
seen = find_unique_char(a)
if seen:
    print(f"Unique characters are: {seen}")
else:
    print(f"No unique characters.")