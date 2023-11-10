text_string = "Welcome to Python Training"
text_string = text_string.lower()
vowel_count = 0
vowels_array = []
vowels = set("aeiou")

for char in text_string:
    if char in vowels:
        vowel_count += 1
        vowels_array.append(char)

print(vowel_count)
print(vowels_array)
