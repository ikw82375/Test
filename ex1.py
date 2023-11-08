file_name="data.txt"
sum=0

with open(file_name, "r") as file:
    
    for line in file:
        try:
            sum += int(line) 
        except ValueError:
            # 行が整数でない場合は無視
            pass

print("整数の和:", sum)