from analysis import *

def normal():
    # Pmax lay gia ti lon nhat trong .dat , Pmin lay gia trinho nhat trong .dat
    if 0.8*compression_pressure < Pmax < compression_pressure and 0.8*Minimum_pressure_intake < Pmin < Minimum_pressure_intake:
        value = 'Bình thường'
    else:
        value = 'Hư hỏng'
    return value

def damage():
    if Pci < Minimum_pressure:
        damage_c ='Gãy xéc măng, gãy xupap hay bị lủng piston'
    elif Minimum_pressure < Pci <0.62*compression_pressure:
        damage_c = 'Hở gioăng nắp máy'
    elif 0.62*compression_pressure < Pci <0.8*compression_pressure:
        damage_c = 'Hở xupap'
    elif Pci > compression_pressure:
        damage_c = 'Buồng đốt bị bám mụi than, kẹt xupap xả'
    elif Pci > 0.9*compression_pressure:
        damage_c = 'Các xy lanh mòn không đều'
    return damage_c

def damage_in():
    if Pmin < 0.8*Minimum_pressure_intake:
        damage_in = 'Xuppap bị kẹt (không mở hoàn toàn)'
    elif Pmin > 0.62*P_iMinimum_pressure_intakentake:
        damage_in = 'Lọt khí qua xecmang (xecmang đóng không kín)'
    return damage_in
    
        