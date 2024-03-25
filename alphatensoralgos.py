import numpy as np



#regular matrix mult

def matnaive(a,b):
    
    #uses numpy matrix multiply
    return a * b


def div2x2(a):
    
    m = len(a)/2


    a11 = a[0:m, 0:m]
    a12 = a[m:2*m, 0:m]
    a21 = a[0:m, m:2*m]
    a22 = a[m:2*m, m:2*m]
    
    
    return (a11, a12,
            a21, a22)

def div5x5(a):
    
    m = len(a)/5
    
    #row 1
    
    a11 = a[0:m, 0:m]
    a12 = a[m:2*m, 0:m]
    a13 = a[2*m:3*m, 0:m]
    a14 = a[3*m:4*m, 0:m]
    a15 = a[4*m:5*m, 0:m]
    
    #row 2
    
    a21 = a[0:m, m:2*m]
    a22 = a[m:2*m, m:2*m]
    a23 = a[2*m:3*m, m:2*m]
    a24 = a[3*m:4*m, m:2*m]
    a25 = a[4*m:5*m, m:2*m]
    
    #row 3
    
    a31 = a[0:m, 2*m:3*m]
    a32 = a[m:2*m, 2*m:3*m]
    a33 = a[2*m:3*m, 2*m:3*m]
    a34 = a[3*m:4*m, 2*m:3*m]
    a35 = a[4*m:5*m, 2*m:3*m]
    
    #row 4
    
    a41 = a[0:m, 3*m:4*m]
    a42 = a[m:2*m, 3*m:4*m]
    a43 = a[2*m:3*m, 3*m:4*m]
    a44 = a[3*m:4*m, 3*m:4*m]
    a45 = a[4*m:5*m, 3*m:4*m]
    
    #row 5
    
    a51 = a[0:m, 4*m:5*m]
    a52 = a[m:2*m, 4*m:5*m]
    a53 = a[2*m:3*m, 4*m:5*m]
    a54 = a[3*m:4*m, 4*m:5*m]
    a55 = a[4*m:5*m, 4*m:5*m]
      
    return (a11, a12, a13, a14, a15,
            a21, a22, a23, a24, a25,
            a31, a32, a33, a34, a35,
            a41, a42, a43, a44, a45,
            a51, a52, a53, a54, a55)



#divide into 20 submatrixes
def div4x5(a):
    
    col = len(a)/4
    row = len(a[1])/5
    
    a11 = a[0:row, 0:col]
    a12 = a[row:2*row, 0:col]
    a13 = a[2*row:3*row, 0:col]
    a14 = a[3*row:4*row, 0:col]
    a15 = a[4*row:5*row, 0:col]
    
    a21 = a[0:row, col:2*col]
    a22 = a[row:2*row, col:2*col]
    a23 = a[2*row:3*row, col:2*col]
    a24 = a[3*row:4*row, col:2*col]
    a25 = a[4*row:5*row, col:2*col]
    
    a31 = a[0:row, 2*col:3*col]
    a32 = a[row:2*row, 2*col:3*col]
    a33 = a[2*row:3*row, 2*col:3*col]
    a34 = a[3*row:4*row, 2*col:3*col] 
    a35 = a[4*row:5*row, 2*col:3*col]
    
    a41 = a[0:row, 3*col:4*col]
    a42 = a[row:2*row, 3*col:4*col]
    a43 = a[2*row:3*row, 3*col:4*col]
    a44 = a[3*row:4*row, 3*col:4*col]
    a45 = a[4*row:5*row, 3*col:4*col]
    
    return (a11, a12, a13, a14, a15,
            a21, a22, a23, a24, a25,
            a31, a32, a33, a34, a35,
            a41, a42, a43, a44, a45)

#divide mat into 16 smaller mats
#to 4x4

def div4x4(a):
    
    m = int(len(a)/4)
    
    #row 1
    
    a11 = a[0:m, 0:m]
    a12 = a[m:2*m, 0:m]
    a13 = a[2*m:3*m, 0:m]
    a14 = a[3*m:4*m, 0:m]
    
    #row 2
    
    a21 = a[0:m, m:2*m]
    a22 = a[m:2*m, m:2*m]
    a23 = a[2*m:3*m, m:2*m]
    a24 = a[3*m:4*m, m:2*m]
    
    
    #row 3
    
    a31 = a[0:m, 2*m:3*m]
    a32 = a[m:2*m, 2*m:3*m]
    a33 = a[2*m:3*m, 2*m:3*m]
    a34 = a[3*m:4*m, 2*m:3*m]
    
    #row 4
    
    a41 = a[0:m, 3*m:4*m]
    a42 = a[m:2*m, 3*m:4*m]
    a43 = a[2*m:3*m, 3*m:4*m]
    a44 = a[3*m:4*m, 3*m:4*m]


    return (a11, a12, a13, a14,
            a21, a22, a23, a24, 
            a31, a32, a33, a34, 
            a41, a42, a43, a44)


#strassen

def mat2x2(a, b):
    
    if True:
        a11, a12, a21, a22 = div2x2(a)
        b11, b12, b21, b22 = div2x2(b)
        
        m1 = mat2x2(a11 + a22, b11 + b22)
        m2 = mat2x2(a21 + a22, b11)
        m3 = mat2x2(a11, b12 - b22)
        m4 = mat2x2(a22, b21 - b11)
        m5 = mat2x2(a11 + a12, b22)
        m6 = mat2x2(a21 - a11, b11 + b12)
        m7 = mat2x2(a12 - a22, b21 + b22)
        
        c11 = m1 + m4 - m5 + m7
        c12 = m3 + m5
        c21 = m2 + m4
        c22 = m1 - m2 + m3 + m6
        
        result = np.concatenate((np.concatenate((c11, c21), axis=0), np.concatenate((c12, c22), axis=0)), axis=1)
        return result   
        
    elif False:
        return
    else:
        matnaive(a,b)


#4x5

def mat455(a,b):
    
    
    #FIX TmIS BECAUSE IT mAS TO BE 4x5 * 5x5
    if(len(a)>1):
        
        #submatrixes
        a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45 = div4x5(a)
        b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45, b51, b52, b53, b54, b55 = div5x5(b)
    
        m1 = mat455(a32, -b21 - b25 - b31)
        m2 = mat455(a22 + a25 - a35, -b25 - b51)
        m3 = mat455(-a31 - a41 + a42, -b11 + b25)
        m4 = mat455(a12 + a14 + a34, -b25 - b41)
        m5 = mat455(a15 + a22 + a25, -b24 + b51)
        m6 = mat455(-a22 - a25 - a45, b23 + b51)
        m7 = mat455(-a11 + a41 - a42, b11 + b24)
        m8 = mat455(a32 - a33 - a43, -b23 + b31)
        m9 = mat455(-a12 - a14 + a44, b23 + b41)
        m10 = mat455(a22 + a25, b51)
        m11 = mat455(-a21 - a41 + a42, -b11 + b22)
        m12 = mat455(a41 - a42, b11)
        m13 = mat455(a12 + a14 + a24, b22 + b41)
        m14 = mat455(a13 - a32 + a33, b24 + b31)
        m15 = mat455(-a12 - a14, b41)
        m16 = mat455(-a32 + a33, b31)
        m17 = mat455(a12 + a14 - a21 + a22 - a23 + a24 - a32 + a33 - a41 + a42, b22)
        m18 = mat455(-a21, b11 + b12 + b52)
        m19 = mat455(-a23, b31 + b32 + b52)
        m20 = mat455(-a15 + a21 + a23 - a25, -b11 - b12 + b14 - b52)
        m21 = mat455(a21 + a23 - a25, b52)
        m22 = mat455(a13 - a14 - a24, b11 + b12 - b14 - b31 - b32 + b34 + b44)
        m23 = mat455(a13, -b31 + b34 + b44)
        m24 = mat455(a15, -b44 - b51 + b54)
        m25 = mat455(-a11, b11 - b14)
        m26 = mat455(-a13 + a14 + a15, b44)
        m27 = mat455(a13 - a31 + a33, b11 - b14 + b15 + b35)
        m28 = mat455(-a34, -b35 - b41 - b45)
        m29 = mat455(a31, b11 + b15 + b35)
        m30 = mat455(a31 - a33 + a34, b35)
        m31 = mat455(-a14 - a15 - a34, -b44 - b51 - b54 - b55)
        m32 = mat455(a21 + a41 + a44, b13 - b41 - b42 - b43)
        m33 = mat455(a43, -b31 - b33)
        m34 = mat455(a44, -b13 + b41 + b43)
        m35 = mat455(-a45, b13 + b51 + b53)
        m36 = mat455(a23 - a25 - a45, b31 + b32 + b33 + b52)
        m37 = mat455(-a41 - a44 + a45, b13)
        m38 = mat455(-a23 - a31 + a33 - a34, b35 + b41 + b42 + b45)
        m39 = mat455(-a31 + a41 - a44 + a45, -b13 + b51 + b53 + b55)
        m40 = mat455(-a13 + a14 + a15 - a44, -b31 - b33 + b34 + b44)
        m41 = mat455(-a11 + a41 - a45, b13 + b31 + b33 - b34 + b51 + b53 - b54)
        m42 = mat455(-a21 + a25 - a35, -b11 - b12 - b15 + b41 + b42 + b45 - b52)
        m43 = mat455(a24, b41 + b42)
        m44 = mat455(a23 + a32 - a33, b22 - b31)
        m45 = mat455(-a33 + a34 - a43, b35 + b41 + b43 + b45 + b51 + b53 + b55)
        m46 = mat455(-a35, -b51 - b55)
        m47 = mat455(a21 - a25 - a31 + a35, b11 + b12 + b15 - b41 - b42 - b45)
        m48 = mat455(-a23 + a33, b22 + b32 + b35 + b41 + b42 + b45)
        m49 = mat455(-a11 - a13 + a14 + a15 - a21 - a23 + a24 + a25, -b11 - b12 + b14)
        m50 = mat455(-a14 - a24, b22 - b31 - b32 + b34 - b42 + b44)
        m51 = mat455(a22, b21 + b22 - b51)
        m52 = mat455(a42, b11 + b21 + b23)
        m53 = mat455(-a12, -b21 + b24 + b41)
        m54 = mat455(a12 + a14 - a22 - a25 - a32 + a33 - a42 + a43 - a44 - a45, b23)
        m55 = mat455(a14 - a44, -b23 + b31 + b33 - b34 + b43 - b44)
        m56 = mat455(a11 - a15 - a41 + a45, b31 + b33 - b34 + b51 + b53 - b54)
        m57 = mat455(-a31 - a41, -b13 - b15 - b25 - b51 - b53 - b55)
        m58 = mat455(-a14 - a15 - a34 - a35, -b51 + b54 - b55)
        m59 = mat455(-a33 + a34 - a43 + a44, b41 + b43 + b45 + b51 + b53 + b55)
        m60 = mat455(a25 + a45, b23 - b31 - b32 - b33 - b52 - b53)
        m61 = mat455(a14 + a34, b11 - b14 + b15 - b25 - b44 + b45 - b51 + b54 - b55)
        m62 = mat455(a21 + a41, b12 + b13 + b22 - b41 - b42 - b43)
        m63 = mat455(-a33 - a43, -b23 - b33 - b35 - b41 - b43 - b45)
        m64 = mat455(a11 - a13 - a14 + a31 - a33 - a34, b11 - b14 + b15)
        m65 = mat455(-a11 + a41, -b13 + b14 + b24 - b51 - b53 + b54)
        m66 = mat455(a11 - a12 + a13 - a15 - a22 - a25 - a32 + a33 - a41 + a42, b24)
        m67 = mat455(a25 - a35, b11 + b12 + b15 - b25 - b41 - b42 - b45 + b52 + b55)
        m68 = mat455(a11 + a13 - a14 - a15 - a41 - a43 + a44 + a44, -b31 - b33 + b34)
        m69 = mat455(-a13 + a14 - a23 + a24, -b24 - b31 - b32 + b34 - b52 + b54)
        m70 = mat455(a23 - a25 + a43 - a45, -b31 - b32 - b33)
        m71 = mat455(-a31 + a33 - a34 + a35 - a41 + a43 - a44 + a45, -b51 - b53 - b55)
        m72 = mat455(-a21 - a24 - a41 - a44, b41 + b42 + b43)
        m73 = mat455(a13 - a14 - a15 + a23 - a24 - a25, b11 + b12 - b14 + b24 + b52 - b54)
        m74 = mat455(a21 - a23 + a24 - a31 + a33 - a34, b41 + b42 + b45)
        m75 = -mat455(a12 + a14 - a22 - a25 - a31 + a32 + a34 + a35 - a41 + a42, b25)
        m76 = mat455(a13 + a33, -b11 + b14 - b15 + b24 + b34 - b35)
        
        
        #build res matrix
        
        c11 = -m10 + m12 + m14 - m15 - m16 + m53 + m5 - m66 - m7
        c21 = m10 + m11 - m12 + m13 + m15 + m16 - m17 - m44 + m51
        c31 = m10 - m12 + m15 + m16 - m1 + m2 + m3 - m4 + m75
        c41 = -m10 + m12 - m15 - m16 + m52 + m54 - m6 - m8 + m9
        
        c12 = m13 + m15 + m20 + m21 - m22 + m23 + m25 - m43 + m49 + m50
        c22 = -m11 + m12 - m13 - m15 - m16 + m17 + m18 - m19 - m21 + m34 + m44
        c32 = -m16 - m19 - m21 - m28 - m29 - m38 + m42 + m44 - m47 + m48
        c42 = m11 - m12 - m18 + m21 - m32 + m33 - m34 - m36 + m62 - m70
        
        c13 = m15 + m23 + m24 + m34 - m37 + m40 - m41 + m55 - m56 - m9
        c23 = -m10 + m19 + m32 + m35 + m36 + m37 - m43 - m60 - m6 - m72
        c33 = -m16 - m28 + m33 + m37 - m39 + m45 - m46 + m63 - m71 - m8
        c43 = m10 + m15 + m16 - m33 + m34 - m35 - m37 - m54 + m6 + m8 - m9
        
        c14 = -m10 + m12 + m14 - m16 + m23 + m24 + m25 + m26 + m5 - m66 - m7
        c24 = m10 + m18 - m19 + m20 - m22 - m24 - m26 - m5 - m69 + m73
        c34 = -m14 + m16 - m23 - m26 + m27 + m29 + m31 + m46 - m58 + m76
        c44 = m12 + m25 + m26 - m33 - m35 - m40 + m41 + m65 - m68 - m7
        
        c15 = m15 + m24 + m25 + m27 - m28 + m30 + m31 - m4 + m61 + m64
        c25 = -m10 - m18 - m2 - m30 - m38 + m42 - m43 + m46 + m67 + m74
        c35 = -m10 + m12 - m15 + m28 + m29 - m2 - m30 - m3 + m46 + m4 - m75
        c45 = -m12 - m29 + m30 - m34 + m35 + m39 + m3 - m45 + m57 + m59


        result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0)), np.concatenate((c14, c24, c34, c44), axis=0), np.concatenate((c15, c25, c35, c45), axis=0)
, axis=1)
    
    
        return result
    
    elif False:
        return
    
    else:
        return matnaive(a, b)
                                                                                                                                                                                                                
       
        
#4x4 z2

def mat444(a,b):

    #FIX LATER FOR LARGER NUM
    if(len(a) > 1):
        
        #submatrixes
        a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44 = div4x4(a)
        b11, b12, b13, b14, b21, b22, b23, b24, b31, b32, b33, b34, b41, b42, b43, b44 = div4x4(b)
        
        
        
        #multiply matrixes
        
        m1 = mat444(a11, b13)
        m2 = mat444(a11 ^ a31 ^ a33, b11 ^ b31 ^ b33)
        m3 = mat444(a11 ^ a31 ^ a34, b12 ^ b42 ^ b43)
        m4 = mat444(a13 ^ a21 ^ a23, b13 ^ b14 ^ b34)
        m5 = mat444(a11 ^ a31, b11 ^ b12 ^ b13 ^ b31 ^ b33 ^ b42 ^ b43)
        m6 = mat444(a13 ^ a23, b13 ^ b14 ^ b32 ^ b33 ^ b34 ^ b42 ^ b43)
        m7 = mat444(a14 ^ a43 ^ a44, b31 ^ b33 ^ b41)
        m8 = mat444(a14 ^ a41 ^ a44, b13 ^ b14 ^ b44)
        m9 = mat444(a13 ^ a23 ^ a24, b32 ^ b42 ^ b43)
        m10 = mat444(a14 ^ a44, b13 ^ b14 ^ b31 ^ b33 ^ b41 ^ b43 ^ b44)
        m11 = mat444(a33, b11 ^ b22 ^ b23 ^ b31 ^ b32)
        m12 = mat444(a12 ^ a32 ^ a33, b22 ^ b23 ^ b32)
        m13 = mat444(a34, b12 ^ b21 ^ b23 ^ b41 ^ b42)
        m14 = mat444(a12 ^ a32, b21 ^ b22 ^ b23 ^ b32 ^ b41)
        m15 = mat444(a12 ^ a32 ^ a34, b21 ^ b23 ^ b41)
        m16 = mat444(a21, b12 ^ b14 ^ b22 ^ b23 ^ b34)
        m17 = mat444(a12 ^ a21 ^ a22, b12 ^ b22 ^ b23)
        m18 = mat444(a12 ^ a22, b12 ^ b22 ^ b23 ^ b24 ^ b44)
        m19 = mat444(a24, b23 ^ b24 ^ b32 ^ b42 ^ b44)
        m20 = mat444(a12 ^ a23 ^ a24 ^ a32 ^ a33, b32)
        m21 = mat444(a12 ^ a22 ^ a24, b23 ^ b24 ^ b44)
        m22 = mat444(a43, b23 ^ b24 ^ b31 ^ b34 ^ b41)
        m23 = mat444(a12 ^ a13 ^ a14 ^ a23 ^ a24 ^ a31 ^ a34, b42 ^ b43)
        m24 = mat444(a12 ^ a42 ^ a43, b23 ^ b24 ^ b34)
        m25 = mat444(a12 ^ a42, b11 ^ b21 ^ b23 ^ b24 ^ b34)
        m26 = mat444(a12 ^ a41 ^ a42, b11 ^ b21 ^ b23)
        m27 = mat444(a14, b43)
        m28 = mat444(a12 ^ a21 ^ a22 ^ a31 ^ a34, b12)
        m29 = mat444(a12 ^ a21 ^ a23 ^ a42 ^ a43, b34)
        m30 = mat444(a12 ^ a21 ^ a23 ^ a42 ^ a43, b11)
        m31 = mat444(a41, b11 ^ b14 ^ b21 ^ b23 ^ b44)
        m32 = mat444(a12 ^ a32 ^ a34 ^ a43 ^ a44, b41)
        m33 = mat444(a12 ^ a22 ^ a24 ^ a41 ^ a44, b44)
        m34 = mat444(a21 ^ a31 ^ a41, b11 ^ b12 ^ b14)
        m35 = mat444(a12 ^ a21 ^ a22 ^ a32 ^ a33, b23 ^ b24 ^ b32 ^ b41)
        m36 = mat444(a12 ^ a24 ^ a32 ^ a43, b23 ^ b24 ^ b32 ^ b41)
        m37 = mat444(a12 ^ a21 ^ a33 ^ a42, b11 ^ b22 ^ b23 ^ b34)
        m38 = mat444(a22 ^ a32 ^ a42, b21 ^ b22 ^ b24)
        m39 = mat444(a12, b23)
        m40 = mat444(a13, b33)
        m41 = mat444(a11 ^ a13 ^ a14 ^ a21 ^ a23 ^ a41 ^ a44, b13 ^ b14)
        m42 = mat444(a12 ^ a32 ^ a34 ^ a41 ^ a42, b21 ^ b23)
        m43 = mat444(a24 ^ a34 ^ a44, b41 ^ b42 ^ b44)
        m44 = mat444(a23 ^ a33 ^ a43, b31 ^ b32 ^ b34)
        m45 = mat444(a11 ^ a13 ^ a14 ^ a31 ^ a33 ^ a43 ^ a44, b31 ^ b33)
        m46 = mat444(a12 ^ a22 ^ a34 ^ a41, b12 ^ b21 ^ b23 ^ b44)
        m47 = mat444(a12 ^ a22 ^ a24 ^ a42 ^ a43, b23 ^ b24)
        
        
        #make parts of final matrix
        
        c11 = m15 ^ m26 ^ m2 ^ m30 ^ m32 ^ m39 ^ m40 ^ m42 ^ m45 ^ m7
        c21 = m11 ^ m12 ^ m14 ^ m20 ^ m22 ^ m24 ^ m25 ^ m29 ^ m35 ^ m36 ^ m37 ^ m38 ^ m44 ^ m47
        c31 = m11 ^ m12 ^ m14 ^ m15 ^ m26 ^ m30 ^ m39 ^ m42
        c41 = m15 ^ m22 ^ m24 ^ m25 ^ m26 ^ m32 ^ m39 ^ m42
        
        c12 = m12 ^ m17 ^ m20 ^ m23 ^ m27 ^ m28 ^ m35 ^ m39 ^ m3 ^ m9
        c22 = m12 ^ m17 ^ m18 ^ m19 ^ m20 ^ m21 ^ m35 ^ m39
        c32 = m12 ^ m13 ^ m14 ^ m15 ^ m17 ^ m28 ^ m35 ^ m39
        c42 = m13 ^ m14 ^ m15 ^ m18 ^ m19 ^ m21 ^ m32 ^ m33 ^ m36 ^ m38 ^ m42 ^ m43 ^ m46 ^ m47
        
        c13 = m1 ^ m27 ^ m39 ^ m40
        c23 = m16 ^ m17 ^ m18 ^ m19 ^ m21 ^ m39 ^ m40 ^ m4 ^ m6 ^ m9
        c33 = m11 ^ m12 ^ m13 ^ m14 ^ m15 ^ m1 ^ m2 ^ m39 ^ m3 ^ m5
        c43 = m10 ^ m22 ^ m24 ^ m25 ^ m26 ^ m27 ^ m31 ^ m39 ^ m7 ^ m8
        
        c14 = m1 ^ m21 ^ m24 ^ m29 ^ m33 ^ m39 ^ m41 ^ m47 ^ m4 ^ m8
        c24 = m16 ^ m17 ^ m18 ^ m21 ^ m24 ^ m29 ^ m39 ^ m47
        c34 = m16 ^ m17 ^ m18 ^ m25 ^ m26 ^ m28 ^ m30 ^ m31 ^ m34 ^ m35 ^ m37 ^ m38 ^ m42 ^ m46
        c44 = m21 ^ m24 ^ m25 ^ m26 ^ m31 ^ m33 ^ m39 ^ m47      
        
        
        #combine to big matrix
        
        result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0), np.concatenate((c14, c24, c34, c44), axis=0)), axis=1)
        
        
        return result
    
    else:
        
        return a*b
        #return matnaive(a,b)
        


#decide wmat algoritmm to use :3

def multdecide():
    
    
    
    return