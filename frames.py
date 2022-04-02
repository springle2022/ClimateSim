from curses.ascii import isdigit
from tkinter import Misc, StringVar, Tk,Canvas,Label, Frame, Button,Text,Entry
import random
import time
from turtle import bgcolor, color
import os

try:
    import trendline
    import gui
    #import image_handler
except:
    from library_files import trendline
    from library_files import gui
    #from lib import image_handler

path_to_here = os.path.dirname(__file__)

path_to_here = path_to_here[0:1-len("\library_files")]


gui = gui.interface()

class global_monitering():
    
    YEAR = 2019 #Time, in years.

    #CO2_LEVELS = 416.0 #Carbon Dioxide Levels, Parts Per Million, source https://climate.nasa.gov/vital-signs/carbon-dioxide/
    
    year, levels = trendline.get_data(path_to_here + "\data\Carbon_Dioxide_Post_Industrial.txt")
    CO2_LEVELS = round(levels[len(levels)-1],1)
    #print(CO2_LEVELS)

    TORNADO_COUNT = 1517 #NOAA National Centers for Environmental Information, State of the Climate: Tornadoes for Annual 2020, published online January 2021, retrieved on July 26, 2021 from https://www.ncdc.noaa.gov/sotc/tornadoes/202013.
    

    #CYCLONE_COUNT = 18 #NOAA National Centers for Environmental Information, State of the Climate: Tropical Cyclones for Annual 2019, published online January 2020, retrieved on July 26, 2021 from https://www.ncdc.noaa.gov/sotc/tropical-cyclones/201913.
    
    #HIGH_TEMP_COUNT = 
    #LOW_TEMP_COUNT = 
    EXTREME_EVENTS_COUNT = TORNADO_COUNT #+ CYCLONE_COUNT #+ HIGH_TEMP_COUNT #+ LOW_TEMP_COUNT
    TORNADO_CHANGE, TORNADO_CHANGE_K = trendline.get_trend_v2(path_to_here + "data\Tornadoes.txt","exponential",0.9791,YEAR)
    '''H2O_LEVELS = 0 #Water Vapor Levels, Parts Per Million
    N2O_LEVELS = 0 #Nitrous Oxide Levels, Parts Per Million
    CH4_LEVELS = 0 #Methane Levels, Parts Per Million'''
    
    CO2_EMMISIONS = 2.3 #Carbon Dioxide Emmisions, Parts Per Million, source https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide
    CO2_CHANGE, CO2_CHANGE_K = trendline.get_trend_v2(path_to_here + "data\Carbon_Dioxide_Post_Industrial.txt","exponential",1.02,YEAR)
    
    '''H2O_EMMISIONS = 1 #Water Vapor Emmisions, Parts Per Million
    N2O_EMMISIONS = 1 #Nitrous Oxide Emmisions, Parts Per Million
    CH4_EMMISIONS = 1 #Methane Emmisions, Parts Per Million'''

    pH = 8.1 #Current Oceanic pH level, source: https://www.epa.gov/ocean-acidification/understanding-science-ocean-and-coastal-acidification   
    START_pH = pH
    pH_CHANGE = 0.00375 # 0.3/80; predicted change, source https://ocean.si.edu/ocean-life/invertebrates/ocean-acidification 

    GLOBAL_SEA_LEVEL = 9.5  #Global Mean Sea Level, in millimeters, source: https://www.climate.gov/news-features/understanding-climate/climate-change-global-sea-level  
    year, sealevels = trendline.get_data(path_to_here + "\data\Sea_Levels.txt")
    GLOBAL_SEA_LEVEL = round(sealevels[len(sealevels)-1],1)

    SEA_LEVEL_CHANGE, LEVEL_CHANGE_K = trendline.get_trend_v2(path_to_here + "data\Sea_Levels.txt","exponential",1.00825,YEAR)

    #LEVEL_CHANGE = 3.6

    GLOBAL_TEMP = 1.02 #Global Temperature Anomally, in degrees celcius, source: https://climate.nasa.gov/vital-signs/global-temperature/ 
    year, globaltemp = trendline.get_data(path_to_here + "\data\Temperature.txt")
    GLOBAL_TEMP = round(globaltemp[len(globaltemp)-1],2)

    #TEMP_CHANGE = trendline.get_trend(path_to_here + "data\Temperature.txt")
    TEMP_CHANGE, TEMP_CHANGE_K = trendline.get_trend_v2(path_to_here + "data\Temperature.txt","exponential",1.025,YEAR)

    '''print("CO2 (795,149 BCE - 1955 CE; Ice Cores): " + str(trendline.get_trend("data\Carbon_Dioxide_Pre_Industrial.txt")))
    print("CO2 (1959 CE - 2015 CE; Direct): " + str(trendline.get_trend("data\Carbon_Dioxide_Post_Industrial.txt")))'''

    OCEAN_TEMP = 0.76

    '''IMAGE_DROUGHT = image_handler.load_image("2016.17.9_Polychroniou_orig.png")
    IMAGE_EXTREME_EVENT = image_handler.load_image("extreme_event.png")
    IMAGE_CORAL_REEF = image_handler.load_image("coral_reef.png")
    IMAGE_FLOOD = image_handler.load_image("flood.png")'''

    def create(self,root):
        main = gui.new_frame(root,0,0,"NEWS")
        label = Label(main,text="These are some factors that show effects from Climate Change").grid(row=0,column=0,sticky="NEWS",columnspan=99)
        return main

    
    global year_entry
    year_entry = StringVar(value="2019")

    def year_change(*args):
        print(year_entry.get())

    year_entry.trace_add("write", year_change)


    def start(self,root):

        start_year = 2019
        year_entry.initialize(start_year)
        start_CO2 = self.CO2_LEVELS
        start_temp = self.GLOBAL_TEMP
        start_pH = self.pH
        start_sea_level = self.GLOBAL_SEA_LEVEL
        start_ocean_temp = self.OCEAN_TEMP
        start_ee_count = self.EXTREME_EVENTS_COUNT #Start Extreme Event Count        

        global text_year,text_sea_level,text_co2,text_temp,text_eec,text_ocean_temp,text_pH

        year_frame = gui.new_frame(root,1,0,"NEWS")

        label_year = gui.new_label(year_frame,"Year: ",1,0,"NEWS")




        text_year = gui.new_entry(year_frame,year_entry,5,1,1,"NEWS")

        co2_frame = gui.new_frame(root,1,1,"NEWS")

        label_co2 = gui.new_label(co2_frame,", CO2 Level (ppm): ",1,2,"NEWS")

        text_co2 = gui.new_label(co2_frame,start_CO2,1,3,"NEWS")
        
        temp_frame = gui.new_frame(root,1,2,"NEWS")

        label_temp = gui.new_label(temp_frame,", Global Temp (°F): ",1,4,"NEWS")

        text_temp = gui.new_label(temp_frame,start_temp,1,5,"NEWS")

        #eec_frame = gui.new_frame(root,1,3,"NEWS")

        #label_eec = gui.new_label(eec_frame,", Tornado Count: ",1,6,"NEWS")

        #text_eec = gui.new_label(eec_frame,start_ee_count,1,7,"NEWS")
        
        ocean_temp_frame = gui.new_frame(root,3,0,"NEWS")
        
        label_ocean_temp = gui.new_label(ocean_temp_frame,"Global Ocean Temp (°F): ",4,0,"NEWS")

        text_ocean_temp = gui.new_label(ocean_temp_frame,start_ocean_temp,4,1,"NEWS")

        sea_level_frame = gui.new_frame(root,3,1,"NEWS")

        label_sea_level = gui.new_label(sea_level_frame,", Sea Level (inches): ",4,2,"NEWS")

        text_sea_level = gui.new_label(sea_level_frame,start_sea_level,4,3,"NEWS")

        pH_frame = gui.new_frame(root,3,2,"NEWS")

        label_pH = gui.new_label(pH_frame,", pH: ",4,4,"NEWS")

        text_pH = gui.new_label(pH_frame,start_pH,4,5,"NEWS")

        button_frame = gui.new_frame(root,1,4,"NEWS")

        button = gui.new_button(button_frame,"GO!",self.go,1,10,"NEWS")['bg']="green"


        column_span = 11

        '''image_label = Label(root,image=self.IMAGE_DROUGHT)
        image_label.grid(row=2,column=0,sticky="NEWS",columnspan=round(column_span/2))

        image_label2 = Label(root,image=self.IMAGE_EXTREME_EVENT)
        image_label2.grid(row=2,column=round(column_span/2)-1,sticky="NEWS",columnspan=round(column_span/2))

        image_label3 = Label(root,image=self.IMAGE_FLOOD)
        image_label3.grid(row=3,column=0,sticky="NEWS",columnspan=round(column_span/2))

        image_label4 = Label(root,image=self.IMAGE_CORAL_REEF)
        image_label4.grid(row=3,column=round(column_span/2)-1,sticky="NEWS",columnspan=round(column_span/2))'''

        #image
        '''image_frame = Frame(root).grid(row=2,column=0,padx=5,pady=5,columnspan=column_span,sticky="NEWS")
        image = Label(image_frame,bg="blue").grid(row=0,column=0,columnspan=column_span)'''

    def go(self,year=-1,step=10):
        
        print(year_entry.get())
        
        year = year_entry.get()

        if isdigit(year): 

            year = int(year)

            gui.root.lift()
            #self.start(gui.root)

            ocean_temp_year, ocean_temp_data = trendline.get_data(path_to_here+"data\\Ocean_Temp.txt")
            #ocean_temp_trend = trendline.find_linear_trend_from_list(ocean_temp_year, ocean_temp_data)
            ocean_temp_trend, ocean_temp_trend_K = trendline.get_trend_v2(path_to_here + "data\Ocean_Temp.txt","exponential",1.021,self.YEAR)

            #Tornado_Trend = trendline.get_trend(path_to_here+"data\Tornadoes.txt")
            #EE_Trend = Tornado_Trend # + others


            i = 0
            if year < 0:
                year = self.YEAR
            SeaLevel = self.GLOBAL_SEA_LEVEL
            CarbonDioxide = self.CO2_LEVELS
            Temp = self.GLOBAL_TEMP
            pH = self.pH
            Ocean_Temp = self.OCEAN_TEMP
            #Extreme_Event_Count = self.EXTREME_EVENTS_COUNT



            '''while i < step:
                i += 1
                year += 1
                SeaLevel = self.SEA_LEVEL_CHANGE*1.00825**year+self.LEVEL_CHANGE_K
                CarbonDioxide = self.CO2_CHANGE*1.02**year+self.CO2_CHANGE_K
                Temp = self.TEMP_CHANGE*1.025**year+self.TEMP_CHANGE_K
                pH = self.pH_CHANGE*(year-2019)+self.START_pH
                Ocean_Temp = ocean_temp_trend*1.021**year+ocean_temp_trend_K
                #Extreme_Event_Count = self.TORNADO_CHANGE*0.9791**year+self.TORNADO_CHANGE_K

                time.sleep(0.1)'''

            #generate new values
            SeaLevel = self.SEA_LEVEL_CHANGE*1.00825**year+self.LEVEL_CHANGE_K
            CarbonDioxide = self.CO2_CHANGE*1.02**year+self.CO2_CHANGE_K
            Temp = self.TEMP_CHANGE*1.025**year+self.TEMP_CHANGE_K
            pH = self.pH_CHANGE*(year-2019)+self.START_pH
            Ocean_Temp = ocean_temp_trend*1.021**year+ocean_temp_trend_K
            #Extreme_Event_Count = self.TORNADO_CHANGE*0.9791**year+self.TORNADO_CHANGE_K

            text_sea_level['text']=round(SeaLevel,1)
            text_co2['text']=round(CarbonDioxide,1)
            text_temp['text']=round(9*Temp/5,2)
            #text_eec['text']=round(Extreme_Event_Count)
            text_pH['text']=round(pH,2)
            text_ocean_temp['text']=round(9*Ocean_Temp/5,2)

            self.YEAR = year
            self.GLOBAL_SEA_LEVEL = SeaLevel
            self.CO2_LEVELS = CarbonDioxide
            self.GLOBAL_TEMP = Temp
            self.pH = pH
            self.OCEAN_TEMP = Ocean_Temp
            #self.EXTREME_EVENTS_COUNT = Extreme_Event_Count

            #year_entry.initialize("2019")

        else:
            year = self.YEAR
            SeaLevel = self.GLOBAL_SEA_LEVEL
            CarbonDioxide = self.CO2_LEVELS
            Ocean_Temp = self.OCEAN_TEMP
            pH = self.pH
        return year,SeaLevel,CarbonDioxide,Ocean_Temp,pH

