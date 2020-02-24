from __future__ import print_function
twinkle = "Twinkle twinkle, little star. How I wonder what you are. Up above the world so high, Like a diamond in the sky. Twinkle twinkle little star, How I wonder what you are"
twinkleChar = len(twinkle)
twinkle1 = twinkle[:29]
twinkle2 = twinkle[30:56]
twinkle3 = twinkle[57:84]
twinkle4 = twinkle[85:111]
twinkle5 = twinkle[112:140]
twinkle6 = twinkle[141:166]
twinkleLst = [twinkle1, twinkle2, twinkle3, twinkle4, twinkle5, twinkle6]
for i in range(0,6):
    print("line " + str(i+1) + ": " + twinkleLst[i])
print("Number of characters = " + str(twinkleChar))

