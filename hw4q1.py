import os

########################################################################
########################################################################

def print_sort_words(sort_arr, ascii_str_old, txt):

    new_txt = []
    for i in range(len(sort_arr)): 
        value_asci = sort_arr[i]
        index = ascii_str_old.index(value_asci)
        new_txt.append(txt[index])
        ascii_str_old[index] = ''

    return ' '.join(new_txt)

def bubble_sort(ascii_str):

    n = len(ascii_str)      
    for i in range(n-1):   
        for j in range(0, n-i-1): 
            if ascii_str[j] > ascii_str[j+1] : 
                ascii_str[j], ascii_str[j+1] = ascii_str[j+1], ascii_str[j] 
    return ascii_str
        
def sort_words(txt: str) -> str:
    
    ascii_str = []
    ascii_str_old = []
    words = [word for word in txt.split()]

    for word in words:
        asc_w = 0
        for w in word:
            asc_w += ord(w)
        ascii_str.append(asc_w)
        ascii_str_old.append(asc_w)

    sort_arr = bubble_sort(ascii_str)
    return print_sort_words(sort_arr, ascii_str_old, words)
    
########################################################################
# DO NOT EDIT!!!
if __name__ == "__main__":
    text = input().strip(os.linesep)
    sorted_text = sort_words(text)
    print(sorted_text)


