import numpy as np


#strassenMod2

def strassen(a,b,depth,m,n):
    
    if depth < 1:
        return a @ b
    
    
    P1 = strassen(a[0:m,0:m],b[0:m,m:n]-b[m,m<<1:m,m<<1], depth-1, m>>1,m)
    P2 = strassen(a[0:m,0:m]+a[0:m,m,m<<1],b[m,m<<1:m,m<<1], depth-1, m>>1,m)
    P3 = strassen(a[m:n,0:m]+a[m:n,m:n],b[0:m,0:m], depth-1, m>>1,m)
    P4 = strassen(a[m:n,m:n],b[m:n,0:m]-b[0:m,0:m], depth-1, m>>1,m)
    P5 = strassen(a[0:m,0:m]+a[m:n,m:n],b[0:m,0:m]+b[m:n,m:n],depth-1,m>>1,m)
    P6 = strassen(a[0:m,m:n]-a[m:n,m:n],b[m:n,0:m]+b[m:n,m:n],depth-1,m>>1,m)
    P7 = strassen(a[0:m,0:m]-a[m:n,0:m],b[0:m,0:m]+b[0:m,m:n],depth-1,m>>1,m)  
    
    c11 = P5 + P4 - P2 + P6
    c21 = P3 + P4
    c12 = P1 + P2
    c22 = P5 + P1 - P3 - P7
    
    c = np.concatenate((np.concatenate((c11, c21), axis=0), np.concatenate((c12, c22), axis=0)), axis=1)
  
    return c


def strassenMod2(a,b,depth,m,n):
    
    if depth < 1:
        return a @ b
    
    
    P1 = strassenMod2(a[0:m,0:m],b[0:m,m:n]^b[m,m<<1:m,m<<1], depth-1, m>>1,m)
    P2 = strassenMod2(a[0:m,0:m]^a[0:m,m,m<<1],b[m,m<<1:m,m<<1], depth-1, m>>1,m)
    P3 = strassenMod2(a[m:n,0:m]^a[m:n,m:n],b[0:m,0:m], depth-1, m>>1,m)
    P4 = strassenMod2(a[m:n,m:n],b[m:n,0:m]^b[0:m,0:m], depth-1, m>>1,m)
    P5 = strassenMod2(a[0:m,0:m]^a[m:n,m:n],b[0:m,0:m]^b[m:n,m:n],depth-1,m>>1,m)
    P6 = strassenMod2(a[0:m,m:n]^a[m:n,m:n],b[m:n,0:m]^b[m:n,m:n],depth-1,m>>1,m)
    P7 = strassenMod2(a[0:m,0:m]^a[m:n,0:m],b[0:m,0:m]^b[0:m,m:n],depth-1,m>>1,m)  
    
    c11 = P5 ^ P4 ^ P2 ^ P6
    c21 = P3 ^ P4
    c12 = P1 ^ P2
    c22 = P5 ^ P1 ^ P3 ^ P7
    
    c = np.concatenate((np.concatenate((c11, c21), axis=0), np.concatenate((c12, c22), axis=0)), axis=1)
  
    return c

def strassenInit(a,b,mod2):
      
    if len(a) == len(b) and len(b) == len(b[0]):  
        n = len(a)
        m = n>>1
        depth = 0
        #get log2 div
        #edit later
        while not(n & 1) and n>=32:
            depth += 1
            n = n >> 1
        
        if depth != 0:
            if mod2:
                return strassenMod2(a,b,depth,m,m<<1)
            return strassen(a,b,depth,m,m<<1)
        else:
            return a @ b
    else:
        return a @ b

    
## UNUSED & NEVER FINISHED
# def strassenIt(a,b,depth,m):
    
#     n = m << 1
#     P = np.zeros([depth,7,m,m])
#     c = np.zeros([n,n])
#     ax = np.zeros([depth,n,n])
#     bx = np.zeros([depth,n,n])
#     cx = np.zeros([depth,n,n])
    
#     #individual Ps
#     for x in range(7):
#         #recurssion layer
#         for y in range(depth,-1,-1):
            
#             if y == depth:
#                 #do regular matmulfor deepest layer
#                 True
                
#             else:
#                 #do strassen for other layers
#                 False
    
    
    
    
#     c[0:m,0:m] = P[4] + P[3] - P[1] + P[5]
#     c[0:m,m:n] = P[0] + P[1]
#     c[m:n,0:m] = P[2] + P[3]
#     c[m:n,m:n] = P[4] + P[0] - P[3] - P[6]
    
    
#     return c
    

###THE FOLLOWING WAS GENERATED WITH SCRIPTS


def div3x4(a):

	col = len(a)//3
	row = len(a[1])//4

	#row 1

	a11 = a[0:row,0:col]
	a12 = a[row:1*row,0:col]
	a13 = a[2*row:3*row,0:col]
	a14 = a[3*row:4*row,0:col]
	#row 2

	a21 = a[0:row,col:1*col]
	a22 = a[row:1*row,col:1*col]
	a23 = a[2*row:3*row,col:1*col]
	a24 = a[3*row:4*row,col:1*col]
	#row 3

	a31 = a[0:row,2*col:3*col]
	a32 = a[row:1*row,2*col:3*col]
	a33 = a[2*row:3*row,2*col:3*col]
	a34 = a[3*row:4*row,2*col:3*col]

	return (a11, a12, a13, a14, 
	  a21, a22, a23, a24, 
	  a31, a32, a33, a34)

def div4x5(a):

	col = len(a)//4
	row = len(a[1])//5

	#row 1

	a11 = a[0:row,0:col]
	a12 = a[row:1*row,0:col]
	a13 = a[2*row:3*row,0:col]
	a14 = a[3*row:4*row,0:col]
	a15 = a[4*row:5*row,0:col]
	#row 2

	a21 = a[0:row,col:1*col]
	a22 = a[row:1*row,col:1*col]
	a23 = a[2*row:3*row,col:1*col]
	a24 = a[3*row:4*row,col:1*col]
	a25 = a[4*row:5*row,col:1*col]
	#row 3

	a31 = a[0:row,2*col:3*col]
	a32 = a[row:1*row,2*col:3*col]
	a33 = a[2*row:3*row,2*col:3*col]
	a34 = a[3*row:4*row,2*col:3*col]
	a35 = a[4*row:5*row,2*col:3*col]
	#row 4

	a41 = a[0:row,3*col:4*col]
	a42 = a[row:1*row,3*col:4*col]
	a43 = a[2*row:3*row,3*col:4*col]
	a44 = a[3*row:4*row,3*col:4*col]
	a45 = a[4*row:5*row,3*col:4*col]

	return (a11, a12, a13, a14, a15, 
	  a21, a22, a23, a24, a25, 
	  a31, a32, a33, a34, a35, 
	  a41, a42, a43, a44, a45)

def mat345(a,b,depth):

	a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34 = div3x4(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45 = div4x5(b)


	if depth == 0:
		return strassenInit(a,b,True)
	else:
		m1 =mat345( -a32+a33+a14-a24,b21-b22+b42-b23+b43-b24-b25, depth-1)
		m2 =mat345( -a31-a33+a34,-b21+b22+b23+b24+b44+b45, depth-1)
		m3 =mat345( -a31-a33+a24,-b11-b21+b12+b22+b13+b23+2*b14+b24+b44+b15+b45, depth-1)
		m4 =mat345( a23-a33,b11-b31-b12+b32-b13+b33-2*b14+2*b34-b15+b35, depth-1)
		m5 =mat345( -a11+a12-a32-a23+a24,b23+b33+b24+b34+b25+b35, depth-1)
		m6 =mat345( a31,-b11+b31+b12-b32+b13+b43+2*b14-b34+b44+2*b15-b25-b35+b45, depth-1)
		m7 =mat345( a11-a22+a23-a24,b11-b31-b12+b32-b13+b23+b33-b14+b34-b15+b25+b35, depth-1)
		m8 =mat345( -a11+a12+a32-2*a13-a33+a24,b11-b31-b14+b34-b15+b35, depth-1)
		m9 =mat345( a24-a34,b21-b41-b22+b42-b23+b43-b24+b44, depth-1)
		m10 =mat345( a11-a21,b11-b31-b12+b32-2*b13+b33-2*b14-b24+b34-2*b15+b35, depth-1)
		m11 =mat345( -a21+a22-a32-a23+a24,-b21+b22+b23+2*b24+b25, depth-1)
		m12 =mat345( a11+a13,-b11-b31-2*b41-b22+b32+2*b42-b23+b43+b14+b34+2*b44+b15+b45, depth-1)
		m13 =mat345( a21-a31,b11-b31-b12-b22-b13-b23-b14+b34, depth-1)
		m14 =mat345( a33-a24,-b11+b31+b12-b32+b13+b43+2*b14-b34+b44+b15+b45, depth-1)
		m15 =mat345( -a11+a12-a32-a13+a33+a14-a34,b11-b31-b12+b32-b14+b34-b15+b25+b35, depth-1)
		m16 =mat345( -a11+a12+a32-a13-a33+a24,b11-b21-b31-b14+b24+b34-b15+b25+b35, depth-1)
		m17 =mat345( -a31-a33+a14-a24+a34,b21+b31-b22-b32-b23+b43-b24-b34-b25-b35, depth-1)
		m18 =mat345( -a11-a23+a24,b11-b31-b12+b32-b13-b23-2*b14-b24+b34-b15-b25, depth-1)
		m19 =mat345( a11+a13-a14+a24-a34,-b11+b21-2*b41+b12-b22+2*b42-b23+b43+b14-b24+2*b44+b15+b45, depth-1)
		m20 =mat345( -a11+a21-a13+a23,-b21-b31+b22+b32+b23+b33+b24+b34+b25+b35, depth-1)
		m21 =mat345( a11-a31-a12+a32+a13-a33-a14+a34,-b11+b31+b12-b32+b43+b14-b34+b44+b15-b25-b35+b45, depth-1)
		m22 =mat345( a11-a12+a13+a33-a24,b11-b21-b31+b33+b43-b14+b24+2*b34+b44-b15+b25+2*b35+b45, depth-1)
		m23 =mat345( a22-a23+a24,b12+b22+b13+b23, depth-1)
		m24 =mat345( -a32+a33,-b11+b21+b31-b22+b42-b23+b33+2*b43+b14-b24+b44+b15-b25+b45, depth-1)
		m25 =mat345( a32-a33+a34,b21-b22+b42-b23+b43-b24, depth-1)
		m26 =mat345( -a21+a31+a22-a32-a23+a33+a24-a34,-b21+b22+b23+b24, depth-1)
		m27 =mat345( a11-a12+a32+2*a13-a33-2*a14+a24,b11-b31-b12+b32-b14+b34-b15+b35, depth-1)
		m28 =mat345( -a21+a22-a23-a33+a24,b11-b21-b31+b22+b32+b23+b33-b14+b24+b34-b15+b25+b35, depth-1)
		m29 =mat345( -a11+a12-a32-a13+a14,-b21+b22+b43+b24+b44+b45, depth-1)
		m30 =mat345( a24,-b31-b41+b32+b42+b34+b44, depth-1)
		m31 =mat345( -a31-a33,-b11+b21+b31-b22-b32-b23+b43+b14-b24-b34+b15-b25-b35, depth-1)
		m32 =mat345( -a23+a33,b22+b32+b23+b33, depth-1)
		m33 =mat345( -a11+a12-a32-a13+a24,b33+b43+b34+b44+b35+b45, depth-1)
		m34 =mat345( a14-a24+a34,-b21-b31-b41+b22+b32+b23-b43+b24+b34+b44+b25+b35+b45, depth-1)
		m35 =mat345( a21+a23-a24,-b11-b21+b12+b22+b13+b23+2*b14+2*b24+b15+b25, depth-1)
		m36 =mat345( a21-a22+a23-a24,b11-b21-b31-b12+b22+b32-b13+b23+b33-b14+b24+b34-b15+b25+b35, depth-1)
		m37 =mat345( -a11-a13+a24,b21-b31-2*b41-b22+b32+2*b42-b23+b43-b24+b34+2*b44-b25+b45, depth-1)
		m38 =mat345( -a11-a13+a14,2*b21-2*b41-2*b22+2*b42-b23+b43-2*b24+2*b44-b25+b45, depth-1)
		m39 =mat345( -a14+a24,b21-b41-b22+b42-b23+b43-b24+b44-b25+b45, depth-1)
		m40 =mat345( -a21+a31-a23+a33,-b21-b31+b24+b34, depth-1)
		m41 =mat345( a11-a12+a13-a14,-b21+b22+b24, depth-1)
		m42 =mat345( -a12+a22+a13-a23-a14+a24,b23+b25, depth-1)
		m43 =mat345( a11-a22+a13+a23-a24,b11-b31+b22+b32+b23+b33-b14+b34-b15+b35, depth-1)
		m44 =mat345( a32-a33+a24,-b22+b42-b23+b43, depth-1)
		m45 =mat345( a21-a31-a22+a23-a24,-b21+b12+b22+b13+b23+b24, depth-1)
		m46 =mat345( a11,b11-b31-b12+b32-b14+b34, depth-1)
		m47 =mat345( a32,-b11+b31+b22+b23+b33+b43+b14+b24+b44+b15+b45, depth-1)
		
		c11 = m19+m15+m18-2*m12-m14+2*m1+m4+m5+m7+m8-m9+m41+m42-m43+m44+m46+m47+m34-2*m37+m38+2*m39+m27+m29+2*m30+m22-m23+m25
		c12 = 2*m1+m8-m9-m12+m15-m16+m19+m25+m27+m30+m34-m37+m38+m39-m41+m44
		c13 = -m1-m7+m9+m12-m15-m19+m23-m25-m27-m30-m34+m37-m38-m39-m42+m43
		c14 = m4+m5+m7-m12-m14+m16+m18+m22-m23+m29+2*m30-2*m37+m38+2*m39+m41+m42-m43+m47
		c15 = m1-m9+m15+m19+m25+m27-m30+m34+m37-m39+m46
		c21 = m3+m4+m6+m11-m12+m13-m20+m24+m30+m31+m35+m36-m37+m40-m43+m44+m45+m47
		c22 = m3+m6+m7-m10+m13+m14-m16-m18-m22+m23+m24+m31-m33+m35-m36+m40+m44+m45-m46
		c23 = -m3-m6-m7+m10-m13-m14+m18-m28-m31-m32-m35-m40-m45+m46
		c24 = m4+m11-m12-m14+m16-m20+m22-m23+2*m30+m33+m35+m36-m37-m43+m47
		c25 = m3+m6+m12+m13+m14+m20+m23+m28-2*m30+m31+m32+m37+m40+m43+m45
		c31 = -m1+m2+m6-m17+m24+m26+m28+2*m31-m34+m36-m39+m45+m47
		c32 = m2+m15-m16-m21-m22+m24+m25-m29+m31-m33-m41
		c33 = -m2-m15+m21-m26-m28+m29-m31-m36+m41-m45
		c34 = -m1+m2-m3-m9-m14+m16-m17+m22-m25+m26+m28+m30+m31+m33-m34+m36-m39+m45+m47
		c35 = m1+m3+m6+m9+m14+m17+m25-m30+m34+m39

	result = np.concatenate((np.concatenate((c11, c21, c31), axis=0), np.concatenate((c12, c22, c32), axis=0), np.concatenate((c13, c23, c33), axis=0), np.concatenate((c14, c24, c34), axis=0), np.concatenate((c15, c25, c35), axis=0)), axis=1)

	return result



def div4x4(a):

	col = len(a)//4
	row = len(a[1])//4

	#row 1

	a11 = a[0:row,0:col]
	a12 = a[row:1*row,0:col]
	a13 = a[2*row:3*row,0:col]
	a14 = a[3*row:4*row,0:col]
	#row 2

	a21 = a[0:row,col:1*col]
	a22 = a[row:1*row,col:1*col]
	a23 = a[2*row:3*row,col:1*col]
	a24 = a[3*row:4*row,col:1*col]
	#row 3

	a31 = a[0:row,2*col:3*col]
	a32 = a[row:1*row,2*col:3*col]
	a33 = a[2*row:3*row,2*col:3*col]
	a34 = a[3*row:4*row,2*col:3*col]
	#row 4

	a41 = a[0:row,3*col:4*col]
	a42 = a[row:1*row,3*col:4*col]
	a43 = a[2*row:3*row,3*col:4*col]
	a44 = a[3*row:4*row,3*col:4*col]

	return (a11, a12, a13, a14, 
	  a21, a22, a23, a24, 
	  a31, a32, a33, a34, 
	  a41, a42, a43, a44)

def mat444mod2(a,b,depth):

	a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44 = div4x4(a)
	b11, b12, b13, b14, b21, b22, b23, b24, b31, b32, b33, b34, b41, b42, b43, b44 = div4x4(b)


	if depth == 0:
		return strassenInit(a,b,False)
	else:
		m1 =mat444mod2( a14,b31^b12^b22^b42^b13^b23^b33^b43^b14^b24^b34^b44, depth-1)
		m2 =mat444mod2( a41^a42^a23^a43^a14,b31^b12^b22^b42^b13^b23^b33^b43^b34, depth-1)
		m3 =mat444mod2( a41^a43^a44,b11^b21^b41^b12^b22^b42^b24^b34, depth-1)
		m4 =mat444mod2( a11^a33^a14,b11^b31^b12^b32, depth-1)
		m5 =mat444mod2( a41^a22^a24^a34^a44,b11^b21^b22^b32^b42^b43^b14^b24, depth-1)
		m6 =mat444mod2( a42^a43,b21^b31^b12^b22^b42^b13^b33^b43^b24^b34, depth-1)
		m7 =mat444mod2( a33,b11^b21^b12^b32^b23^b33^b24^b34, depth-1)
		m8 =mat444mod2( a11^a21^a31^a23^a14,b12^b32, depth-1)
		m9 =mat444mod2( a41^a12^a33^a43^a14,b21^b31^b23^b33^b24^b34, depth-1)
		m10 =mat444mod2( a41^a23^a24^a34^a44,b11^b21^b41^b22^b32^b42^b14^b24^b44, depth-1)
		m11 =mat444mod2( a41^a43,b11^b31^b41^b12^b22^b42^b23^b33^b24^b34, depth-1)
		m12 =mat444mod2( a34,b11^b21^b12^b32^b43^b44, depth-1)
		m13 =mat444mod2( a31^a12^a32^a33^a14,b21^b32, depth-1)
		m14 =mat444mod2( a11^a21^a31^a22^a32^a33^a14,b11^b32^b14, depth-1)
		m15 =mat444mod2( a11^a23^a14,b31^b32^b14, depth-1)
		m16 =mat444mod2( a41^a12^a42^a13^a23^a43^a14,b31^b32^b34, depth-1)
		m17 =mat444mod2( a41^a12^a32^a43^a14,b22^b32, depth-1)
		m18 =mat444mod2( a21^a23^a34,b11^b21^b41^b12^b32, depth-1)
		m19 =mat444mod2( a11^a21^a31^a12^a32^a13^a23^a33^a14,b32, depth-1)
		m20 =mat444mod2( a31^a33^a34,b11^b21^b12^b32, depth-1)
		m21 =mat444mod2( a41^a22^a42^a43^a24^a34^a44,b11^b21^b41^b22^b32^b14^b24^b44, depth-1)
		m22 =mat444mod2( a41^a12^a42^a33^a14,b21^b31^b22^b32^b24^b34, depth-1)
		m23 =mat444mod2( a11^a13^a14,b31^b32, depth-1)
		m24 =mat444mod2( a41^a44,b11^b21^b12^b22^b42^b43^b24^b34, depth-1)
		m25 =mat444mod2( a41^a43^a14,b11^b21^b41^b12^b22^b42, depth-1)
		m26 =mat444mod2( a31^a22^a32^a33^a24,b11^b21^b32^b14, depth-1)
		m27 =mat444mod2( a31^a32^a33,b11^b21^b12^b32^b13^b14, depth-1)
		m28 =mat444mod2( a21^a23,b21^b41^b12^b32^b13^b14, depth-1)
		m29 =mat444mod2( a11^a14,b31^b12^b32^b13^b14, depth-1)
		m30 =mat444mod2( a12^a13,b31^b33^b34, depth-1)
		m31 =mat444mod2( a41^a33^a44,b11^b21^b12^b22^b24^b34, depth-1)
		m32 =mat444mod2( a22^a23,b11^b22^b32^b42^b23^b43^b14, depth-1)
		m33 =mat444mod2( a41^a22^a42^a43^a24,b11^b21^b41^b32^b14^b44, depth-1)
		m34 =mat444mod2( a41^a43^a34,b11^b21^b41^b12^b32^b42, depth-1)
		m35 =mat444mod2( a12^a14,b31^b22^b23^b33^b24^b34, depth-1)
		m36 =mat444mod2( a41^a22^a42^a43^a14,b11^b21^b41^b32^b14^b24^b44, depth-1)
		m37 =mat444mod2( a41^a22^a32^a33^a24^a34^a44,b11^b21^b22^b32^b14^b24, depth-1)
		m38 =mat444mod2( a22^a24,b11^b21^b32^b42^b43^b14, depth-1)
		m39 =mat444mod2( a41^a23^a44,b11^b21^b41^b12^b22^b42^b24^b34^b44, depth-1)
		m40 =mat444mod2( a41^a23^a14,b11^b21^b41^b12^b22^b42^b14^b24^b44, depth-1)
		m41 =mat444mod2( a11^a21^a31^a32^a23^a33^a14,b11^b12^b32^b13^b14, depth-1)
		m42 =mat444mod2( a21^a23^a24,b11^b21^b41^b32^b14, depth-1)
		m43 =mat444mod2( a21^a23^a14,b11^b21^b41^b32, depth-1)
		m44 =mat444mod2( a41^a12^a42^a43^a14,b31^b32^b24^b34, depth-1)
		m45 =mat444mod2( a32^a33,b11^b21^b12^b32^b13^b23^b14^b24, depth-1)
		m46 =mat444mod2( a41^a42^a43,b31^b12^b22^b42^b13^b23^b33^b43^b24^b34, depth-1)
		m47 =mat444mod2( a23,b31^b12^b22^b42^b13^b23^b33^b43^b14, depth-1)
		
		c11 = m13^m19^m23^m27^m28^m29^m41^m43
		c12 = m4^m7^m9^m11^m13^m19^m25^m27^m28^m29^m35^m41^m43
		c13 = m2^m4^m7^m9^m11^m13^m15^m16^m19^m25^m27^m28^m30^m41^m43^m44^m46^m47
		c14 = m1^m2^m15^m16^m23^m44^m46^m47
		c21 = m14^m15^m26^m27^m28^m29^m41^m42
		c22 = m1^m2^m5^m10^m12^m18^m24^m33^m36^m38^m39^m43^m46^m47
		c23 = m1^m2^m5^m10^m12^m14^m15^m18^m24^m26^m27^m29^m32^m33^m36^m39^m41^m43^m46
		c24 = m1^m2^m33^m36^m42^m43^m46^m47
		c31 = m4^m8^m18^m20^m27^m28^m29^m41
		c32 = m4^m7^m8^m9^m11^m13^m17^m18^m27^m28^m29^m34^m35^m41
		c33 = m4^m5^m8^m9^m11^m13^m17^m18^m24^m26^m28^m29^m31^m34^m35^m37^m38^m41^m45
		c34 = m4^m5^m7^m8^m9^m11^m12^m13^m17^m18^m20^m24^m26^m27^m28^m29^m31^m34^m35^m37^m38^m41
		c41 = m1^m2^m3^m5^m7^m9^m11^m12^m21^m22^m24^m25^m31^m33^m34^m35^m38^m39^m40^m44^m46^m47
		c42 = m1^m2^m5^m12^m21^m24^m25^m33^m34^m38^m39^m40^m46^m47
		c43 = m1^m2^m5^m6^m7^m9^m12^m21^m22^m25^m31^m33^m34^m35^m38^m39^m40^m44^m47
		c44 = m1^m2^m3^m25^m39^m40^m46^m47

	result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0), np.concatenate((c14, c24, c34, c44), axis=0)), axis=1)

	return result


def mat445mod2(a,b,depth):

	a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44 = div4x4(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45 = div4x5(b)


	if depth == 0:
		return strassenInit(a,b,False)
	else:
		m1 =mat445mod2( a12^a42^a13^a23^a43^a14^a24,b32^b35, depth-1)
		m2 =mat445mod2( a12,b11^b13^b43^b24^b15^b25^b45, depth-1)
		m3 =mat445mod2( a21^a41^a43,b11^b15^b35, depth-1)
		m4 =mat445mod2( a42^a44,b11^b41^b12^b42^b13^b43, depth-1)
		m5 =mat445mod2( a11^a21^a13^a23^a14^a24,b31^b32^b33, depth-1)
		m6 =mat445mod2( a12^a22^a14^a24,b21^b41^b32^b42^b23^b24^b35^b45, depth-1)
		m7 =mat445mod2( a22^a32^a42,b24^b44, depth-1)
		m8 =mat445mod2( a11^a21^a41^a12^a42^a44,b11^b21^b41^b22^b42^b13^b23^b43^b15, depth-1)
		m9 =mat445mod2( a11^a21^a12^a42^a43,b21^b41^b22^b42^b25^b45, depth-1)
		m10 =mat445mod2( a22^a44,b41^b25, depth-1)
		m11 =mat445mod2( a12^a22^a32^a13^a33^a14^a24^a34,b41^b35^b45, depth-1)
		m12 =mat445mod2( a11^a21^a41^a12^a22^a32^a44,b21^b31^b41^b22^b32^b42^b23^b33^b43, depth-1)
		m13 =mat445mod2( a13,b41^b12^b42^b14^b34^b35^b45, depth-1)
		m14 =mat445mod2( a21^a41^a12^a22^a32^a13^a23^a33^a43^a14^a24^a34,b35, depth-1)
		m15 =mat445mod2( a31^a12^a22^a32^a14^a24^a34,b11^b31^b12^b32^b13^b33, depth-1)
		m16 =mat445mod2( a12^a22^a32^a42^a14^a24^a34^a44,b11^b41^b12^b42^b13^b43, depth-1)
		m17 =mat445mod2( a41^a12^a22^a32^a14^a24^a44,b21^b31^b41^b22^b32^b42^b23^b33^b43, depth-1)
		m18 =mat445mod2( a11^a21^a12^a22^a32^a23^a33,b33^b34, depth-1)
		m19 =mat445mod2( a12^a22^a32^a14^a24^a34,b11^b13^b43^b14^b44^b35^b45, depth-1)
		m20 =mat445mod2( a11^a31^a12^a42^a44,b11^b13^b43^b44^b15^b25^b45, depth-1)
		m21 =mat445mod2( a12^a22^a32^a13^a33^a14^a24,b31^b22^b32^b42^b33^b24^b44, depth-1)
		m22 =mat445mod2( a12^a22^a14^a24,b21^b22^b23, depth-1)
		m23 =mat445mod2( a12^a42^a13^a33^a14^a24,b41^b22^b32^b42^b24^b44^b35^b45, depth-1)
		m24 =mat445mod2( a11^a21^a13,b31^b12^b32^b14^b34, depth-1)
		m25 =mat445mod2( a12^a22^a13^a14^a24,b41^b32^b42^b35^b45, depth-1)
		m26 =mat445mod2( a11^a21,b11^b21^b31^b41^b22^b32^b42^b14^b34^b15^b25^b45, depth-1)
		m27 =mat445mod2( a22^a42,b41^b22^b32^b42^b35^b45, depth-1)
		m28 =mat445mod2( a22^a24,b41, depth-1)
		m29 =mat445mod2( a11^a31^a12^a22^a32^a14^a24^a34,b11^b13^b43^b14^b44, depth-1)
		m30 =mat445mod2( a13^a33,b41^b22^b32^b42^b24^b34^b44^b35^b45, depth-1)
		m31 =mat445mod2( a11^a31^a41^a12^a22^a32^a43,b11^b15, depth-1)
		m32 =mat445mod2( a23^a33^a43,b34, depth-1)
		m33 =mat445mod2( a22,b21^b41, depth-1)
		m34 =mat445mod2( a31^a12^a22^a32^a13^a14^a24^a34,b31^b12^b32^b33^b14, depth-1)
		m35 =mat445mod2( a11^a31^a12^a22^a32,b11^b15^b25^b45, depth-1)
		m36 =mat445mod2( a12^a22^a32^a13^a33^a14^a34^a44,b41^b45, depth-1)
		m37 =mat445mod2( a21,b11, depth-1)
		m38 =mat445mod2( a12^a22^a32^a13^a33,b31^b22^b32^b42^b24^b34^b44, depth-1)
		m39 =mat445mod2( a21^a31^a41,b14, depth-1)
		m40 =mat445mod2( a21^a41,b41^b12^b42^b35^b45, depth-1)
		m41 =mat445mod2( a11^a21^a41^a42^a44,b11^b21^b41^b12^b22^b42^b13^b23^b43, depth-1)
		m42 =mat445mod2( a11^a21,b31^b12^b32^b13^b23^b43^b14^b34^b15^b25^b45, depth-1)
		m43 =mat445mod2( a22^a32^a42^a24^a34^a44,b44, depth-1)
		m44 =mat445mod2( a11^a21^a12^a22^a32^a43,b11^b21^b31^b41^b22^b32^b42^b34^b15^b25^b45, depth-1)
		m45 =mat445mod2( a11^a31^a12^a22^a32^a44,b25^b45, depth-1)
		m46 =mat445mod2( a21^a41^a12^a42^a13^a14^a44,b41^b42^b45, depth-1)
		m47 =mat445mod2( a41^a44,b21^b31^b41^b22^b32^b42^b23^b33^b43, depth-1)
		m48 =mat445mod2( a43,b11^b21^b31^b41^b22^b32^b42^b15^b25^b45, depth-1)
		m49 =mat445mod2( a12^a22^a32,b11^b21^b31^b41^b22^b32^b42^b24^b34^b44^b15^b25^b45, depth-1)
		m50 =mat445mod2( a22^a14^a24,b21^b41^b23^b24, depth-1)
		m51 =mat445mod2( a31^a41^a33^a43^a34^a44,b31^b32^b33, depth-1)
		m52 =mat445mod2( a11^a21^a12,b11^b13^b23^b43^b15^b25^b45, depth-1)
		m53 =mat445mod2( a42^a44,b11^b13^b43^b15^b25^b45, depth-1)
		m54 =mat445mod2( a31^a33^a34,b31^b32^b33, depth-1)
		m55 =mat445mod2( a11^a31^a12^a22^a32^a24^a34,b43^b44, depth-1)
		m56 =mat445mod2( a23,b31, depth-1)
		m57 =mat445mod2( a11^a31,b11^b13^b43^b14^b44^b15^b25^b45, depth-1)
		m58 =mat445mod2( a22^a42^a43,b21^b41^b22^b32^b42^b25^b35^b45, depth-1)
		m59 =mat445mod2( a21^a41^a12^a22^a32^a13^a14^a24^a34,b41^b12^b42^b14^b35^b45, depth-1)
		m60 =mat445mod2( a21^a41^a42^a44,b41^b12^b42^b15^b45, depth-1)
		
		c11 = m2^m6^m13^m24^m25^m28^m37^m42^m50^m52
		c12 = m49^m52^m56^m58^m60^m21^m18^m13^m14^m1^m3^m5^m7^m8^m9^m10^m11^m41^m42^m44^m45^m46^m48^m35^m36^m37^m38^m31^m32^m33^m27^m30^m23^m24
		c13 = m4^m13^m15^m16^m19^m20^m24^m29^m34^m37^m39^m40^m42^m43^m52^m53^m55^m57^m59
		c14 = m2^m4^m13^m16^m19^m20^m39^m40^m43^m53^m57^m59
		c15 = m49^m50^m52^m56^m58^m21^m18^m13^m14^m1^m2^m3^m5^m6^m7^m9^m10^m11^m42^m44^m45^m48^m35^m36^m37^m38^m31^m32^m33^m27^m28^m30^m23^m24^m25
		c21 = m28^m33^m37^m56
		c22 = m1^m3^m8^m9^m10^m11^m14^m25^m26^m31^m33^m35^m36^m37^m41^m42^m45^m46^m52^m58^m60
		c23 = m49^m50^m53^m55^m57^m59^m19^m20^m21^m15^m16^m17^m18^m12^m13^m2^m4^m6^m7^m42^m43^m44^m48^m40^m34^m37^m38^m39^m32^m33^m27^m29^m30^m22^m23^m24
		c24 = m2^m4^m6^m7^m13^m16^m19^m20^m22^m23^m26^m27^m30^m32^m39^m40^m43^m44^m48^m49^m53^m57^m59
		c25 = m3^m10^m11^m14^m28^m31^m35^m36^m37^m45
		c31 = m2^m6^m11^m13^m19^m24^m25^m29^m30^m33^m35^m37^m38^m42^m49^m50^m52^m57
		c32 = m7^m11^m21^m23^m25^m27^m34^m39^m40^m54^m59
		c33 = m49^m50^m52^m57^m59^m19^m21^m15^m16^m17^m13^m2^m4^m6^m7^m42^m47^m40^m34^m35^m37^m38^m39^m33^m27^m29^m30^m22^m23^m24
		c34 = m4^m6^m7^m13^m16^m19^m22^m23^m27^m30^m39^m40^m59
		c35 = m49^m50^m52^m56^m57^m58^m19^m21^m18^m13^m14^m1^m2^m3^m5^m6^m7^m9^m42^m44^m48^m35^m37^m38^m31^m32^m33^m27^m29^m30^m23^m24^m25
		c41 = m3^m4^m10^m27^m33^m37^m40^m48^m53^m58^m60
		c42 = m3^m8^m9^m10^m26^m27^m31^m33^m35^m37^m40^m41^m42^m45^m52^m58^m60
		c43 = m8^m9^m31^m35^m45^m47^m48^m51^m52^m53^m54
		c44 = m2^m7^m20^m26^m39^m44^m48^m49^m53^m57
		c45 = m3^m4^m31^m35^m37^m40^m45^m53^m60

	result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0), np.concatenate((c14, c24, c34, c44), axis=0), np.concatenate((c15, c25, c35, c45), axis=0)), axis=1)

	return result



def mat445(a,b,depth):

	a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44 = div4x4(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45 = div4x5(b)


	if depth == 0:
		return strassenInit(a,b,True)
	else:
		m1 =mat445( a41-a42,b14+b15, depth-1)
		m2 =mat445( 2*a14-a34-a44,-b42-b43+b44, depth-1)
		m3 =mat445( a11-a41+a42+a23+a43+a14+a24-a34,b11+b41-b22+b13-b33+b43+2*b14+b24-b34+3*b44-b35+b45, depth-1)
		m4 =mat445( -2*a11-a21+a31+a41+2*a12+a22-a32-a42+a13+a23-a33+a14+a24-a34,-b32-b23-b24+b34-b25, depth-1)
		m5 =mat445( a23,b11+b21-b31+b41+b13+b23-b33+b43+2*b14+2*b24-2*b34+2*b44, depth-1)
		m6 =mat445( -2*a14-a24+a34+a44,-b32+b42-b33+b43-b35+b45, depth-1)
		m7 =mat445( a11+a21-a31-a42-a43-a14-a24+a34,b11+b21+b13+b23+2*b14+2*b24, depth-1)
		m8 =mat445( 2*a11+a21-a31-a41-2*a12-a22+a32+a42,b22-b32-b24+b34, depth-1)
		m9 =mat445( -2*a11+a31+a41,-b12-b13+b14, depth-1)
		m10 =mat445( a13-a33-a43,b11+b41+b12-b32+b42+b13-b33+b43+b14+b34+b44, depth-1)
		m11 =mat445( 2*a13-a33-a43,-b21+b31-b22+b32-b23+b33-b24+b34, depth-1)
		m12 =mat445( -a23+a44,b11+b21-b31+b41+b13+b23-b33+b43+2*b14+2*b24-2*b34+2*b44-b25+b35, depth-1)
		m13 =mat445( -a11+a41+a12-a42+a14-2*a44,-b11-b21+b31-b41-b13-b23+b33-b43-2*b14-2*b24+2*b34-2*b44+b15+b25-b35+b45, depth-1)
		m14 =mat445( -a12+a32+a42-a13+a33+a43-a14-a24+a34,-b21-b22-b23-b24+b25, depth-1)
		m15 =mat445( a12+a13,b31+2*b34, depth-1)
		m16 =mat445( -a21-a41+a22+a42+a23+a24,b11+b41+b13+b43+2*b14+3*b44+b45, depth-1)
		m17 =mat445( a42+a43,b11+b21-b31+b41+b13+b23-b33+b43+4*b14+4*b24-3*b34+3*b44+3*b15+3*b25-b35+b45, depth-1)
		m18 =mat445( a41-a42-a43-a44,b15, depth-1)
		m19 =mat445( a13-a43+a14-a44,-b31-b32-b33-b34+b35, depth-1)
		m20 =mat445( -a23-2*a14-a24+a34+a44,-b32-b33+b44-b35+b45, depth-1)
		m21 =mat445( 2*a11+a21-a31-a41,b12+b22+b13+b23+b15+b25, depth-1)
		m22 =mat445( a21+a41-a22-a42,b11+b41+b13+b43+3*b14+3*b44+b15+b45, depth-1)
		m23 =mat445( a11-a41-a14+a44,b11+b21+b13+b23-b33+b43+2*b14+2*b24-b34+b44-b15-b25-b35+b45, depth-1)
		m24 =mat445( -a12-2*a13+a33+a43,-b21+b31-b22-b23-b24+2*b34, depth-1)
		m25 =mat445( -a21-a41+a22+a42+a23+a43+a24+a44,b41+b43+3*b44+b15+b45, depth-1)
		m26 =mat445( -a23-a24,b11+b41+b13+b43+2*b14+2*b44, depth-1)
		m27 =mat445( -a11+a31+a42+a43+a14-a34,b21+b22+b23+b24+b15, depth-1)
		m28 =mat445( a11-a41-a12+a42,-b11+b31-b41-b13-b23+b33-b43-2*b14-b24+2*b34-2*b44+b15-b25-b35+b45, depth-1)
		m29 =mat445( a14,b11+b41+2*b14+2*b44, depth-1)
		m30 =mat445( a13+a23-a33+a14+a24-a34,b21-b31+b22-b32+b23-b33+b24-b34-b25+b35, depth-1)
		m31 =mat445( -a42-a23-2*a43,b11+b21-b31+b41+b13+b23-b33+b43+4*b14+4*b24-3*b34+3*b44+2*b15+2*b25-b35+b45, depth-1)
		m32 =mat445( a22+a42+2*a23+2*a43,b14+b24+b15+b25, depth-1)
		m33 =mat445( a11+a21-a31-a12-a22+a32-a13-a23+a33-a14-a24+a34,b23+b24+b25, depth-1)
		m34 =mat445( a11-a41+a42,b11+b41+b13+b23-b33+b43+3*b14+b24-b34+3*b44+b15+b25-b35+b45, depth-1)
		m35 =mat445( -a22-a42-a23-a43,-b11-b21-b13-b23-2*b14-2*b24+b15+b25, depth-1)
		m36 =mat445( -a11+a31+a41+a14-a34-a44,b41+b42+b43+b44+b15, depth-1)
		m37 =mat445( a11-a31-2*a12+a32-2*a13+a33-a14+a34,b21+b22+b23+b24, depth-1)
		m38 =mat445( a11-a41+a14+a24-a34,-b12-b22-b33+b43+b14+b24-b34+b44-b35+b45, depth-1)
		m39 =mat445( -a11+a41,b13+b23-b33+b43+b14+b24-b34+b44+b15+b25-b35+b45, depth-1)
		m40 =mat445( a44,-b11-b21+b31-b41-b13-b23+b33-b43-2*b14-2*b24+2*b34-2*b44+b15+b25-b35+b45, depth-1)
		m41 =mat445( a12,-b21+b31-2*b24+2*b34, depth-1)
		m42 =mat445( -a42-2*a43,b11+b21-b31+b41+b13+b23-b33+b43+3*b14+3*b24-3*b34+3*b44+b15+b25-b35+b45, depth-1)
		m43 =mat445( a11+a21-a31-a14-a24+a34,-b12-b22+b14+b24, depth-1)
		m44 =mat445( a11-a41-a12+a42+a14+a24-a34,-b11+b31-b41+b22-b13+b33-b43-2*b14-b24+2*b34-2*b44+b15-b35+b45, depth-1)
		m45 =mat445( -a11+a41-a42-a43+a14-a44,b11+b21+b41+b13+b23-b33+b43+2*b14+2*b24-b34+3*b44-b15-b25-b35+b45, depth-1)
		m46 =mat445( a11+a21-a31-2*a12-a22+a32-2*a13-a23+a33-a14-a24+a34,-b11-2*b21-b22-b13-2*b23-2*b14-3*b24+b15+b25, depth-1)
		m47 =mat445( a11-a31-a41+a14,b11+b41+b42+b43+2*b14+b44, depth-1)
		m48 =mat445( a23+a43,b11+b21-b31+b41+b13+b23-b33+b43+4*b14+4*b24-3*b34+3*b44+2*b15+b25+b45, depth-1)
		m49 =mat445( -a13+a33+a43-a14-a24+a34,b11+b21-b31+b41+b12+b22-b32+b42+b13+b23-b33+b43+b14+b24-b34+b44-b25+b35, depth-1)
		m50 =mat445( -a12+a32+a42,-b22-b23+b24, depth-1)
		m51 =mat445( a13-a43+a14-a44,b32+b33+b35, depth-1)
		m52 =mat445( -2*a11-a21+a31+a41+2*a12+a22-a32-a42+2*a13+a23-a33-a43+2*a14+a24-a34-a44,-b11-b21-b32-b13-b23-2*b14-2*b24+b34+b15+b25, depth-1)
		m53 =mat445( -a14-a24+a34,-b11+b31-b41-b12+b32-b42-b13+b33-b43-b14+b34-b44+b15-b35+b45, depth-1)
		m54 =mat445( -a11+a14,b11+2*b14, depth-1)
		m55 =mat445( -a11-a21+a31+2*a12+3*a22-a32+a42+2*a13+3*a23-a33+a43+a14+a24-a34,-b11-b21-b13-b23-2*b14-2*b24+b15+b25, depth-1)
		m56 =mat445( a24+a44,b15+b45, depth-1)
		m57 =mat445( a43+a44,b11+b21-b31+b41+b13+b23-b33+b43+2*b14+2*b24-2*b34+3*b44-b25+b35+b45, depth-1)
		m58 =mat445( -a13-a23+a33-a14-a24+a34,-b23+b33-b24+b34-b25+b35, depth-1)
		m59 =mat445( a21-a22-a23-a24,-b11+b21+b22-b13+b23-2*b14+b24+b15, depth-1)
		m60 =mat445( -a11-a21+a31+a22+a42+a23+a43+a14+a24-a34,b11-b22+b13+2*b14+b24-b15, depth-1)
		m61 =mat445( -2*a11-a21+a31+a41+a22,b22+b23+b14+b15+b25, depth-1)
		m62 =mat445( -a11+a31+a41-a13+a33+a43,b11+b41+b12+b42+b13+b43+b14+b44, depth-1)
		
		c11 = -2*m1+4*m3+4*m10+4*m11+4*m12+2*m13+3*m15+2*m18+2*m19+4*m20+4*m24-2*m28+m29+4*m30-2*m34+4*m40+m41+4*m44+2*m45+4*m49-2*m51+4*m53-m54-2*m57
		c12 = -3*m49+m51-m52-3*m53-m54+2*m57-m59-m19-3*m20-m15+m16-2*m18-3*m12-m13+m1-3*m3+m4+m9-2*m10-2*m11-m41-3*m44-2*m45-m46+m47-2*m40+m34-m37-m33+m62+2*m28-3*m30-2*m24-m25
		c13 = m49+m52+m53+m54-m57+m59+m20-m16+m18+m12+m3-m4+m10+m11+m41+m44+m45+m46+m37+m33-m28-m29+m30+m24+m25
		c14 = m1-2*m3-2*m10-2*m11-2*m12-m13-m15-m18-m19-2*m20-2*m24+m28-2*m30+m34-2*m40-m41-2*m44-m45-2*m49+m51-2*m53+m57
		c15 = m3+m10+m11+m12+m13+m15+m18+m19+m20+m24+m30+2*m40+m44+m45+m49+m53
		c21 = m54+3*m55+2*m56+2*m60-m21-2*m16+m18-2*m12+2*m1-m2+m3-4*m5+3*m7+m42-m43+m45+3*m46-m47-2*m40+4*m35-m36+3*m37-m38-m31-m32-m61-2*m26+3*m27-2*m22+m23
		c22 = m54-m56+m59-2*m60+m20+m16+m18+m12-m1+m3+2*m5-m6-m7-m9-m42-m43+m45-m47+m40+m35-m36-m38+m31+m32+2*m26-m27+m22+m23
		c23 = m2-m3-m5-m18+m21-m23-m26-m31-m32-2*m35+m36-m37+m38+m42+m43-m45-m46+m47-m54-m55-m59+m60+m61
		c24 = -m1+2*m5-m7+m12+m16+m22+m26-m27+m31+m32-m35-m37+m40-m42-m46-m55-m56-m60
		c25 = -m5+m7-m12+m27+m35+m37-m40+m46+m55+m56+m60
		c31 = 8*m49-m50-2*m51+8*m53+2*m56-2*m57-2*m58+2*m19+4*m20+6*m15-2*m16-3*m17+3*m18+2*m12+2*m13+2*m14-m2+6*m3-2*m4-4*m5-2*m8+8*m10+4*m11+m41+m42+6*m44+3*m45-m47-4*m48+2*m40-3*m34-m36+3*m37+m39-4*m31-2*m61-2*m26+3*m27-4*m28+m29+6*m30-2*m22+m23+7*m24
		c32 = -5*m49+m50+m51-m52-6*m53+m55-m56+2*m57+m58-m60-m19-2*m20-2*m15+2*m16+m17-m18-2*m12-m13-m14-3*m3+3*m4+2*m5-m6+2*m8-4*m10-2*m11-m41-m42-5*m44-m45+2*m48-m40+2*m34+2*m35-m36-m37-m38+2*m31-2*m33+m61+m62+2*m26-m27+4*m28-4*m30+m22+m23-3*m24-m25
		c33 = 2*m49-m50+m52+2*m53-m55-m57+m60+m20-m16+m12+m2+m3-2*m4-m5-m8+2*m10+m11+m41+m42+2*m44+m47-m48-m34-2*m35+m36-m39-m31+2*m33-m26-2*m28-m29+2*m30-m23+m24+m25
		c34 = -4*m49+m50+m51-4*m53-m56+m57+m58-m19-2*m20-2*m15+m16+m17-m18-m12-m13-m14-3*m3+m4+2*m5+m8-4*m10-2*m11-m41-m42-3*m44-m45+2*m48-m40+2*m34-m37+2*m31+m61+m26-m27+2*m28-3*m30+m22-3*m24
		c35 = m3-m5+2*m10+m11+m13+m14+2*m15-m17+m18+m19+m20+2*m24+m27+m30-m31+m37+m40+m44+m45-m48+2*m49+2*m53+m56
		c41 = -2*m1+4*m5+4*m12+3*m17+2*m18-m23+m29+4*m31-m34-m39+2*m40-m42-m45+4*m48-m54-2*m57
		c42 = -m49-m54-m55+2*m57-m59-m20+m16-m17-2*m18-3*m12+m1-m3-2*m5+m6+m9+m42-m45-m46+m47-2*m48-m40-2*m35-m37+m38-2*m31+m62-m30-m23-m25
		c43 = m5+m12-m16+m18+m23+m25-m29+m31+m34+2*m35+m37+m39-m42+m45+m46+m48+m54+m55-m57+m59
		c44 = m1-2*m5-2*m12-m17-m18-2*m31-m40+m42-2*m48+m57
		c45 = m5+m12+m17+m18+m31+m40+m48

	result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0), np.concatenate((c14, c24, c34, c44), axis=0), np.concatenate((c15, c25, c35, c45), axis=0)), axis=1)

	return result



def div5x5(a):

	col = len(a)//5
	row = len(a[1])//5

	#row 1

	a11 = a[0:row,0:col]
	a12 = a[row:1*row,0:col]
	a13 = a[2*row:3*row,0:col]
	a14 = a[3*row:4*row,0:col]
	a15 = a[4*row:5*row,0:col]
	#row 2

	a21 = a[0:row,col:1*col]
	a22 = a[row:1*row,col:1*col]
	a23 = a[2*row:3*row,col:1*col]
	a24 = a[3*row:4*row,col:1*col]
	a25 = a[4*row:5*row,col:1*col]
	#row 3

	a31 = a[0:row,2*col:3*col]
	a32 = a[row:1*row,2*col:3*col]
	a33 = a[2*row:3*row,2*col:3*col]
	a34 = a[3*row:4*row,2*col:3*col]
	a35 = a[4*row:5*row,2*col:3*col]
	#row 4

	a41 = a[0:row,3*col:4*col]
	a42 = a[row:1*row,3*col:4*col]
	a43 = a[2*row:3*row,3*col:4*col]
	a44 = a[3*row:4*row,3*col:4*col]
	a45 = a[4*row:5*row,3*col:4*col]
	#row 5

	a51 = a[0:row,4*col:5*col]
	a52 = a[row:1*row,4*col:5*col]
	a53 = a[2*row:3*row,4*col:5*col]
	a54 = a[3*row:4*row,4*col:5*col]
	a55 = a[4*row:5*row,4*col:5*col]

	return (a11, a12, a13, a14, a15, 
	  a21, a22, a23, a24, a25, 
	  a31, a32, a33, a34, a35, 
	  a41, a42, a43, a44, a45, 
	  a51, a52, a53, a54, a55)

def mat455(a,b,depth):

	a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45 = div4x5(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45, b51, b52, b53, b54, b55 = div5x5(b)


	if depth == 0:
		return strassenInit(a,b,True)
	else:
		m1 =mat455( a21+a31+2*a23+2*a33+a24+a34,-b11+b21+b31+b12-b22-b32-b13+b23+b33, depth-1)
		m2 =mat455( -a11+a41-a12+a42-a13+a43-a14+a44,-2*b13+b33-b53+2*b15-b35+b55, depth-1)
		m3 =mat455( -a31-a32-a34+a35,-b23+b14-b44+b54, depth-1)
		m4 =mat455( a11+a12+a13+a14,b21-b23+b25, depth-1)
		m5 =mat455( a21+a22+a24-a25,b22+b52+2*b13-b33+b53+2*b14-b24-b34, depth-1)
		m6 =mat455( a13+a15-a35,b11-b31+b51+b23+b33-b43+b15-b35+b55, depth-1)
		m7 =mat455( a23+a33-a43+a24+a34-a44+a25+a35-a45,-b12+b22+b32, depth-1)
		m8 =mat455( -a22-a32+a42+a23+a33-a43-a24-a34+a44+a25+a35-a45,b22, depth-1)
		m9 =mat455( a31+3*a33+2*a34+a35,b13-b43-b14+b44, depth-1)
		m10 =mat455( -a13-a23+a43-a15-a25+a45,-b22-b52+b13+b23-b33+2*b53+b24+b54-b15-b25+b35-2*b55, depth-1)
		m11 =mat455( a22+a32-a23-a33+a24+a34-a44-a25-a35,b11+b21-b41+b51+b12+2*b22-b42+b52+b13+b23-b43+b53, depth-1)
		m12 =mat455( a21+a22-a13+a43+a24-a25,-b12+b32-b52+2*b13-b33+b53+b14-b34+b54, depth-1)
		m13 =mat455( -a21-a23-2*a24,2*b12-b32+b52, depth-1)
		m14 =mat455( a11-a31+a12-a32+a13-a33+a14-a34-a15+a35,2*b14-b24-b34+b54, depth-1)
		m15 =mat455( a11+a21-a41+a12+a22-a42+a14+a24-a44-a15-a25+a45,-b12+b32-b52-2*b13+b33-b53-b14+2*b15-b35+b55, depth-1)
		m16 =mat455( -a22+a23+a25,2*b12-b22-b42+2*b13-b23-b43-2*b14+b24+b44-2*b15+b25+b45, depth-1)
		m17 =mat455( -a31+a22-a23-a33-a34-a25,b11+b21-b31+b51+3*b13-b23-b33+b53-b15+b25, depth-1)
		m18 =mat455( -a13+a43-a15+a35,b11-b31+b51-b13+b33-b53+b15-b35+b55, depth-1)
		m19 =mat455( -a11-a31-3*a13-3*a33-2*a14-2*a34-a15-a35,-b14+b24, depth-1)
		m20 =mat455( -a31-a32-a33-a34,b14+b24-b44+b54, depth-1)
		m21 =mat455( -a31+a22-a23-2*a33-a34-a25,-b11+b21+b31+b12-b22-b32-b13+2*b23+b33-b43-b24+b44, depth-1)
		m22 =mat455( -a31-a33-a34,-2*b11+b21+b41+2*b13-b23-b43-2*b15+b25+b45, depth-1)
		m23 =mat455( a21+a22-a13+a43+a24-a15-a25+a45,b22+b52-2*b13+b33-b53-b24-b54+2*b15-b35+b55, depth-1)
		m24 =mat455( -a11+a31-a12+a32-a13-a14+a34+a15-a35,-b23+2*b14-b24-b34+b54, depth-1)
		m25 =mat455( a11-a31+a13-a33+2*a14+a24-a34-a44,-b11+b41+2*b12-b32+b52+b13-b43-b15+b45, depth-1)
		m26 =mat455( -a24-a34+a44,b11-b41+b12+2*b22-b42+b52-b13+b43+b15-b45, depth-1)
		m27 =mat455( -a11-a12-a13-a14+a15,b23, depth-1)
		m28 =mat455( a35,b13+b23-b43+b53, depth-1)
		m29 =mat455( a14-a44,b13-b43-b15+b45, depth-1)
		m30 =mat455( -a41-a43-a44,-b11-2*b12+b32-b52-b13+b33-b53+b15-b35+b55, depth-1)
		m31 =mat455( -a12+a42+a13-a43+a15-a45,-2*b13+2*b23+b33-b53+2*b15-b25-b35+b55, depth-1)
		m32 =mat455( a31-a22-a13+a23+a33-a24-a44-a15+a25-a35,b21+b51+b12-b22-b32+b13+b23-b43+b53-b24+b44, depth-1)
		m33 =mat455( a11+a13+a14,3*b11-b21-b31-b41+b51-b13+b23+b43+3*b15-b25-b35-b45+b55, depth-1)
		m34 =mat455( a13+a23-a43,-b12+b32-b52+b14-b34+b54, depth-1)
		m35 =mat455( -a11+a41-2*a13+2*a43-a14+a44,b33-b53+b15-b35+b55, depth-1)
		m36 =mat455( -a21-a31-a23-a33-a43-a44+a25+a35-a45,b21+b51+b12-b22-b32+b23+b53, depth-1)
		m37 =mat455( a31+2*a33+a34,2*b13-b23-b43-2*b14+b24+b44, depth-1)
		m38 =mat455( -a11+a21+a41-a13+a23+a43-2*a14+2*a24+2*a44,2*b12-b32+b52, depth-1)
		m39 =mat455( a11+a42+2*a13-a43+a14-a45,-b13+b23+b33-b53+b15-b35+b55, depth-1)
		m40 =mat455( a33,b13-2*b23-b33+b43+2*b14-b24-b34+b54, depth-1)
		m41 =mat455( a31-a22+a23+a33-a24+a25-a35,b21+b51-b22-b52+b13+b23-b43+b53-b14+b44, depth-1)
		m42 =mat455( -a13-a14-a15,-b13+b43, depth-1)
		m43 =mat455( a13-a43,2*b13-b33+b53, depth-1)
		m44 =mat455( a42-a43-a45,-b21-b13+b33-b53+b15-b35+b55, depth-1)
		m45 =mat455( -a22-a32+a23+a33+a25+a35,b11+2*b21-b41+b51+b12+2*b22-b42+b52+b13+2*b23-b43+b53, depth-1)
		m46 =mat455( a21+a31-a41+a23+a33-a43-a25-a35+a45,b12-b32+b52, depth-1)
		m47 =mat455( a11+a12-a42+a43+a14-a15+a45,-b21-2*b13+b23+b33-b53+2*b15-b25-b35+b55, depth-1)
		m48 =mat455( -a13+a33-a15+a35,-b11+b21+b31+b13-b23-b33+b14+b24-b44+b54-b15+b25+b35, depth-1)
		m49 =mat455( -a11-a13-2*a14,-b11+b41+b13-b43-b15+b45, depth-1)
		m50 =mat455( -a31-a13-3*a33-a14-2*a34-a15-a35,b13-b43-2*b14+b24+b44, depth-1)
		m51 =mat455( a11-a31+a13-a33+2*a14-2*a34,-b11+b41+b13-b43-b15+b45, depth-1)
		m52 =mat455( a12+a22-a42-a13-a23+a43-a14-a24+a44-a15-a25+a45,b12+b22-b32+b52+b14-b24, depth-1)
		m53 =mat455( -a21-a22-2*a23-a24,b21+b51, depth-1)
		m54 =mat455( -a21-a22-a23-a24+a25,-b11-b21+b31-2*b51-b12+b32-b52+b14-b34+b54, depth-1)
		m55 =mat455( -a11-2*a13-a14,b11-b31+b51+b23+b15-b35+b55, depth-1)
		m56 =mat455( a13+a44+a15,b21+b51+b13+b23-b43+b53, depth-1)
		m57 =mat455( a44,b21+b51+2*b13+b23-2*b43+b53-b15+b45, depth-1)
		m58 =mat455( a11+a31+a12-a22-a42+a23+a33+a43+a14-a24-a44-2*a15+a25-a35+a45,b12-b32+b52+b14-b24, depth-1)
		m59 =mat455( -a21-a22-a13-2*a23+a43-a24-a15+a45,-b21-b51-b13+b33-b53+b15-b35+b55, depth-1)
		m60 =mat455( a11-a31+a12-a32+a14-a34-a15+a35,b21-b23+2*b14-b34+b54+b25, depth-1)
		m61 =mat455( a22-a23-a14-a24+a44-a25,2*b12-b22-b42+b13-b43-2*b14+b24+b44-b15+b45, depth-1)
		m62 =mat455( a14+a24-a44,2*b12-b22-b42-2*b14+b24+b44, depth-1)
		m63 =mat455( -a22+a23+a24+a25,3*b12-b32-b42+b52+b13-b43-b14+b44-b15+b45, depth-1)
		m64 =mat455( a21+a31+a23+a33-a25-a35,b21+b51-b22-b52+b23+b53, depth-1)
		m65 =mat455( a31+a32+a13+a34+a15-a35,b21-b23+b14+b24-b44+b54+b25, depth-1)
		m66 =mat455( a13+a33+a14+a34+a15+a35,-2*b14+b24+b44, depth-1)
		m67 =mat455( a21+a31+a23+a33+a24+a34,2*b11-b31+b51+2*b12-b32+b52+2*b13-b33+b53, depth-1)
		m68 =mat455( -a13+a43-a15+a45,b21+b51+2*b13-b23-b33-2*b15+b25+b35, depth-1)
		m69 =mat455( a31+a33-a24+a34,-b11+b41+2*b12-b32+b52+b13-b43-b15+b45, depth-1)
		m70 =mat455( a21-a41+a22-a42+a13+2*a23-2*a43+a24-a44+a15,-b13+b33-b53+b15-b35+b55, depth-1)
		m71 =mat455( -a22-a32+a23+a33-a24-a34+a25+a35,b11+b21-b41+b51+b12+b22-b42+b52+b13+b23-b43+b53, depth-1)
		m72 =mat455( a13+a33+a24+a34+a44+a15+a35,b12-b22-b32-b24+b44, depth-1)
		m73 =mat455( a13+a15,b51+b13+b23-b43+b55, depth-1)
		m74 =mat455( a11+2*a13-a43+a14,b11-b31+b51+b13+b15-b35+b55, depth-1)
		m75 =mat455( a21+a22+a23+a24,-b22-b52+b24+b54, depth-1)
		m76 =mat455( a43+a44+a45,b21+b51+b23+b53, depth-1)
		
		c11 = -m6-m18+m27-m28-m29-m31+m33+m39+m43-m44-m47-m49+m56-m57-m74
		c12 = m8-m9+m11+m19+m25+m29+m32-m41-m42+m49-m50+m52+m56+m57-m58+m61+m63+m69+m71
		c13 = m6+m18-m27+m28-m42-m43+m55+m74
		c14 = m3-m4-m9+m19+m24+m27-m42-m50+m60+m65
		c15 = m4+m6+m18-2*m27+m28+m29+m31-m39-m42-m43+m44+m47+m55-m56+m57+m73+m74
		c21 = -m12+m13+m16+m17-m22+m29-m34-m43-m53-m54+m61+m62+m67-m69
		c22 = m7-m9-m13-m29+m32+m36-m41-m42-m50+m56-m61-m62-m63+m64-m66+m72+m76
		c23 = m1+m7+m12+m21+m32+m34+m36-m37-m42+m43-m50+m53+m54+m56-m66+m72+m76
		c24 = m5+m7-m9-m12+m32-m34+m36-m41-m42-m43-m50+m56+m64-m66+m72+m75+m76
		c25 = -m50+2*m53+m54+m56+m59+m21-m16+m12+m1+m7+m10-m42+m43+m34+m36-m37-m66+m68+m72+m32-m61-m62-m29+m75+m76+m23
		c31 = -m11+m14-m16-m17-m21+m22+m24-m26+m27-m28-m29-m32+m40-m45-m49-m51-m56-m57-m61-m62-m72
		c32 = m9+m11+m26+m29-m32+m41+m42+m49+m50+m51-m56+m57+m61+m62+m63+m66+m69+m71-m72
		c33 = -m14-m24-m27+m28+m37-m40+m42+m50+m66
		c34 = m3+m9+m14-m20+m24+m27+m42+m50+m66
		c35 = m50+m56+m57+m20+m21+m16+m17-2*m14-m6+m11+m42+m45+m48-2*m40+m37+m66+m72+m73+m65+m32+m61+m62+m26-2*m27+m28+m29-2*m24
		c41 = -m6-m13-m18-m25-m28+m30-m38-m44-m49-m53+m56-m57-m59-m69-m70
		c42 = m8+m11+m13+m25+m36+m38+m46+m49+m57+m64+m69+m71+m76
		c43 = m6+m18+m28+m35+m39+m53+m55-m56+m59+m70+m74+m76
		c44 = m2+m3-m4+m5-m12+m15-m23+m24+m27-m32+m36+m41-m43+m46-m56+m58+m60+m64+m65+m76
		c45 = m2+m4+m6+m18+m28+m35+m39+m44+m47+2*m53+m55-2*m56+m57+2*m59+m68+2*m70+m73+m74+m76

	result = np.concatenate((np.concatenate((c11, c21, c31, c41), axis=0), np.concatenate((c12, c22, c32, c42), axis=0), np.concatenate((c13, c23, c33, c43), axis=0), np.concatenate((c14, c24, c34, c44), axis=0), np.concatenate((c15, c25, c35, c45), axis=0)), axis=1)

	return result


def mat555mod2(a,b,depth):

	a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55 = div5x5(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45, b51, b52, b53, b54, b55 = div5x5(b)


	if depth == 0:
		return strassenInit(a,b,False)
	else:
		m1 =mat555mod2( a22,b24, depth-1)
		m2 =mat555mod2( a22^a42^a43,b23^b33^b34, depth-1)
		m3 =mat555mod2( a22^a42^a45,b22^b52^b54, depth-1)
		m4 =mat555mod2( a41^a22^a42,b14^b15^b25, depth-1)
		m5 =mat555mod2( a21,b14, depth-1)
		m6 =mat555mod2( a21^a51^a53,b13^b33^b34, depth-1)
		m7 =mat555mod2( a22^a42,b22^b52^b23^b33^b14^b24^b34^b54^b15^b25, depth-1)
		m8 =mat555mod2( a23,b34, depth-1)
		m9 =mat555mod2( a11^a13^a23,b14^b15^b35, depth-1)
		m10 =mat555mod2( a13^a23,b21^b31^b32^b52^b14^b24^b34^b54^b15^b35, depth-1)
		m11 =mat555mod2( a13^a23^a15,b32^b52^b54, depth-1)
		m12 =mat555mod2( a21^a51^a55,b12^b52^b54, depth-1)
		m13 =mat555mod2( a12^a13^a23,b21^b31^b24, depth-1)
		m14 =mat555mod2( a21^a51^a22^a42^a13^a23^a15^a25^a45^a55,b52^b54, depth-1)
		m15 =mat555mod2( a21^a51,b11^b21^b12^b52^b13^b33^b14^b24^b34^b54, depth-1)
		m16 =mat555mod2( a21^a51^a52,b11^b21^b24, depth-1)
		m17 =mat555mod2( a25,b54, depth-1)
		m18 =mat555mod2( a25^a35,b21^b51^b33^b53^b14^b24^b34^b54^b15^b55, depth-1)
		m19 =mat555mod2( a32^a25^a35,b21^b51^b24, depth-1)
		m20 =mat555mod2( a33^a25^a35,b33^b53^b34, depth-1)
		m21 =mat555mod2( a11^a21^a31^a41^a22^a42^a13^a23^a25^a35,b14^b15, depth-1)
		m22 =mat555mod2( a21^a51^a22^a42^a23^a33^a43^a53^a25^a35,b33^b34, depth-1)
		m23 =mat555mod2( a31^a25^a35,b14^b15^b55, depth-1)
		m24 =mat555mod2( a33,b31^b33^b53^b44^b35^b45, depth-1)
		m25 =mat555mod2( a31^a24^a34^a44^a54^a45^a55,b55, depth-1)
		m26 =mat555mod2( a31^a24^a34,b13^b43^b44, depth-1)
		m27 =mat555mod2( a11^a31^a41^a51^a53^a14^a24^a34^a44,b42^b13^b44^b35, depth-1)
		m28 =mat555mod2( a11^a31^a41^a51^a13^a33^a43^a53,b35, depth-1)
		m29 =mat555mod2( a43,b32^b23^b33^b35, depth-1)
		m30 =mat555mod2( a24^a44^a54,b41, depth-1)
		m31 =mat555mod2( a33^a24^a34,b44^b35^b45, depth-1)
		m32 =mat555mod2( a24^a34,b13^b43^b44^b35^b45, depth-1)
		m33 =mat555mod2( a44,b41, depth-1)
		m34 =mat555mod2( a14^a24^a34^a54,b41, depth-1)
		m35 =mat555mod2( a24^a54^a55,b43^b53^b44, depth-1)
		m36 =mat555mod2( a11,b11^b12^b42^b44^b15^b35, depth-1)
		m37 =mat555mod2( a42^a43,b23, depth-1)
		m38 =mat555mod2( a14^a34^a44^a54^a15^a35^a45^a55,b32^b53, depth-1)
		m39 =mat555mod2( a44,b41^b42^b43^b45, depth-1)
		m40 =mat555mod2( a31,b11^b13^b43^b44^b15^b55, depth-1)
		m41 =mat555mod2( a11^a31^a41^a51^a12^a42^a52,b11^b25, depth-1)
		m42 =mat555mod2( a12,b21^b31^b22^b25, depth-1)
		m43 =mat555mod2( a42^a52^a43,b31^b23, depth-1)
		m44 =mat555mod2( a11^a41^a12^a42,b11, depth-1)
		m45 =mat555mod2( a32,b21^b51^b23^b25, depth-1)
		m46 =mat555mod2( a11^a31^a51^a52,b11^b25, depth-1)
		m47 =mat555mod2( a11^a31^a51^a12^a32^a52,b25, depth-1)
		m48 =mat555mod2( a31^a41^a51^a53^a24^a34,b42^b13^b44^b35, depth-1)
		m49 =mat555mod2( a12^a42^a52^a13^a33^a43,b31^b23, depth-1)
		m50 =mat555mod2( a12^a32^a42^a52^a35^a45^a55,b51^b22, depth-1)
		m51 =mat555mod2( a32^a35,b51, depth-1)
		m52 =mat555mod2( a52,b11^b21^b22^b23, depth-1)
		m53 =mat555mod2( a42^a52^a43^a53,b31, depth-1)
		m54 =mat555mod2( a55,b51^b12^b52^b43^b53^b44, depth-1)
		m55 =mat555mod2( a32^a35^a55,b51^b22, depth-1)
		m56 =mat555mod2( a13^a33^a43^a53^a15^a35^a45^a55,b32, depth-1)
		m57 =mat555mod2( a41,b12^b13^b15^b25, depth-1)
		m58 =mat555mod2( a45,b22^b52^b53^b55, depth-1)
		m59 =mat555mod2( a11^a31^a41^a51^a14^a34^a44^a54,b45^b55, depth-1)
		m60 =mat555mod2( a33^a14^a24^a34^a44^a15,b32^b53^b44^b45, depth-1)
		m61 =mat555mod2( a42^a45,b22, depth-1)
		m62 =mat555mod2( a31^a41^a24^a34^a44^a54^a55,b12, depth-1)
		m63 =mat555mod2( a33^a14^a24^a34^a15,b44^b45, depth-1)
		m64 =mat555mod2( a24^a34^a44^a54,b12^b22^b32^b42^b52, depth-1)
		m65 =mat555mod2( a53^a24^a54,b32^b42^b44, depth-1)
		m66 =mat555mod2( a31^a51^a53^a24^a34,b13, depth-1)
		m67 =mat555mod2( a54,b41, depth-1)
		m68 =mat555mod2( a24^a54,b32^b42^b43^b53^b44, depth-1)
		m69 =mat555mod2( a12^a42^a52,b11^b21^b31^b51, depth-1)
		m70 =mat555mod2( a24,b44, depth-1)
		m71 =mat555mod2( a14^a24^a15,b44^b45^b55, depth-1)
		m72 =mat555mod2( a12^a13,b31, depth-1)
		m73 =mat555mod2( a53,b31^b32^b42^b13^b33^b44, depth-1)
		m74 =mat555mod2( a31^a41^a51^a53^a24^a34^a44,b42^b44, depth-1)
		m75 =mat555mod2( a15,b51^b32^b52^b44^b45^b55, depth-1)
		m76 =mat555mod2( a31^a24^a34^a54^a55,b43^b44, depth-1)
		m77 =mat555mod2( a32^a52^a35^a55,b22, depth-1)
		m78 =mat555mod2( a41^a42,b25, depth-1)
		m79 =mat555mod2( a31^a41^a51^a24^a34^a44^a54,b12^b42^b44, depth-1)
		m80 =mat555mod2( a51^a52,b11, depth-1)
		m81 =mat555mod2( a31^a41^a51^a43^a53^a24^a34,b35, depth-1)
		m82 =mat555mod2( a33^a24^a54^a35^a55,b53, depth-1)
		m83 =mat555mod2( a13^a33^a43,b41^b13^b23^b33^b43^b53, depth-1)
		m84 =mat555mod2( a12^a32^a42^a13^a33^a43,b23, depth-1)
		m85 =mat555mod2( a31^a24^a34^a44^a54^a55,b12^b43^b44^b55, depth-1)
		m86 =mat555mod2( a13^a33^a43^a14^a24^a34^a44,b41^b32^b13^b43^b53^b35, depth-1)
		m87 =mat555mod2( a11^a31^a41^a51^a24^a34^a44^a54,b12^b42^b44^b45^b55, depth-1)
		m88 =mat555mod2( a21^a51^a12^a22^a32^a52^a13^a23^a25^a35,b21^b24, depth-1)
		m89 =mat555mod2( a24^a34^a44^a54^a35^a45^a55,b22^b32^b52, depth-1)
		m90 =mat555mod2( a33^a43^a24^a54^a35^a45^a55,b32, depth-1)
		m91 =mat555mod2( a14^a34^a44^a54^a15^a35^a45^a55,b32^b53^b55, depth-1)
		m92 =mat555mod2( a12^a42^a52^a15^a45^a55,b51, depth-1)
		m93 =mat555mod2( a11^a53^a14^a24^a54,b42^b44, depth-1)
		m94 =mat555mod2( a11^a31^a41^a51,b15^b25^b35^b45^b55, depth-1)
		m95 =mat555mod2( a14^a54,b41, depth-1)
		
		c11 = m41^m42^m44^m46^m50^m51^m61^m67^m72^m77^m78^m92^m95
		c12 = m50^m51^m56^m59^m61^m65^m70^m71^m75^m77^m79^m87^m90^m92^m93
		c13 = m24^m27^m28^m29^m31^m32^m34^m39^m43^m48^m49^m56^m60^m63^m65^m67^m72^m81^m83^m86^m90^m93
		c14 = m8^m9^m10^m11^m13^m36^m41^m42^m44^m46^m50^m51^m59^m61^m70^m71^m75^m77^m78^m79^m87^m92
		c15 = m28^m31^m36^m41^m44^m46^m59^m63^m70^m71^m78^m79^m81^m87
		c21 = m1^m13^m16^m19^m30^m33^m51^m67^m72^m80^m88
		c22 = m3^m11^m12^m14^m17^m56^m61^m62^m65^m70^m74^m79^m90
		c23 = m2^m6^m8^m20^m22^m26^m35^m37^m66^m70^m76^m82
		c24 = m1^m5^m8^m17^m70
		c25 = m4^m5^m9^m21^m23^m25^m28^m31^m38^m63^m70^m71^m78^m81^m91
		c31 = m30^m33^m34^m37^m41^m43^m44^m45^m47^m49^m51^m67^m72^m78^m80^m84^m95
		c32 = m25^m33^m35^m38^m39^m51^m54^m55^m58^m60^m63^m64^m68^m76^m82^m85^m89
		c33 = m24^m26^m31^m32^m35^m37^m43^m49^m70^m72^m76^m82^m84
		c34 = m17^m18^m19^m20^m23^m24^m26^m31^m32^m37^m40^m41^m43^m44^m45^m47^m49^m70^m72^m78^m80^m84
		c35 = m25^m26^m31^m32^m38^m40^m41^m44^m47^m63^m70^m71^m78^m80^m91
		c41 = m33^m37^m41^m42^m43^m46^m50^m52^m55^m61^m69^m78
		c42 = m25^m33^m38^m39^m58^m60^m61^m62^m63^m76^m82^m85^m90
		c43 = m29^m33^m37^m38^m39^m48^m60^m63^m66^m74^m81^m82^m90
		c44 = m1^m2^m3^m4^m7^m25^m29^m33^m38^m39^m48^m57^m58^m60^m62^m63^m66^m74^m76^m81^m82^m85^m90
		c45 = m25^m33^m39^m48^m57^m62^m66^m74^m76^m78^m81^m85
		c51 = m37^m43^m51^m52^m53^m55^m67^m77^m80
		c52 = m35^m51^m54^m55^m62^m65^m68^m70^m74^m77^m79
		c53 = m26^m35^m37^m43^m53^m65^m66^m68^m70^m73^m76
		c54 = m5^m6^m12^m15^m16^m35^m37^m43^m51^m52^m53^m54^m55^m65^m68^m70^m73^m77
		c55 = m26^m32^m33^m36^m39^m40^m46^m48^m57^m62^m66^m74^m76^m79^m80^m85^m87^m94

	result = np.concatenate((np.concatenate((c11, c21, c31, c41, c51), axis=0), np.concatenate((c12, c22, c32, c42, c52), axis=0), np.concatenate((c13, c23, c33, c43, c53), axis=0), np.concatenate((c14, c24, c34, c44, c54), axis=0), np.concatenate((c15, c25, c35, c45, c55), axis=0)), axis=1)

	return result


def mat555(a,b,depth):

	a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55 = div5x5(a)
	b11, b12, b13, b14, b15, b21, b22, b23, b24, b25, b31, b32, b33, b34, b35, b41, b42, b43, b44, b45, b51, b52, b53, b54, b55 = div5x5(b)


	if depth == 0:
		return strassenInit(a,b,True)
	else:
		m1 =mat555( -a51+2*a52+2*a54-2*a55,3*b11+b21+b41, depth-1)
		m2 =mat555( a53,2*b12-b32-b52-2*b14+b34+b54+4*b15-2*b35-2*b55, depth-1)
		m3 =mat555( a51-2*a52-a54+2*a55,2*b11+b41, depth-1)
		m4 =mat555( -a53+a55,b21+b51, depth-1)
		m5 =mat555( a41-a42-2*a44+2*a45,-2*b11-b21+2*b12+b22, depth-1)
		m6 =mat555( a44,3*b12+b22+b42, depth-1)
		m7 =mat555( -a51+2*a52-a44+2*a54-2*a55,2*b11+b41+b12+b22, depth-1)
		m8 =mat555( -a44+a54,-2*b11-b41+2*b12+b42, depth-1)
		m9 =mat555( -a41+2*a42+a44-2*a45,b12+b22, depth-1)
		m10 =mat555( a45,2*b11-b31-b51-2*b12+b32+b52, depth-1)
		m11 =mat555( -a43+a45,-b11-b21-b31+b12+b22+b32, depth-1)
		m12 =mat555( a41-a51-2*a42+2*a52+a43-2*a44+2*a54+a45-2*a55,-b11-b21+b12+b22, depth-1)
		m13 =mat555( -a31+2*a32+2*a34-2*a35,3*b14+b24+b44-6*b15-2*b25-2*b45, depth-1)
		m14 =mat555( a31-a41-2*a32+2*a42-2*a34+2*a44+2*a35-2*a45,-b11-b21-b31+b32+b14+b24+b34-2*b15-2*b25-2*b35, depth-1)
		m15 =mat555( -a31+2*a32+2*a34-a44-2*a35,b12+b22+2*b14+b44-4*b15-2*b45, depth-1)
		m16 =mat555( -a31+a41+2*a32-2*a42+a43+2*a34-2*a44-2*a35+a45,-b11-b21-b31+b12+b22+b32+b34-2*b35, depth-1)
		m17 =mat555( -a31+a51+a32-a52+2*a34-2*a54-2*a35+2*a55,b22+b52, depth-1)
		m18 =mat555( -a31+a41+a32-a42+2*a34-2*a44-2*a35+2*a45,b21+b31+b51-b22-b32-b52+b24+b34+b54-2*b25-2*b35-2*b55, depth-1)
		m19 =mat555( a33-a53,-2*b12+b32+b52, depth-1)
		m20 =mat555( -a33+a43+a53,b32, depth-1)
		m21 =mat555( -a34+a54,b12-b42+b52-b14+b44-b54+b15-b45+b55, depth-1)
		m22 =mat555( -a34+a44,-2*b11-b41+2*b12+b42, depth-1)
		m23 =mat555( -a34+a44,-2*b12-b42+2*b14+b44-4*b15-2*b45, depth-1)
		m24 =mat555( a31-2*a32-a34+2*a35,2*b14+b44-4*b15-2*b45, depth-1)
		m25 =mat555( a35,b24+b34+b54-2*b25-2*b35-2*b55, depth-1)
		m26 =mat555( -a53+a35-a45,b21+b31+b51-b32, depth-1)
		m27 =mat555( -a31+a32+2*a34-a35,2*b14+b24-4*b15-2*b25, depth-1)
		m28 =mat555( a31-a41-a32+a42-2*a34+2*a44+a35-2*a45,-2*b11+b31+b51+2*b12-b32-b52+b24+b34+b54-2*b25-2*b35-2*b55, depth-1)
		m29 =mat555( a31-a51-a32+a52-2*a34+2*a54+a35+a45-a55,2*b11+b21-2*b12+b52, depth-1)
		m30 =mat555( -a31+a41+a32-a42+2*a34-2*a44-a35+a45,-2*b11+b31+b51+2*b12-b32-b52-2*b14+b34+b54+4*b15-2*b35-2*b55, depth-1)
		m31 =mat555( a31-a41-a32+a42+a53-2*a34+2*a44+a35-a45,b21+b31+b51+2*b12-b32-b52-2*b14+b34+b54+4*b15-2*b35-2*b55, depth-1)
		m32 =mat555( -a31+a41+a51+a32-a42-a52+2*a34-2*a44-2*a54-a35+a45+a55,2*b11+b21, depth-1)
		m33 =mat555( -a33+a35,b34-2*b35, depth-1)
		m34 =mat555( -a31+a41+2*a32-2*a42-a33+a43+2*a34-2*a44-a35+a45,-b31+b32+b34-2*b35, depth-1)
		m35 =mat555( -a31+a51+a32-a52-a33+a53+2*a34-2*a54-a35+a55,-2*b12+b52, depth-1)
		m36 =mat555( -a34+a54-a35+a55,-2*b12+b32+b52+2*b14-b34-b54-2*b15+b35+b55, depth-1)
		m37 =mat555( a23,b21+b31-b22-b32-b23-b33+b25+b35, depth-1)
		m38 =mat555( -a22+a23,-b11+b21-b41+b13-b23+b43, depth-1)
		m39 =mat555( a41+a22-2*a42-a23+2*a24-4*a44+2*a25+2*a45,b11+b21+b31-b12-b22-2*b32-b13-b23-b33+b15+b25+b35, depth-1)
		m40 =mat555( a22-a42-a23+a43,-2*b13+b33+b53, depth-1)
		m41 =mat555( a41+a22-2*a42-a23+a43+2*a24-4*a44+2*a25+a45,-2*b21-b31+b41-2*b12+2*b22+3*b32-b42+b52-2*b13+2*b23+2*b33-b43+b53+2*b14-b34-b54-2*b15-2*b25+b45+b55, depth-1)
		m42 =mat555( -a24+a44,b15-b45+b55, depth-1)
		m43 =mat555( a25,-b11+b41-b51+2*b12-2*b42+2*b52+b13-b43+b53-2*b15+2*b45-2*b55, depth-1)
		m44 =mat555( a21-a41-2*a22+2*a42-4*a24+4*a44-5*a25-2*a45,b11+b21+b31-2*b12-2*b22-2*b32-b13-b23-b33+b15+b25+b35, depth-1)
		m45 =mat555( -a21+a22+2*a24+3*a25,2*b11+b21+b31-4*b12-2*b22-2*b32-2*b13-b23-b33+2*b15+b25+b35, depth-1)
		m46 =mat555( a24-a44+a25,-2*b22+b42+b15-b45+b55, depth-1)
		m47 =mat555( -a23+a43+a24-a44+a25-a45,3*b12+b22+b32-3*b14-b24-b34+3*b15+b25+b35, depth-1)
		m48 =mat555( a22-a23+a24+a25,-2*b11-b41+2*b13+b43, depth-1)
		m49 =mat555( a41+a22-2*a42-a23+a43+a24-3*a44+a25+a45,-2*b21+b41-4*b12+b22+b32-b42+b52-4*b13+b23+b33-b43+b53+4*b14+b24-b34-b54-4*b15-3*b25+b35+b45+b55, depth-1)
		m50 =mat555( -a22+a42+a23-a43-a24+a44-a25+a45,b23+b33+b53, depth-1)
		m51 =mat555( a11-a41-a51-2*a12+2*a42+2*a52+2*a14-2*a44-2*a54+2*a15-2*a45-2*a55,3*b12+b22+b32+3*b13+b23+b33-b43+b53-3*b14-b24-b34+4*b15+b25+b35-b45+b55, depth-1)
		m52 =mat555( a11-a21-a51-2*a12+2*a22+2*a52+2*a14-2*a24-2*a54+2*a15-2*a25-2*a55,b13, depth-1)
		m53 =mat555( -a11+a21+a31+2*a12-2*a22-2*a32-2*a14+2*a24+2*a34-2*a15+2*a25+2*a35,3*b12+b22-b42+b52+3*b13+b23-b43+b53-3*b14-b24+b44-b54+3*b15+b25-b45+b55, depth-1)
		m54 =mat555( a11-a21-a31-2*a12+2*a22+2*a32+2*a14-2*a24-3*a34+a54+2*a15-2*a25-2*a35,b12-b42+b52-b43+b53-b14+b44-b54+b15-b45+b55, depth-1)
		m55 =mat555( a11-a41-a51-2*a12+2*a42+2*a52+2*a14+a24-3*a44-2*a54+2*a15-2*a45-2*a55,-b43+b53+b15-b45+b55, depth-1)
		m56 =mat555( a11-a41-a51-2*a12+2*a42+2*a52-a23+a43+2*a14+a24-3*a44-2*a54+2*a15+a25-3*a45-2*a55,3*b12+b22+b32+2*b13+b23+b33-3*b14-b24-b34+3*b15+b25+b35, depth-1)
		m57 =mat555( -a11+a31+a41+2*a12-2*a32-2*a42+a23-a43-2*a14-a24+3*a34+3*a44-a54-2*a15-a25+2*a35+3*a45,b12-b14+b15, depth-1)
		m58 =mat555( -a11+a41+a51+2*a12-2*a42-2*a52+a23+a33-a43-a53-2*a14-a24-a34+3*a44+3*a54-2*a15-a25-a35+3*a45+3*a55,2*b12+b22+b32+2*b13+b23+b33-2*b14-b24-b34+2*b15+b25+b35, depth-1)
		m59 =mat555( a31-a41+a12-a22-2*a32+a42-2*a34+2*a44+2*a35-2*a45,-5*b12-b42+b52+4*b14+b24-b54-3*b15-2*b25+b45+b55, depth-1)
		m60 =mat555( -a12+a42+a52+a23-a43-a24+a44-a25+a45,2*b13+b23+b33, depth-1)
		m61 =mat555( a12-a32-a42-a23+a43+a24-a44+a25-a45,2*b12+b22-2*b14-b24+2*b15+b25, depth-1)
		m62 =mat555( a12-a42-a52-a23-a33+a43+a53+a24+a34-a44-a54+a25+a35-a45-a55,2*b12+b22+2*b13+b23+b33-2*b14-b24+2*b15+b25, depth-1)
		m63 =mat555( a11-a21-a41-a12+a22+a42-2*a14+2*a24+2*a44-2*a15+2*a25+2*a45,-b12+b42-b52+b15-b45+b55, depth-1)
		m64 =mat555( a11-a41-a12+a42+a23-2*a14+2*a44-2*a15+2*a45,b11-b12-b13+b15, depth-1)
		m65 =mat555( -a11+a21+a41+a12-a22-a42+2*a14-2*a24-2*a44+2*a15-3*a25-2*a45,b11-2*b12+b42-b52-b13+2*b15-b45+b55, depth-1)
		m66 =mat555( a13-a43,2*b15+b25+b35, depth-1)
		m67 =mat555( -a41-a22+2*a42-a13+2*a23-a43-2*a24+4*a44-2*a25,-2*b21+b41-3*b12+b22+b32-b42+b52-4*b13+b23+b33-b43+b53+2*b14-b34-b54-b15-b25+b35+b45+b55, depth-1)
		m68 =mat555( a13-a23-a43,-b11-b21-b31+2*b12+2*b22+2*b32+b13+b23+b33-2*b15-2*b25-2*b35, depth-1)
		m69 =mat555( -a13+a23+a43,-b12-b22-b32+b15+b25+b35, depth-1)
		m70 =mat555( a13-a23-a45,-4*b12-b42+b52+2*b14-b34-b54+2*b35+b45+b55, depth-1)
		m71 =mat555( -a21+a22+a13-a43+2*a24+3*a25,b11+b21+b31-2*b12-2*b22-2*b32-b13-b23-b33+b25+b35, depth-1)
		m72 =mat555( a13-a23+a24-a44+a25-a45,-2*b21+b41-4*b13+b23+b33-b43+b53, depth-1)
		m73 =mat555( a51+a12-a42-2*a52+a13-2*a23+a43+2*a24-2*a44-2*a54+2*a25-2*a45+2*a55,3*b11+b21+b41-3*b13-b43+b53, depth-1)
		m74 =mat555( -a12+a42+a52+a13-a43,2*b15+b25, depth-1)
		m75 =mat555( a12-a22-a42-a13+a23+a43,-b12-b22+b15+b25, depth-1)
		m76 =mat555( a14-a44-a54,-b42+b52+b44-b54-b45+b55, depth-1)
		m77 =mat555( a14-a24-a54,-b43+b53, depth-1)
		m78 =mat555( -a11+a41+a51+2*a12-2*a42-2*a52-3*a14+3*a44+3*a54-2*a15+2*a45+2*a55,-b43+b53-b45+b55, depth-1)
		m79 =mat555( -a11+a21+a31+2*a12-2*a22-2*a32-3*a14+3*a24+3*a34-2*a15+2*a25+2*a35,-b42+b52-b43+b53+b44-b54-b45+b55, depth-1)
		m80 =mat555( a15-a45,-b41+b51+b42-b52+b43-b53-b45+b55, depth-1)
		m81 =mat555( a11-a21-a41-a12+a22+a42-2*a14+2*a24+2*a44-3*a15+3*a25+3*a45,b42-b52-b45+b55, depth-1)
		m82 =mat555( a14-a44+a15-a45,b11-b21+b41-b12+b22-b42-b13+b23-b43+b15-b25+b45, depth-1)
		m83 =mat555( a14-a44-a54+a15-a45,3*b12+b22+b42-3*b15-b45+b55, depth-1)
		m84 =mat555( -a14+a44+a54-a15+a45+a55,-2*b13+b33+b53, depth-1)
		m85 =mat555( a14-a44-a54+a15-a45-a55,-2*b12+b32+b52+2*b14-b34-b54-2*b15+b35+b55, depth-1)
		m86 =mat555( a53+a14-a44-a54+a15-a45-a55,2*b12-b32-b52-2*b14+b34+b54+4*b15-b35-2*b55, depth-1)
		m87 =mat555( a22-a23+a14-a44+a15-a45,-b11+b21-b41-b12-b22+b13-b23+b43+b15+b25, depth-1)
		m88 =mat555( a22-a42-a23+a43+a14-a34-a44+a15-a35-a45,2*b12+b22+b23+b33+b53-2*b14-b24+2*b15+b25, depth-1)
		m89 =mat555( -a14+a24+a44-a15+a25+a45,-2*b12-b42+2*b15+b45, depth-1)
		m90 =mat555( -a14+a24+a34-a15+a25+a35,b22+b32+b52+b23+b33+b53-b24-b34-b54+b25+b35+b55, depth-1)
		m91 =mat555( a11-a21-a31-2*a12+3*a22+3*a32-a42-a52-a23-a33+a43+a53+3*a14-2*a24-2*a34-a44-a54+3*a15-2*a25-2*a35-a45-a55,2*b12+b22+2*b13+b23-2*b14-b24+2*b15+b25, depth-1)
		m92 =mat555( -a51-a12+a42+2*a52-2*a13+3*a23-a43+a14-3*a24+2*a44+a54+a15-3*a25+2*a45-2*a55,2*b11+b41-4*b13-b43+b53, depth-1)
		m93 =mat555( a13-a23-a33-a14+a24+a34-a15+a25+a35,b32-b34+b35, depth-1)
		m94 =mat555( -a12+a42+a13-a43-a14+a44-a15+a45,b11+b21-b12-b22-b13-b23+b15+b25, depth-1)
		m95 =mat555( a51+a12-a42-2*a52-a13+a43-a14+a44-a54-a15+a45+2*a55,b12+b22+b15, depth-1)
		m96 =mat555( a12-a42-a52-a13+a43+a53+a14-a44-a54+a15-a45-a55,b33, depth-1)
		m97 =mat555( -a31+a41-a12+a22+2*a32-a42+a13-a23-a14+a24+3*a34-2*a44-a15+a25-2*a35+2*a45,-4*b12-b42+b52+2*b14-b54+b45+b55, depth-1)
		
		c11 = m51-m55-m56+m19+m20+m12+2*m1+m3-m7+m9-m10+m11-m42+m45+m47+m35+2*m37-m66-2*m68+2*m69-m71+m72+m73+2*m64+m65+m32+m29-m77+m80+m81+m92
		c12 = m55+m19+m20+m3+m5+2*m6+m7+m8+m9+m42+m45+m35+m37+m95-m68+m69-m71+m64+m65+m32+m29+m77+m78+m81+m83
		c13 = m50+m51-m55-m56+m12+2*m1+m3-m7+m9+m11+m41-m42+m47+m48+m40+2*m38+m39+m94+m67+m69+m70+2*m72+m73+m75-m77+m87+m92
		c14 = 3*m49+2*m50+2*m55+m57+m59+2*m19+2*m20+m21-m15+m16+2*m13+m14+2*m3+2*m5+4*m6+2*m7+2*m8+3*m9-m10+m11+2*m42+m45+m47+2*m35+2*m36+m37+4*m38+2*m95+m97+m66+3*m67-m68+3*m69+2*m70-m71+3*m72+m64+m65+2*m32+m27+m28+2*m29+m30+2*m75+m76+m24+2*m77+2*m78+m81+4*m82+2*m83+2*m85+4*m87+2*m88+2*m89+2*m90
		c15 = m49+m50+m55+m19+m20+m3+m5+2*m6+m7+m8+m9-m10+m42+m35+m36+2*m38+m95+m66+m67+m69+m70+m72+m32+m27+m28+m29+m30+m75+m77+m78+2*m82+m83+m85+2*m87+m88+m89+m90
		c21 = m51-m52-m55-m56+m12+m1-m7+m9+m11+m41-m42-m43+m45+m47+2*m37+m39-m66+m67-m68+m69+m70-m71+m72+2*m63+2*m64+2*m65
		c22 = m6+m9+m37+m39+m42+m44+m45+m46+m63+m64+m65
		c23 = m1-m7+m9+m11+m12+m38+m39+m41-m42+m47+m48+m51-m52-m55-m56+m67+m69+m70+m72
		c24 = m49+m54+m57-m15+m16+m13+m14+2*m6+3*m9+m11+2*m42+2*m44+m45+2*m46+m47+m37+2*m38+2*m39+m66+m67+m68+m69+m70+m71+m72+m63+m64+m65+m76+m77+m79+2*m82+2*m87+2*m89
		c25 = m6+m9+m38+m39+m42+m44+m46+m66+m68+m71+m82+m87+m89
		c31 = m1-m2-m7-m10+m12+m15-m16+m19+m22+m23+m24+m26+m29+m30+m31+m32-m33+m34+m35
		c32 = -m2+m5+m6-m10+m15+m18+m19+m23+m24+m25+m26+m28+m29+m30+m31+m32+m35
		c33 = m1+m3-m21+m38+m40+m52+m53+m54+m61-m62+m72+m73+m75+m87-m88+m91+m92+m94+m96
		c34 = 2*m49+2*m59+2*m19+2*m15+2*m18+m13-2*m2+2*m5+2*m6-2*m10+2*m35+2*m36+2*m38+2*m97+2*m67+2*m72+2*m31+2*m32+m33+2*m61+2*m26+m27+2*m28+2*m29+2*m30+2*m75+2*m23+3*m24+m25+2*m82+2*m85+2*m87+2*m93
		c35 = m49+m59+m19+m15+m18-m2+m5+m6-m10+m35+m36+m38+m97+m67+m72+m31+m32+m33+m61+m26+m27+m28+m29+m30+m75+m23+m24+m82+m85+m87+m93
		c41 = m1-m7+m9-m10+m11+m12+m19+m20+m29+m32+m35
		c42 = m5+m6+m9+m19+m20+m29+m32+m35
		c43 = m1-m7+m9+m11+m12+m38+m39+m40+m41+m48+m50+m67+m69+m70+m72
		c44 = 2*m49+2*m50+2*m19+2*m20-m15+m16+m13+m14+2*m5+2*m6+3*m9-m10+m11+2*m35+2*m36+2*m38+2*m67+2*m69+2*m70+2*m72+2*m32+m27+m28+2*m29+m30+2*m82+2*m85+2*m87+2*m88+2*m89+2*m90
		c45 = m49+m50+m19+m20+m5+m6+m9-m10+m35+m36+m38+m67+m69+m70+m72+m32+m27+m28+m29+m30+m82+m85+m87+m88+m89+m90
		c51 = m1-m2+m3+m4+m30+m31+m32
		c52 = -m2+m3+m5+m6+m7+m8-m10+m17+m18+m25+m26+m28+m29+m30+m31+m32
		c53 = m1+m3+m38+m60+m72+m73+m75+m84+m87+m92+m94+m96
		c54 = m49+m56+m57+m58+m59+m60+m21+m17+m18+m13-2*m2+2*m3+m5+2*m6+2*m7+2*m8-m10+2*m38+m95+m97+m67+m72+m74+m31+m32+m62+m26+m28+m29+m30+2*m75+m24+m25+2*m82+m83+2*m85+m86+2*m87+m93
		c55 = -m2+m3+m6+m7+m8+m38+m74+m75+m82+m83+m85+m86+m87+m95

	result = np.concatenate((np.concatenate((c11, c21, c31, c41, c51), axis=0), np.concatenate((c12, c22, c32, c42, c52), axis=0), np.concatenate((c13, c23, c33, c43, c53), axis=0), np.concatenate((c14, c24, c34, c44, c54), axis=0), np.concatenate((c15, c25, c35, c45, c55), axis=0)), axis=1)

	return result







#decide what algoritmm to use :3
def multdecide(a,b,mod2):
    
    #square
    sq = False
    n = len(a)
    m = len(b)
    p = len(b[0])
    depth = 0
    
    if n == m and m == p:
        sq = True
        
    if sq:
        if n%4 == 0:
            x = n
            while(x%4 == 0 and x>1000):
                depth += 1
                x = x>>2            
            if n > 1000:
                if mod2:
                    c = mat444mod2(a,b,depth)
                c = strassenInit(a,b,depth)
            else:
                c = strassenInit(a, b, mod2)
        elif n%5 == 0:
            x = n
            while(x%5 == 0 and x>1000):
                depth += 1
                x = x/5            
            if n > 1000:
                if mod2:
                    c = mat555mod2(a,b,depth)
                c = mat555(a,b,depth)
            else:
                c = strassenInit(a, b, mod2)
    elif(n%3 == 0 and m%4 == 0 and p%5 == 0 and not mod2):
        x = n
        y = m
        z = p
        while(x%3 == 0 and y%4 ==0 and z%5==0 and z>1000):
            depth += 1
            x = x/3
            y = y>>2
            z = z/5
        if p > 1000:
            c = mat345(a,b,depth)
        else:
            strassenInit(a,b,mod2)
    elif(n%4 == 0 and n==m and p%5==0):
        x = n
        z = p
        while(x%4 == 0 and z%5==0 and z>1000):
            depth += 1
            x = x >> 2
            z = z/5
        if p > 1000:
            if mod2:
                c = mat445mod2(a,b,depth)
            c = mat445(a,b,depth)
        else:
            strassenInit(a,b,mod2)
    elif(n%4==0 and p%5==0 and m==p and not mod2):
        x = n
        z = p
        while(x%4 == 0 and z%5==0 and z>1000):
            depth += 1
            x = x >> 2
            z = z/5
        if p > 1000:
            c = mat455(a,b,depth)   
    else:
        c = strassenInit(a,b,mod2)
        
        
    return c
    

def matMul(a,b,mod2):
    
    if mod2:
        #convert to bool for xors
        c = multdecide(a.astype(bool), b.astype(bool),True)
        #convert back to int for result
        c = c.astype(int)
    else:
        c = multdecide(a, b,False)
    
    return c
      