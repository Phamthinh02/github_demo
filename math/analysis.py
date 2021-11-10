from modules_math import *
from os import *

def math(self):
# Declare value
 extTem_T = self.lineEdit.text()
 comp_rat_T = self.lineEdit.text()
 piston_jour_T = self.lineEdit.text()
 cyl_dm_T = self.lineEdit.text()
 rod_len_T = self.lineEdit.text()
 xupap_cor_T = self.lineEdit.text()
 air_press_T = self.lineEdit.text()

# Charge siing to float
    extTem_V = float(extTem_T)
    comp_rat_V = float(comp_rat_T)
    piston_jour_V = float(piston_jour_T)
    cyl_dm_V = float(cyl_dm_T)
    rod_len_V = float(rod_len_T)
    xupap_cor_V = float(xupap_cor_T)
    air_press_V = float(air_press_T)

# Math
    n_V = math_analysis.n(Temperature = extTem_V ,
                         Compression_ratio = comp_rat_V)
    
    comp_rat_dyn_V = math_analysis.Dynamic_compression_ratio(Piston_journey = piston_jour_V,
                                                            Late_closing_angle = xupap_cor_V,
                                                            Connecting_rod_length = rod_len_V,
                                                            Compression_ratio = comp_rat_V,
                                                            Cylinder_diameter = cyl_dm_V,
                                                            Intake_pressure = air_press_V)
    
    vol_V = math_analysis.Volume(SPiston_journey = piston_jour_V,
                          Late_closing_angle = xupap_cor_V,
                          Connecting_rod_length = rod_len_V,
                          Compression_ratio = comp_rat_V,
                          Cylinder_diameter = cyl_dm_V,
                          Intake_pressure = air_press_V,
                          Temperature = extTem_V)
    
    n_dyn_V = math_analysis.n_dynamic(Piston_journey = piston_jour_V,
                                    Late_closing_angle = xupap_cor_V,
                                    Connecting_rod_length = rod_len_V,
                                    Compression_ratio = comp_rat_V,
                                    Cylinder_diameter = cyl_dm_V,
                                    Intake_pressure = air_press_V,
                                    Intake_pressure = extTem_V)
    
    Lc, Tc, Tz, Pc = math_analysis.Analysis(Temperature = extTem_V,
                                        Dynamic_compression_ratio = comp_rat_dyn_V,
                                        n = n_V,
                                        Intake_pressure = air_press_V,
                                        Volume = vol_V,
                                        n_dynamic = n_dyn_V)

    P_min = math_analysis.Minimum_pressure(Dynamic_compression_ratio = comp_rat_dyn_V)

    P_discharge = math_analysis.Pressure_discharge(Intake_pressure = air_press_V,
                                                Dynamic_compression_ratio = comp_rat_dyn_V,
                                                n = n_V )

    P_intake = math_analysis.Minimum_pressure_intake(Intake_pressure = air_press_V)

    #Insert
    Lc_value = "{}".format(round(Lc*1000,4))
    self.textEdit.setText(Lc_value)
    Tc_value = "{}".format(round(Tc,4))
    Tz_value = "{}".format(round(Tz,4))
    self.textEdit.setText(Tc_value)
    self.textEdit.setText(Tz_value)
    Pc_value = "{}".format(round(Pc,4))
    self.textEdit.setText(Pc_value)
    P_min_value = "{}".format(round(P_min,4))
    self.textEdit.setText(P_min_value)
    P_discharge_value = "{}".format(round(P_discharge,4))
    self.textEdit.setText(P_discharge_value)
    P_intake_value = "{}".format(round(P_intake,4))
    self.textEdit.setText(P_intake_value)