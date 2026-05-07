import os

var_name = "STUDENT_NAME"

value = os.getenv(var_name)

if value:
    print(f"Значення змінної {var_name} = {value}")
else:
    print(f"Змінна {var_name} не знайдена.")