import zipfile
  
zip_file_path=zipfile.ZipFile('sample.zip') 
total=0 
 
for i in range(1,1000,2): 
    filename=f'sample/kitamura_{i:05}_kgu.txt' 
    with zip_file_path.open(filename, 'r') as file: 
       numbers=int(file.read().strip()) 
       total+=numbers
       
print("奇数ファイルの中の数字の合計=",total)