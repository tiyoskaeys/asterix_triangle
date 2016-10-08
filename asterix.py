__author__ = 'listiyo'
# write code using python 3

def segitiga_bawah(t, i=2) :
    ''' number -> str
        Return a list of * string where it shaping a triangle up bottom
    >>> segitiga_bawah(5)
    >>>       ***
             *****
            *******
           *********
    '''
    if t==0 or t==1 :
        return
    else :
        print( ' ' * (t - 1) + '*' * (i * 2 - 1))
        return segitiga_bawah(t-1, i+1)


def segitiga_atas(t, i=1) :
    ''' number -> str
        Return a list of * string where it shaping a triangle bottom up
    >>> segitiga_atas(5)
    >>>  *********
          *******
           *****
            ***
             *
    '''
    if t==0 :
        return
    else :
        print( ' ' * i  + '*' * (t * 2 - 1))
        return segitiga_atas(t-1, i+1)


def segitiga(t) :
    ''' number -> str
        return a list of * string that shaping triangle in bottom up and up bottom to fulfill Kompas's test

    >>> segitiga(5)
    >>>  *********
          *******
           *****
            ***
             *
            ***
           *****
          *******
         *********
    '''
    if t==0 :
        return
    else:
        segitiga_atas(t)
        segitiga_bawah(t)
        print(' sh-4.3s')

# ----------------- EOF ----------------- #



#segitiga_atas(5)
#segitiga_bawah(5)
#xsegitiga_kombinasi(13, 7)

while True:
    try:
        p = int(input('Masukkan tingkat segitiga yakni 13, atau berapapun yang kamu inginkan : '))
        break
    except ValueError :
        print('ULANGI : Silahkan masukkan angka. \n')

#segitiga(13)
segitiga(p)



# http://skaeys.net/
