s = input("Введите текст:")
words = s.split()
unique_words=set(words)
palindroms=[]
for word in unique_words:
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        palindroms.append(word) # append-добавляет элемент в список
print(f"Получены палиндромы: {palindroms}")
