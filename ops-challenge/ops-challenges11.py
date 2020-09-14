file1 = open("jedi.txt", "w")

file1.writelines("hellow")
file1.writelines("hellow")
file1.writelines("hellow")
file1.writelines("hellow")
file1.writelines("\nhey")

file1.close()

file1 = open("jedi.txt", "r")


print(file1.readlines())

file1.close()

files = open("jedi.txt", "a")

files.writelines("\nyoda")