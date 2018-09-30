import pyautogui as pgu
import sys
from time import sleep
import win32gui

'''
#import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pgu.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:


    print('\n')
#-----------------STEPS
'''
'''
1) GO TO 154,269 
2) RIGHT CLICK
3) Shift + C
4) Go to 1180,727
5) click
'''
'''
Goto 1154,579//For 60 days
Goto 1055,443//For 1 day
Goto 1057,539//For 15 days
Goto 1157,535//For 30 days

6)Ok button 1178,724

go to freq division (108,232)
go to day division (215,232)
go to Chart type   (310,232)
go to Study        (431,232)
go to Tools        (519,235)
7)Right click on chart (322,587)
8)go to 335,346 click
9)click(750,459)
10) CLose excel file click(1597,218)
11) Click(76,155)
12) Press delete
13) click(548,157)

'''

        #repeat


#-----------------------------------Real code



for i in range(1,50):

    pgu.click(195,130)
    pgu.click(120,230)#Script select
    pgu.hotkey('shift','c')#Chart Option Generation
    pgu.click(1050,443)#Chart Generation /// Selection of days
    pgu.click(1150,700)#Click ok
    sleep(5)
    pgu.moveTo(195,359) #move to chart env
    pgu.click(button='right', clicks=1) # Right click 
    pgu.click(300,652)# Choose the option Save chart
    pgu.click(550,750)# Save chart to excel

    window = win32gui.GetWindowText(win32gui.GetForegroundWindow())# Wait for the excel popup
    x=window.find('xcel')
    while(x==-1):#While not detected then do following
        sleep(5)
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())# Check again
        x=window.find('xcel')# Check again
        
        if(x!=-1):#When detected
            print('Excel file active........')
            break

    sleep(2)
    pgu.click(1880,20)# Close the excel file
    sleep(2)
#i = int(input("enter i"))    
    for x in range(430,690,5):  
        pgu.click(x,130)
        pgu.click(x,125)
        pgu.click(x,135) 
        
    #pgu.click(234,156)
    pgu.click(195,130)
    pgu.click(120,230)#Script select
    pgu.press('delete')
    