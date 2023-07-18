def reverse_string(strng):
    array=list(strng)
    start=0
    end=len(array)-1
    result=""
    while(start<end):
        array[start],array[end]=array[end],array[start]
        start+=1
        end-=1 
    return result.join(array)
    # result=strng[::-1]
    # return result

strng=input("Enter the String : ")
print(reverse_string(strng))