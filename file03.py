def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    ind=0
    while ind<len(data) :
        if  data[ind].isdigit() :
            a=data[ind]
            list+=[a]
        ind+=1  
      
    return list 

# Read data from file

fayl3=open("txt_file\\data03.txt","r")
data=fayl3.read()
print(main(data))
fayl3.close()