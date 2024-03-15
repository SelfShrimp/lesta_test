import cppyy

cpp_code = """
bool isEven(int value) {
    return (value % 2) == 0;
}
"""

# Компилируем код с помощью cppyy
cppyy.cppdef(cpp_code)

print(cppyy.gbl.isEven(2))
print(cppyy.gbl.isEven(3))