from analysis import *

def normal():
    if 0.8*Pc < Pmax < Pc and 0.8*P_intake < P_inxylanh < P_intake:
        value = 'Bình thường'
    else:
        value = 'Hư hỏng'
    return value

def damage():
    if Pci < P_min:
        damage_c ='Gãy xéc măng, gãy xupap hay bị lủng piston'
    elif P_min < Pci <0.62*Pmax:
        damage_c = 'Hở gioăng nắp máy'
    elif 0.62*Pc < Pci <0.8*Pc:
        damage_c = 'Hở xupap'
    elif Pci > Pc:
        damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả'
    elif Pci > 0.9*Pc:
        damage_c = 'Các xy lanh mòn không đều'
    return damage_c

def damage_in():
    if P_inxylanh < 0.8*P_intake:
        damage_in = 'Xuppap bị kẹt (không mở hoàn toàn)'
    elif P_inxylanh > 0.62*P_intake:
        damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín)'
    return damage_in
    
        