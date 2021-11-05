#Fatmata Alice Koroma
## Creating a function to count the number of pairs of socks in an array
## The Socks in the pile are stored as individual integer values

def sockmerchant(n, ar):
    #initializing a list that would be used to store pairs of socks
    count1 = []
    #create a set to count the unique element in the array
    my_set= set(ar) 
    #loop throught the set to get the count of individual/unique element 
    for i in my_set:
         #store the pairs into the list
        count1.append(int(ar.count(i)/2))
        # since sets do not support duplicates, we expect that only unique elements and their counts will be in the list we created
        # returning the sum of the list to get the number of pairs
    return sum(count1)

 
    