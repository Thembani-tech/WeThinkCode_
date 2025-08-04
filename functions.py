def my_list():
    return ["iphone", "ipad", "macbook"]
print(my_list())

def my_number():
    return 100
print(my_number())

while iphone := my_list()[0]:
    
    print(f"Current item: {iphone}")
    break  # To prevent an infinite loop in this example