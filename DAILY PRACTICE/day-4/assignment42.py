km_to_m=lambda km : km * 1000
m_to_cm=lambda m : m * 100
cm_to_mm=lambda cm : cm * 10
km_to_m=lambda km : km * 1000
ft_to_inch=lambda ft : ft*12
inch_to_cm=lambda inch : inch * 2.54

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
     