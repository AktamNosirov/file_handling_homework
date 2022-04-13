def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list=[]
    ind=0
    while ind<len(data) :
        if  data[ind].isdigit() :
            a=data[ind]
            list+=[a]
        ind+=1  
      
    return min(list) 



fayl9=open("txt_file/data09.txt","r")
data=fayl9.read()
print(main(data))
fayl9.close()
