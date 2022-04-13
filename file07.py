def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    ind=0
    sum_numbers=0
    while ind<len(data) :
        if data[ind].isdigit() :
            a=data[ind]
            sum_numbers+=int(a)
        ind+=1  
      
    return sum_numbers



fayl7=open("txt_file/data07.txt","r")
data=fayl7.read()
print(main(data))
fayl7.close()



