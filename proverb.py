

def proverb(array):
     for i in range (len(array) - 1):
          print("For want of a " + array[i] + " the " + array[i+1] + " was lost.")

     if (len(array) > 0 and array[0] != '""'):
          print("And all for the want of a "+array[0]+".")     
     elif array.__contains__('""'):
          return      
arr = list(map(str, input().split()))
proverb(arr)
