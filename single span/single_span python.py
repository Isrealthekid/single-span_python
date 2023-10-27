import math
import matplotlib.pyplot as plt

# this data is gotten from Oyenuga "reinforced concrete design" in page 40 
# its a single span with two point loads and a udl
#Variable Decleration
w1=10 #UDL in lb/ft
P1=120 #Point load at C in lb
P2=80
#w2=200 #UDL in lb/ft
L1=2 #Length in ft
L2=2 #Length in ft
L3=1 #Length in ft
L4=3
pointA=160 #Shear force at A in lb
Rb=120 #Reaction at B in lb
Ra=160 #Reaction at D in lb
d=1.6 #Distance in ft

#Calculations
#The plotting of the Shear force diagram and the Bending Moment Diagram
#Will be done different from that done in the textbook

#Calculations for Shear Force
Area1=w1*L1 #10 * 2
Area2=w1*(L1+L2) #10 * 4
Area3=w1*(L1+L2+L3) #10 * 5
Area4=w1 * (L1+L2+L3+L4) #10 * 8
pointA=pointA # (160)
point_c_left=pointA-Area1 #Shear Force at left of C 160 - 2(10) = 140
point_c_right=point_c_left-Rb #Shear force at right of c 140 - 120 = 20
point_d=pointA-Rb - Area2 #Shear Force at left of  d 160-120-10(4)
point_e_left=pointA-Rb - Area3 #Shear Force at right of e 160 - 120 - 10(5)
point_e_right=point_e_left-P2 #Shear Force at left of e -10 -80
point_b=pointA-Rb - Area4 - P2 #Shear Force at right of b 160 - 120-10(8)-80


# #Calculations for Bending Moments
# AreaV1=0.5*L1*V_B_left #Area of V diagram
# AreaV2=V_C_left*L2 #Area of V diagram from B to C
# AreaV3=V_D_left*(L3-d)*0.5 #Area of V diagram from F to D
# M_A=0 #Moment at A in lb.ft
# M_B=M_A+AreaV1 #Moment about B in lb.ft
# M_C=M_B+AreaV2 #Moment about C in lb.ft
# M_F=M_C+V_C_right*0.5*d #Moment about F in lb.ft
# M_D=M_F+AreaV3 #Moment about D in lb.ft
# M_E=0 #Moment about E in lb.ft

#Result
print ("The following plots are the results")

#Plotting

# Shear Force
x = [0, L1, L1 + 0.000001, L1 + L2, L1 + L2 + L3, L1 + L2 + L3 + 0.000001, L1 + L2 + L3 +L4]
V = [pointA, point_c_left, point_c_right, point_d, point_e_left, point_e_right, point_b]


zero = [0, 0, 0, 0, 0, 0, 0]
plt.plot(x, V, x, zero)
plt.xlabel("Length in m")
plt.ylabel("Shear Force in kN")
plt.title("Shear Force Diagram")
plt.grid()
plt.show()