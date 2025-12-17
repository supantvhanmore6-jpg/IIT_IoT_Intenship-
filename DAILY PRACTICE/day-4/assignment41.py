def km_to_m(km):
     return km * 1000

def m_to_cm(m):
     return m * 100

def cm_to_mm(cm):
     return cm * 10

def ft_to_inch(ft):
     return ft * 12

def inch_to_cm(inch):
        return inch * 2.54

def distance_converter(dist,conv_type,fun):
    print("your conversion type is = ",conv_type)
    return fun(dist)


i=int(input("enter the distance = "))
str=input("enter the conv type = ")
if str =='km_to_m':
     print(f"{i}km =",distance_converter(i,str,km_to_m),"m")
elif str=='m_to_cm':
     print(f"{i}m =",distance_converter(i,str,m_to_cm),"cm")
elif str=='cm_to_mm':
     print(f"{i}cm =",distance_converter(i,str,cm_to_mm),"mm")
elif str=='ft_to_inch':
     print(f"{i}ft =",distance_converter(i,str,ft_to_inch),"inch")
elif str=='inch_to_cm':
     print(f"{i}inch =",distance_converter(i,str,inch_to_cm),"cm")
     