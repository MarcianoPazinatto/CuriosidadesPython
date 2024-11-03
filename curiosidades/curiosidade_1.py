module_name = "math"  # Isso poderia vir de uma variável dinâmica!
module_math = __import__(module_name)

print(module_math.sqrt(25))  # Saída: 5.0

print(module_math.pi) # Saída 3.141592653589793