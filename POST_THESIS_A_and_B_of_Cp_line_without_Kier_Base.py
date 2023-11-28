from __future__ import division
import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

def load_A_and_B_of_Cp_line_without_Kier_Base(**kwargs):
	
	for key,value in kwargs.items():
		exec "%s='%s'" % (key,value)
	
	print 'Polymer Type', Polymer_Type, 'Polymer Weight', Polymer_Weight

	############################################################################
	# ONLY STRAIGHT LINES (A and B) CALCULATION WITHOUT KIER'S FORMULA HELPFUL TO CALCULATE Delta Cp at Different Tg's:
	############################################################################
	
	if Polymer_Type=='PC' and Polymer_Weight=='02kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.4806991438799261 - 0.0006378878796372196*Tg_atm
		Abelow= 0.25900679788850695
		Bbelow= 0.003196569890141667
		Aabove= 0.7397059417684331
		Babove= 0.0025586820105044476
		deltaCp= 0.21214834655265669		#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 421.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PC' and Polymer_Weight=='03kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.9655046611534179 - 0.0018484783319076712*Tg_atm
		Abelow= -0.3159229538066474
		Bbelow= 0.004596563004807655
		Aabove= 0.6495817073467705
		Babove= 0.0027480846728999836
		deltaCp= 0.19838615341173438		#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 415.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PMMA' and Polymer_Weight=='01kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.7920162408290767 - 0.0012033072973456583*Tg_atm
		Abelow= -0.6158762508459666
		Bbelow= 0.006402219137423645
		Aabove= 0.17613998998311012
		Babove= 0.005198911840077987
		deltaCp= 0.3371660824324179			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 378.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PMMA' and Polymer_Weight=='02kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.8999106169499997 - 0.001526763002051977*Tg_atm
		Abelow= 0.22183352015771882
		Bbelow= 0.00374834053064095
		Aabove= 1.1217441371077186
		Babove= 0.002221577528588973
		deltaCp= 0.29531246813741685		#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 396.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PMMA' and Polymer_Weight=='03kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.6488329070895775 - 0.0009228939860067621*Tg_atm
		Abelow= -0.013551753925140917
		Bbelow= 0.004386033561635083
		Aabove= 0.6352811531644366
		Babove= 0.003463139575628321
		deltaCp= 0.29536451044898765		#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 383.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PMMA' and Polymer_Weight=='04kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.7275508190380102 - 0.000711941005454199*Tg_atm
		Abelow= 0.4874704542205815
		Bbelow= 0.0028952826201188216
		Aabove= 1.2150212732585917
		Babove= 0.0021833416146646227
		deltaCp= 0.494034169249033			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 328.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PS' and Polymer_Weight=='00kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 1.1582598442822138 - 0.002269757152512417*Tg_atm
		Abelow= -0.23352854384542343
		Bbelow= 0.0047924933842159985
		Aabove= 0.9247313004367904
		Babove= 0.0025227362317035815
		deltaCp= 0.31164042639508227		#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 373.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PS' and Polymer_Weight=='01kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.897125376074815 - 0.0016526153631936519*Tg_atm
		Abelow= -0.14411538483169364
		Bbelow= 0.004524615385336415
		Aabove= 0.7530099912431214
		Babove= 0.002872000022142763
		deltaCp= 0.2840050763299702			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 371.0			#Tg given in Cp-papers or self-supposed

	if Polymer_Type=='PS' and Polymer_Weight=='02kilo_POST_THESIS':
		#Equation of Delta Cp is:
		#deltaCp= 0.6123791304754777 - 0.000889288520929247*Tg_atm
		Abelow= -0.08013798898470745
		Bbelow= 0.004269871140462965
		Aabove= 0.5322411414907702
		Babove= 0.0033805826195337178
		deltaCp= 0.2806745121688685			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 373.0			#Tg given in Cp-papers or self-supposed by seeing Cp(T) plot

	if Polymer_Type=='PVAc' and Polymer_Weight=='189kilo':
		#Equation of Delta Cp is:
		#deltaCp= 1.6450131300256265 + -0.003793594561464537 *Tg_atm
		Abelow= -0.5145999999999977
		Bbelow= 0.006049999999999992
		Aabove= 1.1304131300256288
		Babove= 0.002256405438535455
		deltaCp= 0.4652052214101554			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 311.0			#Tg given in Cp-papers or self-supposed by seeing Cp(T) plot

	if Polymer_Type=='PVME' and Polymer_Weight=='60kilo':
		#Equation of Delta Cp is:
		#deltaCp= 0.9945729727373542 + -0.0018453480908539716 *Tg_atm
		Abelow= 0.2515113248389642
		Bbelow= 0.004186753905707678
		Aabove= 1.2460842975763184
		Babove= 0.002341405814853706
		deltaCp= 0.5369266462055693			#This deltaCp is at Tg given in Cp-papers (Not in PVT-paper). I think this Tg is much better that PVT-paper Tg to calculate actual deltaCp.
		Tg_used_for_deltaCp = 248.0			#Tg given in Cp-papers or self-supposed by seeing Cp(T) plot

	return Abelow,Bbelow,Aabove,Babove,deltaCp,Tg_used_for_deltaCp
