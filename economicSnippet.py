#-----------------------------------------
# Numpy Library :
#-----------------------------------------
import numpy as np
import math as mt

#-----------------------------------------
# Producer Price Index
#-----------------------------------------
numberOfMonth = 24
ppiMonthly    = np.zeros(numberOfMonth)
adequatePay   = 4500
rentalFee     = 1600
rentalFeeSum  = 0
juralInterest = 1.09

# ppi : 22.04 - 22.12
ppiMonthly[ 0] = 7.67/100  # 22.04
ppiMonthly[ 1] = 8.76/100  # 22.05
ppiMonthly[ 2] = 6.77/100  # 22.06
ppiMonthly[ 3] = 5.17/100  # 22.07
ppiMonthly[ 4] = 2.41/100  # 22.08
ppiMonthly[ 5] = 4.78/100  # 22.09
ppiMonthly[ 6] = 7.83/100  # 22.10
ppiMonthly[ 7] = 0.74/100  # 22.11
ppiMonthly[ 8] = -0.24/100 # 22.12

# ppi : 23.01 - 23.12
ppiMonthly[ 9] = 4.15/100  # 23.01
ppiMonthly[10] = 1.56/100  # 23.02
ppiMonthly[11] = 0.44/100  # 23.03
ppiMonthly[12] = 0.81/100  # 23.04
ppiMonthly[13] = 0.65/100  # 23.05
ppiMonthly[14] = 6.50/100  # 23.06
ppiMonthly[15] = 8.23/100  # 23.07
ppiMonthly[16] = 5.89/100  # 23.08
ppiMonthly[17] = 3.40/100  # 23.09
ppiMonthly[18] = 1.94/100  # 23.10
ppiMonthly[19] = 2.81/100  # 23.11
ppiMonthly[20] = 1.14/100  # 23.12

# ppi : 24.01 - 24.02
ppiMonthly[21] = 4.14/100  # 24.01
ppiMonthly[22] = 3.74/100  # 24.02

adequatePay_updated = np.zeros(len(ppiMonthly)+1)
adequatePay_updated[0] = adequatePay

# update adequate fee monthly
for i in range(len(ppiMonthly)):
    adequatePay_updated[i+1] = adequatePay_updated[i]*(1+ppiMonthly[i])

# calculate rental fee monthly, then sum all
for i in range(len(adequatePay_updated)):
    if i<3:    #22.04 - 22.06
        rentalFee = 1600
    
    elif i<14: #22.07 - 23.06
        rentalFee = 2500

    elif i<25: #23.07 - 24.06
        rentalFee = 6300

    rentalFeeSum = rentalFeeSum + rentalFee


print("\n\n---------------------------------------------------------------------------------------") 
print( "Adequate Pay is              : " + str( int( adequatePay_updated.sum() ) ) + " TL" )
print( "Rental Fee is                : " + str( int( rentalFeeSum ) ) + " TL" )

TotalIndemnity = int( adequatePay_updated.sum() ) + int( rentalFeeSum ) 
print( "Total Indemnity is           : " + str(TotalIndemnity) + " TL" )

InterestofDefault = TotalIndemnity*( mt.pow( juralInterest, np.floor( len(adequatePay_updated)/12 ) ) )


print( "Interest of Default included : " + str(int(InterestofDefault)) + " TL" )
print("---------------------------------------------------------------------------------------\n") 

#---------------------------------------------------------------------------------------
# Adequate Pay is              : 191,644 TL
# Rental Fee is                : 101,600 TL
# Total Indemnity is           : 293,244 TL
# Interest of Default included : 348,403 TL
#---------------------------------------------------------------------------------------
