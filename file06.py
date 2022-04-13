def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    ind=0
  
    for i in data.split("\n") :
        a=len(i)
        list.append(a)
    
      
    return list



fayl6=open("txt_file/data06.txt","r")
data=fayl6.read()
print(main(data))
fayl6.close()
