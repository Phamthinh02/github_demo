def normal():
    if 0.8*Pc < Pmax < Pc and 0.8*P_in < P_inxylanh < P_in:
        value = 'Bình thường'
    else:
        value = 'Hư hỏng'
    return value

def damage():
    if Pci < Pmin:
        damage_c ='Gãy xéc măng, gãy xupap hay bị lủng piston'
    elif Pmin < Pci <0.62*Pmax:
        damage_c = 'Hở gioăng nắp máy'
    elif 0.62*Pmax < Pci <0.8*Pmax:
        damage_c = 'Hở xupap'
    elif Pci > Pmax:
        damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả'
    elif Pci > 0.9*Pmax:
        damage_c = 'Các xy lanh mòn không đều'
    return damage_c

def damage_in():
    if P_inxylanh < 0.8*P_in:
        damage_in = 'Xuppap bị kẹt (không mở hoàn toàn)'
    elif P_inxylanh > 0.62*P_in:
        damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín)'
    return damage_in
    
        