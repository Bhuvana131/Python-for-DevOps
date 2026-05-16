
text = input("Enter the text:")
count = 0

for i in text:
    if i in "aeiouAEIOU":
        count = count+1

print("Count of Vowels:",count)