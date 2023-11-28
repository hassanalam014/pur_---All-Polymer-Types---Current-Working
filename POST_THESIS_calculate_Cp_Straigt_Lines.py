from __future__ import division
import os,sys,math,matplotlib.pyplot as plt,numpy as npy
from lmfit import minimize, Parameters, report_fit
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from loadPhysicalConstants import *
from scipy.optimize import bisect,fsolve
from scipy.interpolate import interp1d
from sympy import *
from optimizeResidualFunctions import pureEOSResidual
from loadSpecificHeatExperimentalData import *
from Parameters_of_Different_Polymers import *
from POST_THESIS_A_and_B_of_Cp_line_without_Kier_Base import*

def specificHeat(T,**kwargs):     #Cp/mass  and **kwargs must contain "three" characteristic parameters and "three" flexibility parameters.
	
	for key,value in kwargs.items():
		exec "%s=%s" % (key,value)
	
	C_line=A+B*T

	return C_line

def specificHeatResidualArray(params,C,T,fit_type):
	
	A = params['A'].value
	B = params['B'].value

	kwargs = {'A':A,'B':B}

	residual=npy.zeros(len(C))

	for j in range(0,len(C)):
		C_line = specificHeat(T[j],**kwargs)
		residual[j] = (C[j]-C_line)

	return residual

Program_Running_For=['PVME Reference-NON 60kilo']		#02kilo_POST_THESIS

Pick_List_Element = Program_Running_For[0]
Divide_List_Picked_Element = Pick_List_Element.split()

print(Divide_List_Picked_Element)

Polymer_Type=Divide_List_Picked_Element[0]
Reference=Divide_List_Picked_Element[1]
Polymer_Weight=Divide_List_Picked_Element[2]
# class Polymer_Type

kwargs = {'Polymer_Type':Polymer_Type,'Reference':Reference,'Polymer_Weight':Polymer_Weight}

Abelow,Bbelow,Aabove,Babove,A,B,deltaCp,T0_excluding_Tg,M0_excluding_Tg,C0_excluding_Tg,P0_excluding_Tg,I0_excluding_Tg,Tg0_excluding_Tg,T0_above_Tg,M0_above_Tg,C0_above_Tg,P0_above_Tg,I0_above_Tg,Tg0_above_Tg,T0_at_Tg,M0_at_Tg,C0_at_Tg,P0_at_Tg,I0_at_Tg,Tg0_at_Tg,T0_below_Tg,M0_below_Tg,C0_below_Tg,P0_below_Tg,I0_below_Tg,Tg0_below_Tg,T0_complete_Tg,M0_complete_Tg,C0_complete_Tg,P0_complete_Tg,I0_complete_Tg,Tg0_complete_Tg=loadSpecificHeatExperimentalData(**kwargs)
Abelow,Bbelow,Aabove,Babove,deltaCp,Tg_used_for_deltaCp = load_A_and_B_of_Cp_line_without_Kier_Base(**kwargs)

print T0_below_Tg
print 'Fitting Below Tg'

#Fitting Data to the base curve below glass transition:
params_below_Tg = Parameters()
#The following code sets up the model's parameters. It includes both fitting parameters and parameters that will remain fixed
#for the fitting. The values given are the inital guesses of fitting parameters and values of fixed parameters.
#						(Name,			Value,		        Vary?,	Min,	Max,	Expr)
params_below_Tg.add_many(('A',			0.00,			    True,	None,	None,	None),
				(		'B',			0.0027,				True,	None,	None,	None))

#Running the Levenberg-Marquart algorithm on the residuals in order to do least squares fitting. This will return the fitted value of the RESIDUALS.
#These need to be added to the experimental datapints to find the fitted specific heat.
fit = minimize(specificHeatResidualArray,params_below_Tg,args=(C0_below_Tg,T0_below_Tg,'C_below_Tg'))

#Reporting the values of the parameters. NEED TO FIGURE OUT HOW TO PRINT THIS TO FILE.
report_fit(fit.params)

if 'A' in fit.params and 'B' in fit.params:
	Abelow = fit.params['A'].value
	Bbelow = fit.params['B'].value
	#kwargs = {'A':AIterated,'B':BIterated}

print 'Abelow is: ', Abelow
print 'Bbelow is: ', Bbelow

print T0_above_Tg
print 'Fitting Above Tg'

#Fitting Data to the base curve above glass transition:
params_above_Tg = Parameters()
#The following code sets up the model's parameters. It includes both fitting parameters and parameters that will remain fixed
#for the fitting. The values given are the inital guesses of fitting parameters and values of fixed parameters.
#						(Name,			Value,		        Vary?,	Min,	Max,	Expr)
params_above_Tg.add_many(('A',			-2.53,			    True,	None,	None,	None),
				(		'B',			0.009392431,		True,	None,	None,	None))

#Running the Levenberg-Marquart algorithm on the residuals in order to do least squares fitting. This will return the fitted value of the RESIDUALS.
#These need to be added to the experimental datapints to find the fitted specific heat.
fit = minimize(specificHeatResidualArray,params_above_Tg,args=(C0_above_Tg,T0_above_Tg,'C_above_Tg'))

#Reporting the values of the parameters. NEED TO FIGURE OUT HOW TO PRINT THIS TO FILE.
report_fit(fit.params)

if 'A' in fit.params and 'B' in fit.params:
	Aabove = fit.params['A'].value
	Babove = fit.params['B'].value
	#kwargs = {'A':AIterated,'B':BIterated}

print 'Aabove=',Aabove
print 'Babove=',Babove

#Initializing the array of densities.
T0 = npy.linspace(100,600,100)

C_line_below=npy.zeros(len(T0))
C_line_above=npy.zeros(len(T0))

#To Calculate Delta Cp at Tg:
for i in range(0,len(T0)):
	C_line_below[i] = Abelow+Bbelow*T0[i]
	C_line_above[i] = Aabove+Babove*T0[i]

deltaCp=(Aabove-Abelow)+(Babove-Bbelow)*Tg_used_for_deltaCp

print 'Thus, results are:'
print '#Equation of Delta Cp is:'
print '#deltaCp=',(Aabove-Abelow),'+',(Babove-Bbelow),'*Tg_atm'
print 'Abelow=',Abelow
print 'Bbelow=',Bbelow
print 'Aabove=',Aabove
print 'Babove=',Babove
print 'deltaCp=',deltaCp

#######################################################################################

#######################################################################################

#Setting font size
axis_size = 20
title_size = 20
size = 14
label_size = 20
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

#General line properties.
linewidth = 1
markersize = 1

arrow_ls = 'dashdot'
show_arrows = True

#==================================================================================
#P versus R plots.
figPUREPS=plt.figure(num=None, figsize=(10,6), dpi=None, facecolor='w', edgecolor='k')
ax = plt.axes()

plt.axvline(x=Tg_used_for_deltaCp,lw=0.5,color='k', linestyle='-.')

plt.plot(T0,C_line_below,color='r',lw=linewidth,ls=':',label='C_A+BT below')
plt.plot(T0,C_line_above,color='b',lw=linewidth,ls=':',label='C_A+BT above')

plt.plot(T0_complete_Tg,C0_complete_Tg,'sk',ms=markersize)

plt.xlabel('Temperature T (K)',fontsize=axis_size)
plt.ylabel(r'Specific Heat $c_P$ ($J/g.K$)',fontsize=axis_size)
# plt.axis([250,450,1.00,2.25])
plt.legend(loc=4,fontsize=size,numpoints=1)
plt.subplots_adjust(bottom=0.3)
plt.show()
