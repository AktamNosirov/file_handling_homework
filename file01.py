def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for i in data.split(",") :
        a=int(i)
        list.append(a)
    
      
    return list

# Read data from file

fayl1=open("txt_file\data01.txt","r")
data=fayl1.read()
print(main(data))
fayl1.close()
