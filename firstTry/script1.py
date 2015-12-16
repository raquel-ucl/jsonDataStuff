with open('one.txt', 'r') as file1:
    
    
data1 = set(file1)
    
data1.discard('\n')
    


with open('two.txt', 'r') as file2:
    
    
data2 = set(file2)
    
data1.discard('\n')
  
  


with open('new_file.txt', 'w') as file_out:

        
file_out.writelines(data2 - data1)