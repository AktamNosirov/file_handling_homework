def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    string=""
    for i in data :
        a=str(i)
        string+=a
        
      
    return len(string) 

# Read data from file

fayl2=open("txt_file/data02.txt","r")
data=fayl2.read()
print(main(data))
fayl2.close()