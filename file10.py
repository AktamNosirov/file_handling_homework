def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list=[]
   
  
    for i in data.split("\n") :
        a=len(i)
        list.append(a)
    
      
    return max(list)



fayl10=open("txt_file/data10.txt","r")
data=fayl10.read()
print(main(data))
fayl10.close()
# Read data from file