print("Создаю текстовый файл методом write(). ")
text_file = open("write_it.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Это строка 2\n")
text_file.write("Этой строке достается номер 3 \n")
text_file.close()

print("\nЧитаю вновь созданный файл")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("\nСоздаю иексирвый файл методом writelines().")
text_file = open("write_it.txt", "w", encoding='utf-8')
lines = ["Это строка 1\n",
         "Это строка 2\n",
         "Этой строке достался номер 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nчитаю вновь созданный файл")
text_file= open("write_it.txt", "r", encoding ='utf-8')
print(text_file.read())
text_file.close()
input("\n\nНажмите enter, чтобы выйти")
