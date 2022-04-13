def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    ind=0
    num_numbers=0
    num_caracters=0
    while ind<len(data) :
        if  not data[ind].isdigit() :
            num_caracters+=1
        if  data[ind].isdigit() :
            num_numbers+=1
         
        ind+=1  
      
    return list+[num_numbers]+[num_caracters]

# Read data from file

fayl5=open("txt_file/data05.txt","r")
data=fayl5.read()
print(main(data))
fayl5.close()