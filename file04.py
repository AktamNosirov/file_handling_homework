def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    ind=0
    while ind<len(data) :
        if  not data[ind].isalpha() :
            a=data[ind]
            list.append(a)
        ind+=1  
      
    return list 

# Read data from file

fayl4=open("txt_file/data04.txt","r")
data=fayl4.read()
print(main(data))
fayl4.close()