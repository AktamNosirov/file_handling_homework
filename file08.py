from re import I


def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    list=[]
    ind=0
    for i in data.split("\n"):
       while ind<len(data) :
            if data[ind].isdigit() :
               a=data[ind]
               list.append(a)
            ind+=1  
           
      
      
    return max(list) 



fayl8=open("txt_file/data08.txt","r")
data=fayl8.read()
print(main(data))
fayl8.close()