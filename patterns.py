print("CHOOSE YOUR PATTERN [p1() , p2() , p3() , p4()] :")

def p1():
    '''Experiment 18'''
    n=int(input("enter : "))                      #   to print pattern (for input==5):-
    for i in range(1,n+1):                        #         *
        print(" "*(n-i)," *"*i)                   #        * *
                                                  #       * * *
                                                  #      * * * *
                                                  #     * * * * *
#--------------------------------------------------------------------------------------------------#
def p2():
    n=int(input("enter: "))                       #   to print pattern (for input==5):-
    for i in range(n,0,-1):                       #   12345
        for i2 in range(1,i+1):                   #   1234
            print(i2,end='')                      #   123
        print()                                   #   12
                                                  #   1
#--------------------------------------------------------------------------------------------------#
def p3():
    n=int(input("enter : "))                      #   to print pattern (for input==5):-
    i=0                                           #   12345
    while n>0:                                    #    1234
        for i2 in range(1,n+1):                   #     123
            print(i2,end='')                      #      12
        else:                                     #       1
            print("\n"," "*i,end='')
        i+=1
        n-=1
#--------------------------------------------------------------------------------------------------#
def p4():
    var=input("enter str[starting with i]:")  #   take str sentence and reverse only words starting with i and print it
    nstr=''                                   #   Eg- "hello ia india om wish" will print "ai aidni"
    a=var.split()
    for i in a:
         if i[0].lower()=="i":
              nstr+=i[::-1]+" "
    print(nstr)

p1()
p2()
p3()
p4()
