from ipywidgets import interact, interactive, fixed, interact_manual, Layout, SelectMultiple
import ipywidgets as widgets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
from IPython.display import display
from datetime import datetime as dt
import ipydatetime
import time
import matplotlib.ticker as mticker
import matplotlib
import warnings
import matplotlib.dates as matdates
from matplotlib.dates import HOURLY, MINUTELY, SECONDLY, rrulewrapper, AutoDateLocator
warnings.filterwarnings('ignore')



df = pd.read_csv('Lipo.Master.Data.csv')

df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y %H:%M:%S.%f')




start_date_widget = widgets.DatePicker(
    description='Start Date',
    disabled=False)


end_date_widget = widgets.DatePicker(
    description='End Date',
    disabled=False
)

opts = ['-Select Data-','Speed', 'Altitude', 'ir', 'luminosity', 'pm1s', 'pm25s', 'pm10s', 'pm1e', 'pm25e', 'pm10e', 'a03um01Lair', 'a05um01Lair', 'a1um01Lair', 'a25um01Lair', 'a5um01Lair', 'a10um01Lair', 'Co2', 'Temp', 'Hum', 'uv', 'ROH', 'NH4']
sensor_data_widget = widgets.Select(
    options=opts,
    description='Sensor Data:',
    disabled=False,
    rows=3
    )

speed_widget = widgets.FloatRangeSlider(
    value=[-1.0, 3.0],
    min=-1.0,
    max=3.0,
    step=0.01,
    description='Speed:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)

Altitude_widget = widgets.FloatRangeSlider(
    value=[-250, 150],
    min=-250,
    max=150.0,
    step=0.1,
    description='Altitude:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

ir_widget = widgets.FloatRangeSlider(
    value=[-1.0, 10000.0],
    min=-1.0,
    max=10000.0,
    step=1.0,
    description='IR:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

luminosity_widget = widgets.FloatRangeSlider(
    value=[-1.0, 50000],
    min=-1.0,
    max=50000,
    step=0.01,
    description='Luminosity:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.5f',
)

pm1s_widget = widgets.FloatRangeSlider(
    value=[-1.0, 400.0],
    min=-1.0,
    max=400.0,
    step=1.0,
    description='PM1s:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

pm25s_widget = widgets.FloatRangeSlider(
    value=[-1.0, 600.0],
    min=-1.0,
    max=600.0,
    step=1.0,
    description='PM2.5s:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

pm10s_widget = widgets.FloatRangeSlider(
    value=[-1.0, 600.0],
    min=-1.0,
    max=600.0,
    step=1.0,
    description='PM10s:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

pm1e_widget = widgets.FloatRangeSlider(
    value=[-1.0, 300.0],
    min=-1.0,
    max=300.0,
    step=1.0,
    description='PM1e:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

pm25e_widget = widgets.FloatRangeSlider(
    value=[-1.0, 350.0],
    min=-1.0,
    max=350.0,
    step=1.0,
    description='PM2.5e:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

pm10e_widget = widgets.FloatRangeSlider(
    value=[-1.0, 400.0],
    min=-1.0,
    max=400.0,
    step=1.0,
    description='PM10e:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a03um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 53000.0],
    min=-1.0,
    max=53000.0,
    step=1.0,
    description='03um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a05um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 60000.0],
    min=-1.0,
    max=60000.0,
    step=1.0,
    description='05um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a1um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 61000.0],
    min=-1.0,
    max=61000.0,
    step=1.0,
    description='1um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a25um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 42000.0],
    min=-1.0,
    max=42000.0,
    step=0.01,
    description='25um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a5um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 20000.0],
    min=-1.0,
    max=20000.0,
    step=1.0,
    description='5um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

a10um01Lair_widget = widgets.FloatRangeSlider(
    value=[-1.0, 10000.0],
    min=-1.0,
    max=10000.0,
    step=1.0,
    description='10um01Lair:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

Co2_widget = widgets.FloatRangeSlider(
    value=[-1.0, 10000.0],
    min=-1.0,
    max=10000.0,
    step=1.0,
    description='CO2:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

Temp_widget = widgets.FloatRangeSlider(
    value=[-1.0, 70.0],
    min=-1.0,
    max=70.0,
    step=1.0,
    description='Temperature:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

Hum_widget = widgets.FloatRangeSlider(
    value=[-1.0, 100.0],
    min=-1.0,
    max=100.0,
    step=1.0,
    description='Humidity:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

uv_widget = widgets.FloatRangeSlider(
    value=[-0.1, 1.0],
    min=-0.1,
    max=1.0,
    step=0.01,
    description='UV:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f',
)

roh_widget = widgets.FloatRangeSlider(
    value=[-1.0, 100.0],
    min=-1.0,
    max=100.0,
    step=1.0,
    description='Alcohol:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

nh4_widget = widgets.FloatRangeSlider(
    value=[-1.0, 100.0],
    min=-1.0,
    max=100.0,
    step=1.0,
    description='Nitrate:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)





def change_parameters(start, end, speed, altitude, ir, luminosity, pm1s, pm25s, pm10s, pm1e, pm25e, pm10e, a03um01lair, a05um01lair, a1um01lair, a25um01lair, a5um01lair, a10um01lair, co2, temp, hum, uv, roh, nh4):
    #start_date = pd.to_datetime('2016-01-01')
    #end_date = pd.to_datetime('2018-12-31')
    
    #if check_date(start):
    #    start_date = pd.to_datetime(start)
    #if check_date(end):
    #    end_date = pd.to_datetime(end)

    #print("Start date set to: " + str(start_date))
    #print("End date set to: " + str(end_date))
    
    speedlow = speed[0]
    speedhigh = speed[1]
    
    altitudelow = altitude[0]
    altitudehigh = altitude[1]
    
    irlow = ir[0]
    irhigh = ir[1]
 
    luminositylow = luminosity[0]
    luminosityhigh = luminosity[1]
 
    pm1slow = pm1s[0]
    pm1shigh = pm1s[1]
 
    pm25slow = pm25s[0]
    pm25shigh = pm25s[1]
 
    pm10slow = pm10s[0]
    pm10shigh = pm10s[1]
 
    pm1elow = pm1e[0]
    pm1ehigh = pm1e[1]
 
    pm25elow = pm25e[0]
    pm25ehigh = pm25e[1]
 
    pm10elow = pm10e[0]
    pm10ehigh = pm10e[1]
 
    a03um01lairlow = a03um01lair[0]
    a03um01lairhigh = a03um01lair[1]
 
    a05um01lairlow = a05um01lair[0]
    a05um01lairhigh = a05um01lair[1]
 
    a1um01lairlow = a1um01lair[0]
    a1um01lairhigh = a1um01lair[1]
 
    a25um01lairlow = a25um01lair[0]
    a25um01lairhigh = a25um01lair[1]
 
    a5um01lairlow = a5um01lair[0]
    a5um01lairhigh = a5um01lair[1]
 
    a10um01lairlow = a10um01lair[0]
    a10um01lairhigh = a10um01lair[1]
 
    co2low = co2[0]
    co2high = co2[1]
 
    templow = temp[0]
    temphigh = temp[1]
 
    humlow = hum[0]
    humhigh = hum[1]
     
    uvlow = uv[0]
    uvhigh = uv[1]
     
    rohlow = roh[0]
    rohhigh = roh[1]
     
    nh4low = nh4[0]
    nh4high = nh4[1]
 
    
 
 
    df_date_update = df.loc[(start <= df['Date'].dt.date) & (end >= df['Date'].dt.date)]
    df_speed_update = df_date_update[df_date_update.Speed.between(speedlow,speedhigh)]
    df_altitude_update = df_speed_update[df_speed_update.Altitude.between(altitudelow,altitudehigh)]
    df_ir_update = df_altitude_update[df_altitude_update.ir.between(irlow,irhigh)]
    df_luminosity_update = df_ir_update[df_ir_update.luminosity.between(luminositylow,luminosityhigh)]
    df_pm1s_update = df_luminosity_update[df_luminosity_update.pm1s.between(pm1slow,pm1shigh)]
    df_pm25s_update = df_pm1s_update[df_pm1s_update.pm25s.between(pm25slow,pm25shigh)]
    df_pm10s_update = df_pm25s_update[df_pm25s_update.pm10s.between(pm10slow,pm10shigh)]
    df_pm1e_update = df_pm10s_update[df_pm10s_update.pm1e.between(pm1elow,pm1ehigh)]  
    df_pm25e_update = df_pm1e_update[df_pm1e_update.pm25e.between(pm25elow,pm25ehigh)]
    df_pm10e_update = df_pm25e_update[df_pm25e_update.pm10e.between(pm10elow,pm10ehigh)] 
    df_a03um01lair_update = df_pm10e_update[df_pm10e_update.a03um01Lair.between(a03um01lairlow,a03um01lairhigh)]
    df_a05um01lair_update = df_a03um01lair_update[df_a03um01lair_update.a05um01Lair.between(a05um01lairlow,a05um01lairhigh)]
    df_a1um01lair_update = df_a05um01lair_update[df_a05um01lair_update.a1um01Lair.between(a1um01lairlow,a1um01lairhigh)]
    df_a25um01lair_update = df_a1um01lair_update[df_a1um01lair_update.a25um01Lair.between(a25um01lairlow,a25um01lairhigh)]
    df_a5um01lair_update = df_a25um01lair_update[df_a25um01lair_update.a10um01Lair.between(a5um01lairlow,a5um01lairhigh)]
    df_a10um01lair_update = df_a5um01lair_update[df_a5um01lair_update.a10um01Lair.between(a10um01lairlow,a10um01lairhigh)]
    df_co2_update = df_a10um01lair_update[df_a10um01lair_update.Co2.between(co2low,co2high)]
    df_temp_update = df_co2_update[df_co2_update.Temp.between(templow,temphigh)]
    df_hum_update = df_temp_update[df_temp_update.Hum.between(humlow,humhigh)]
    df_uv_update = df_hum_update[df_hum_update.uv.between(uvlow,uvhigh)]
    df_roh_update = df_uv_update[df_uv_update.ROH.between(rohlow,rohhigh)]
    df_nh4_update = df_roh_update[df_roh_update.NH4.between(nh4low,nh4high)]
    df_nh4_update.to_csv("updatedData.csv")
    
    
    
    

    
    
    DATE = df_nh4_update.Date
    DATE.to_csv("DATE.csv")
    #TIME = df_nh4_update.Time
    #TIME.to_csv("TIME.csv")
    SPEED = df_nh4_update.Speed
    SPEED.to_csv("SPEED.csv")
    ALTITUDE = df_nh4_update.Altitude
    ALTITUDE.to_csv("ALTITUDE.csv")
    IR = df_nh4_update.ir
    IR.to_csv("IR.csv")
    LUMINOSITY = df_nh4_update.luminosity
    LUMINOSITY.to_csv("LUMINOSITY.csv")
    PM1S = df_nh4_update.pm1s
    PM1S.to_csv("PM1S.csv")
    PM25S = df_nh4_update.pm25s
    PM25S.to_csv("PM25S.csv")
    PM10S = df_nh4_update.pm10s
    PM10S.to_csv("PM10S.csv")
    PM1E = df_nh4_update.pm1e
    PM1E.to_csv("PM1E.csv")
    PM25E = df_nh4_update.pm25e
    PM25E.to_csv("PM25E.csv")
    PM10E = df_nh4_update.pm10e
    PM10E.to_csv("PM10E.csv")
    A03UM01LAIR = df_nh4_update.a03um01Lair
    A03UM01LAIR.to_csv("A03UM01LAIR.csv")
    A05UM01LAIR = df_nh4_update.a05um01Lair
    A05UM01LAIR.to_csv("A05UM01LAIR.csv")
    A1UM01LAIR = df_nh4_update.a1um01Lair
    A1UM01LAIR.to_csv("A1UM01LAIR.csv")
    A25UM01LAIR = df_nh4_update.a25um01Lair
    A25UM01LAIR.to_csv("A25UM01LAIR.csv")
    A5UM01LAIR = df_nh4_update.a5um01Lair
    A5UM01LAIR.to_csv("A5UM01LAIR.csv")
    A10UM01LAIR = df_nh4_update.a10um01Lair
    A10UM01LAIR.to_csv("A10UM01LAIR.csv")
    CO2 = df_nh4_update.Co2
    CO2.to_csv("CO2.csv")
    TEMP = df_nh4_update.Temp
    TEMP.to_csv("TEMP.csv")
    HUM = df_nh4_update.Hum
    HUM.to_csv("HUM.csv")
    UV = df_nh4_update.uv
    UV.to_csv("UV.csv")
    ROH = df_nh4_update.ROH
    ROH.to_csv("ROH.csv")
    NH4 = df_nh4_update.NH4
    NH4.to_csv("NH4.csv")
    
    display(df_nh4_update)
    
    

        
    
out = widgets.interactive_output(
        change_parameters, 
          {'start': start_date_widget, 
           'end': end_date_widget,
           'speed': speed_widget,
           'altitude': Altitude_widget,
           'ir': ir_widget,
           'luminosity': luminosity_widget,
           'pm1s': pm1s_widget,
           'pm25s': pm25s_widget,
           'pm10s': pm10s_widget,
           'pm1e': pm1e_widget,
           'pm25e': pm25e_widget,
           'pm10e': pm10e_widget,
           'a03um01lair': a03um01Lair_widget,
           'a05um01lair': a05um01Lair_widget,
           'a1um01lair': a1um01Lair_widget,
           'a25um01lair': a25um01Lair_widget,
           'a5um01lair': a5um01Lair_widget,
           'a10um01lair': a10um01Lair_widget,
           'co2': Co2_widget,
           'temp': Temp_widget,
           'hum': Hum_widget,
           'uv': uv_widget,
           'roh': roh_widget,
           'nh4': nh4_widget,
           #'sensor_data': sensor_data_widget
          }
      )
ui = widgets.HBox(
        [widgets.VBox(
          [widgets.Label("Please Select Date Range and Sensor Data to Graph" ), start_date_widget, end_date_widget]),
         speed_widget,
         Altitude_widget,
         ir_widget,
         luminosity_widget,
         pm1s_widget,
         pm25s_widget,
         pm10s_widget,
         pm1e_widget,
         pm25e_widget,
         pm10e_widget,
         a03um01Lair_widget,
         a05um01Lair_widget,
         a1um01Lair_widget,
         a25um01Lair_widget,
         a5um01Lair_widget,
         a10um01Lair_widget,
         Co2_widget,
         Temp_widget,
         Hum_widget,
         uv_widget,
         roh_widget,
         nh4_widget,
         #sensor_data_widget
        ], 
        layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
    )
         

def plot(sensordata):

    if sensor_data_widget.value == 'Speed':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        SPEED = updatedData["Speed"]

        figspeed, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figspeed.subplots_adjust(hspace=0)

        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 
        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, SPEED, 'tab:blue', label = 'SPEED')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)


          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figspeed.show()
        #plt.savefig('speed.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('speed.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='Altitude':   

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        ALTITUDE = updatedData["Altitude"]

        figaltitude, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figaltitude.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        ax2.set_xlabel('$Date$', fontsize=24)
        #ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, ALTITUDE, 'tab:blue', label = 'ALTITUDE')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)


          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figaltitude.show()
        #plt.savefig('altitude.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('altitude.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='ir':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        IR = updatedData["ir"]

        figir, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figir.subplots_adjust(hspace=0)

        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 
        
        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, IR, 'tab:blue', label = 'IR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        

          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figir.show()
        #plt.savefig('ir.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('ir.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='luminosity':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        LUMINOSITY = updatedData["luminosity"]

        figluminosity, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figluminosity.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, LUMINOSITY, 'tab:blue', label = 'LUMINOSITY')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
     

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figluminosity.show()
       #plt.savefig('luminosity.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('luminosisty.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='pm1s':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM1S = updatedData["pm1s"]

        figpm1s, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm1s.subplots_adjust(hspace=0)

        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, PM1S, 'tab:blue', label = 'PM1S')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        

          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm1s.show()
        #plt.savefig('pm1s.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm1s.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='pm25s':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM25S = updatedData["pm25s"]      

        figpm25s, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm25s.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME,PM25S , 'tab:blue', label = 'PM25S')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        

          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm25s.show()
        #plt.savefig('pm25s.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm25s.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='pm10s':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM10S = updatedData["pm10s"]

        figpm10s, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm10s.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 


        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, PM10S, 'tab:blue', label = 'PM10S')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm10s.show()
        #plt.savefig('pm10s.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm10s.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='pm1e':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM1E = updatedData["pm1e"]

        figpm1e, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm1e.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, PM1E, 'tab:blue', label = 'PM1E')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
      
       
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm1e.show()
        #plt.savefig('pm1e.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm1e.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='pm25e':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM25E = updatedData["pm25e"]

        figpm25e, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm25e.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, PM25E, 'tab:blue', label = 'PM25E')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm25e.show()
        #plt.savefig('pm25e.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm25e.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='pm10e':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        PM10E = updatedData["pm10e"]

        figpm10e, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figpm10e.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, PM10E, 'tab:blue', label = 'PM10E')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figpm10e.show()
        #plt.savefig('pm10e.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('pm10e.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a03um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A03UM01LAIR = updatedData["a03um01Lair"]

        figa03um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa03um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5) 

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A03UM01LAIR, 'tab:blue', label = 'A03UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa03um01Lair.show()
        #plt.savefig('a03um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a03um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a05um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A05UM01LAIR = updatedData["a05um01Lair"]

        figa05um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa05um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A05UM01LAIR, 'tab:blue', label = 'A05UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa05um01Lair.show()
        #plt.savefig('a05um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a05um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a1um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A1UM01LAIR = updatedData["a1um01Lair"]

        figa1um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa1um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5) 

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A1UM01LAIR, 'tab:blue', label = 'A1UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa1um01Lair.show()
        #plt.savefig('a1um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a1um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a25um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A25UM01LAIR = updatedData["a25um01Lair"]

        figa25um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa25um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5) 

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A25UM01LAIR, 'tab:blue', label = 'A25UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa25um01Lair.show()
        #plt.savefig('a25um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a25um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a5um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A5UM01LAIR = updatedData["a5um01Lair"]

        figa5um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa5um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A5UM01LAIR, 'tab:blue', label = 'A5UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa5um01Lair.show()
        #plt.savefig('a5um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a5um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='a10um01Lair':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        A10UM01LAIR = updatedData["a10um01Lair"]

        figa10um01Lair, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figa10um01Lair.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, A10UM01LAIR, 'tab:blue', label = 'A10UM01LAIR')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figa10um01Lair.show()
        #plt.savefig('a10um01lair.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('a10um01lair.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='Co2':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        CO2 = updatedData["Co2"]

        figCo2, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figCo2.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5) 

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, CO2, 'tab:blue', label = 'CO2')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figCo2.show()
        #plt.savefig('co2.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('co2.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='Temp':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        TEMP = updatedData["Temp"]

        figTemp, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figTemp.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, TEMP, 'tab:blue', label = 'TEMP')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figTemp.show()
        #plt.savefig('temp.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('temp.pdf', bbox_inches='tight', pad_inches=0.01)    

    elif sensor_data_widget.value =='Hum':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        HUM = updatedData["Hum"]

        figHum, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figHum.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, HUM, 'tab:blue', label = 'HUM')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figHum.show()   
        #plt.savefig('hum.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('hum.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='uv':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        UV = updatedData["uv"]

        figUV, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figUV.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, UV, 'tab:blue', label = 'UV')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figUV.show()   
        #plt.savefig('uv.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('uv.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='ROH':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        ROH = updatedData["ROH"]

        figROH, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figROH.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, ROH, 'tab:blue', label = 'Alcohol')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figROH.show()   
        #plt.savefig('ROH.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('ROH.pdf', bbox_inches='tight', pad_inches=0.01)

    elif sensor_data_widget.value =='NH4':

        updatedData = pd.read_csv('updatedData.csv')
        updatedData['Date'] = pd.to_datetime(updatedData['Date'],format='%Y-%m-%d %H:%M:%S.%f')

        TIME = updatedData["Date"]
        LUMINOSITY = updatedData["luminosity"]
        NH4 = updatedData["NH4"]

        figNH4, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(45,15))
        figNH4.subplots_adjust(hspace=0)
        
        seclocator = matdates.SecondLocator(bysecond=[30, 0]) #every 20 secs
        #minlocator = matdates.MinuteLocator(byminute=[5,10,15,20,25,30,35,40,45,50,55])  # range(60) is the default
        minlocator = matdates.MinuteLocator(byminute=range(60)) #every 1 minute
        hourlocator = matdates.HourLocator(byhour=range(24))
    
        majorFmt = matdates.DateFormatter('%Y-%m-%d, %H:%M:%S')  
        minorFmt = matdates.DateFormatter('%H:%M:%S') 

        
        ax1.plot(TIME, LUMINOSITY, label = 'LUX')
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
        ax1.xaxis.set_major_locator(hourlocator)
        ax1.xaxis.set_major_formatter(majorFmt)
        ax1.xaxis.set_minor_locator(seclocator)
        ax1.xaxis.set_minor_formatter(minorFmt)
        ax1.grid(which='major', color='k')
        ax1.grid(which='minor', color='k', linestyle=':', alpha=0.5)

        ax2.set_xlabel('$Date$', fontsize=24)
        ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
        ax2.set_ylabel('$Sensor Data$', fontsize=24)
        ax2.plot(TIME, NH4, 'tab:blue', label = 'Nitrate')
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1), fontsize=12)
        
        
          
          

        ax2.xaxis.set_major_locator(hourlocator)
        ax2.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90)

        ax2.xaxis.set_minor_locator(seclocator)
        ax2.xaxis.set_minor_formatter(minorFmt)
        plt.setp(ax2.xaxis.get_minorticklabels(), rotation=90)
        
        ax2.grid(which='major', color='k')
        ax2.grid(which='minor', color='k', linestyle=':', alpha=0.5)
        figNH4.show()   
        #plt.savefig('NH4.eps', bbox_inches='tight', pad_inches=0.01)
        plt.savefig('NH4.pdf', bbox_inches='tight', pad_inches=0.01)

        
plotout = widgets.interactive_output(
        plot, 
          {'sensordata':sensor_data_widget})

plotui = widgets.HBox(
        [widgets.VBox(
          [widgets.Label("Select Sensor Data to Plot"), sensor_data_widget])], 
        layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
    )
display(ui, out, plotui, plotout)
