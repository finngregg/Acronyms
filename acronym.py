def removal(a,b):
    out = ""
    lst = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i].lower()==b[j].lower():
                lst.append(i)
                
        if i not in lst:
            out += a[i][0].upper()
            
    return out

def main():
    ignore = input("Enter words to be ignored separated by commas:\n").split(", ")
    sen = input("Enter a title to generate its acronym:\n").split(" ")

    print("The acronym is: " + removal(sen,ignore))

main()




