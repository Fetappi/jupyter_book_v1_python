import os
print(os.getcwd())



# file = open("my_file.txt")
# file = open(r"lectures\5\my_file.txt")

file = open(r"lectures\5\my_file.txt", encoding="utf-8" )

print( file.read() )


# # file.close()