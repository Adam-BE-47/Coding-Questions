#This is a script that given today's schedule of two people , it will give the time when they can meet.

# -- SSS -- this part takes as input the meetings of the 2 persons  

   # ------> person 1
nb1 = int(input("Please enter how many meetings the first person has : "))

l1 = []
i1= 1
while i1 < (nb1 + 1) :
    mt1 = []
    st1 = "a"
    end1 = "a"

    while (len(st1) < 4 or len(end1) < 4 ):
        print(f"meeting {i1} :  ( hour:min ) ")
        st1 = input("   from : ")
        end1 = input("   to   : ")

    mt1.append(st1)
    mt1.append(end1)
    l1.append(mt1)
    i1 += 1

   # ------> person 2
nb2 = int(input("Please enter how many meetings the second person has : "))

l2 = []
i2 = 1
while i2 < (nb2 + 1) :
    mt2 = []
    st2 = "a"
    end2 = "a"

    while (len(st2) < 4 or len(end2) < 4 ):
        print(f"meeting {i2} :  ( hour:min ) ")
        st2 = input("   from : ")
        end2 = input("   to   : ")

    mt2.append(st2)
    mt2.append(end2)
    l2.append(mt2)
    i2 += 1

# -- EEE --

#function that changes the form of the elements of a list from " hour : min" to " hour.min " (str to float)
def r(list):
    for k in list:

        for x in k:

            try:
                h = int(str(x[0] + x[1]))
                min = int(str(x[3] + x[4]))
                k[k.index(x)] = h + min *(10**-2)

            except:
                h = int(str(x[0]))
                min = int(str(x[2] + x[3]))
                k[k.index(x)] = h + min *(10**-2)
# changing the form of the lists ...
r(l1)
r(l2)

# function that removes a repetitive element
def clean1(list):
    k = False

    for x in list:

        if list.count(x) != 1 :
            list.remove(x)
            k = True
    return k 
 
# function that compares two lists to know the times where the meeting is impossible
def f(list1 , list2):
    imp = []
    for k in list1:

        for q in list2:
            l = []

            if ( k[0] >= q[0] and k[1] >= q[0] and k[0] < q[1]) or ( q[0] >= k[0] and q[1] >= k[0] and q[0] < k[1]):
                l.append(min(k[0] , q[0]))
                l.append(max(k[1] , q[1])) 
                imp.append(l)

            else:
                imp.append(k)
                imp.append(q)

    return imp

imp = f(l1 , l2)

# function that cleans the imp list ;) :
def clean2(list):
    i = 0
    k = False

    while i < len(list)-2:
        l = []
        n = list.index(list[i])

        if ( list[i][0] >= list[i+1][0] and list[i][1] >= list[i+1][0] and list[i][0] <= list[i+1][1]) or ( list[i+1][0] >= list[i][0] and list[i+1][1] >= list[i][0] and list[i+1][0] <= list[i][1]):         
            l.append(min(list[i][0] , list[i+1][0]))
            l.append(max(list[i][1] , list[i+1][1]))

            list.remove(list[i])
            list.remove(list[i])
            list.insert(n ,l)
            k = True 
            
        i += 1

    if k == True:
        return list

    if k == False:
        return k

# cleaning the imp list ...
while clean1(imp):
    clean1(imp)

while clean2(imp) != False :
    clean2(imp)

# function that changes the order of the list from small to big
def order(list):
    l1 = []
    f = []
    l2 = []
    final_list = []

    for x in list:
        l1.append(x[0])
        l2.append(x[0])
    
    while l1 != []:
        f.append(min(l1))
        l1.remove(min(l1))
    
    for y in f:
        final_list.append(list[l2.index(y)])
  
    return final_list

imp = order(imp)


# function that gives the final result
def result(list):
    i = 0
    result = []

    while i < len(list)-1:
        r = []

        if i == 0 and list[i][0] != 8.0:
            r = [8.0 , list[i][0]]
            result.append(r)

        if list[i][1] != list[i+1][0]:
            r = [ list[i][1] , list[i+1][0] ] 
            result.append(r)

        else:
            r = [ list[i][1] , list[i+1][1] ]
            result.append(r)

        if i == len(list)-2 and list[i][1] != 20.0:
            r = [list[i+1][1] , 20.0] 
            result.append(r)

        i += 1
    return result

pos = result(imp)

# function that removes the meetings that are less than 30min (cleaning again)
def clean3(list):
    for l in list:
        t1 = 0
        t0 = 0

        # 0000000000000000
        if str(l[0])[1] == ".":
            try:
                h = int(str(l[0])[0]) * 60
                min = int(str(l[0])[2] + str(l[0])[3] )
                t0 = h + min

            except:
                h = int(str(l[0])[0]) * 60
                min = int(str(l[0])[2]) * 10
                t0 = h + min

        elif str(l[0])[2] == ".":
            try:
                h = (int(str(l[0])[0] + str(l[0])[1] ) ) * 60
                min = int( str(l[0])[3] + str(l[0])[4] )
                t0 = h + min

            except:
                h = (int( str(l[0])[0] + str(l[0])[1] ) ) * 60
                min = int(str(l[0])[3])*10
                t0 = h + min

        # 11111111111111111
        if str(l[1])[1] == ".":
            try:
                h = int(str(l[1])[0]) * 60
                min = int( str(l[1])[2] + str(l[1])[3] )
                t1 = h + min

            except:
                h = int(str(l[1])[0] ) * 60
                min = int(str(l[1])[2]) * 10
                t1 = h + min

        elif str(l[1])[2] == ".":
            try:
                h = (int(str(l[1])[0] + str(l[1])[1] ) ) * 60
                min = int(str(l[1])[3] + str(l[1])[4] )
                t1 = h + min

            except:
                h = (int(str(l[1])[0] + str(l[1])[1]) ) * 60
                min = int(str(l[1])[3]) * 10
                t1 = h + min

        if t1 - t0 < 30 :
            list.remove(l)

    return list
    
# cleaning the pos list ... (again!!)
pos = clean3(pos)

# function that changes the form from float to str
def result_again(list):
    for l in list:

        for x in l:

            if str(x)[1] == ".":
                try:
                    s = str(x)
                    h = s[0]
                    min = s[2] + s[3]
                    l[l.index(x)] = h + "h" + min

                except:
                    s = str(x)
                    h = s[0] 
                    min = s[2] + "0"
                    l[l.index(x)] = h + "h" + min

            elif str(x)[2] == ".":
                try:
                    s = str(x)
                    h = s[0] + s[1]
                    min = s[3] + "0"
                    l[l.index(x)] = h + "h" + min

                except:
                    s = str(x)
                    h = s[0] + s[1] 
                    min = s[3] + s[4]
                    l[l.index(x)] = h + "h" + min

result_again(pos)
print( " possible time for meeting  : " ,pos)

