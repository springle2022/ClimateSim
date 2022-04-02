import math,operator

import os
path_to_here = os.path.dirname(__file__)
path_to_here = path_to_here[0:1-len("\library_files")]

def mean(list):
    sum = 0
    for number in list:
        sum += number
    return sum/len(list)

def median(list):
    list.sort()
    print(list)
    if (len(list)-1)%2 == 0:
        i = round((len(list)-1)/2)
        
        #print(i)

        return list[i]

    else:
        i = math.floor((len(list)-1)/2)
        v1 = list[i]
        v2 = list[i+1]

        return (v1+v2)/2

def get_data(file_name):
    with open(file_name,"r") as data_file:
        data_list = []
        for line in data_file:
            data_list.append(line)
        i = 0

        x_list = [] #list to store all "x" values
        y_list = [] #list to store all "y" values

        while i < len(data_list):
            line = data_list[i]
            isDigit = False
            if len(line) > 1:
                if line[0].isdigit() == True or line[1].isdigit() == True:
                    isDigit = True
            elif line[0].isdigit() == True:
                isDigit = True
            
            
            if isDigit == True:
                j = 0
                x = "" #This will store the independent variable
                while line[j] != " " and line[j] != "," and line[j] != "\n":
                    x = x + line[j]

                    j += 1
                x = float(x)
                x_list.append(x)
                while line[j] == " " or line[j] == ",":

                    j += 1
                
                y = "" #This will store the dependent variable

                while line[j] != " " and line[j] != ","  and line[j] != "\n":
                    y = y + line[j]

                    j += 1
                y = float(y)
                y_list.append(y)
                #print("x: " + str(x) + ", y: " + str(y)) #debug
            i += 1
    return x_list,y_list

def find_linear_trend_from_list(x_list,y_list):
    trend = 0
    change_x_list = []
    change_y_list = []

    #change in x
    i = 0
    while i < len(x_list) -1:
        change_x_list.append(x_list[i+1]-x_list[i])
        i += 1
    
    #change in y
    i = 0
    while i < len(y_list) -1:
        change_y_list.append(y_list[i+1]-y_list[i])
        i += 1

    #x trend
    i = 0
    x_trend = 0
    while i < len(change_x_list):
        x_trend += change_x_list[i]
        i += 1
    
    #y trend
    i = 0
    y_trend = 0
    while i < len(change_y_list):
        y_trend += change_y_list[i]
        i += 1

    trend = y_trend/x_trend

    return trend

def find_trend_v2(x_list,y_list,type,base,input_value):
    if type == "line":

        if len(x_list) != len(y_list):
            print("Error: 'x_list' and 'y_list' are not equal length")
            return None
        
        #trendline calculation from: https://classroom.synonym.com/calculate-trendline-2709.html#calculating-the-slope-(m)-of-the-trendline 

        #n is the length of the lists
        n = len(x_list)

        #a is 'n times the summation of all x-values multiplied by their corresponding y-values'

        i = 0
        result = 0
        while i < n:
            result += (x_list[i] * y_list[i])

            i += 1

        a = n * (result)

        #b is 'the sum of all x-values times the sum of all y-values'
        i = 0
        result_x = 0
        result_y = 0
        while i < n:
            result_x += x_list[i]
            result_y += y_list[i]

            i += 1

        b = result_x*result_y

        #c is 'n times the sum of all squared x-values'
        i = 0
        result = 0
        while i < n:
            result += (x_list[i] ** 2)

            i += 1

        c = n * result

        #d is 'the squared sum of all x-values'
        i = 0
        result = 0
        while i < n:
            result += x_list[i]

            i += 1

        d = result ** 2

        #calculate m
        m = (a - b) / (c - d)
        #print(m)
        return m, k
    elif type == "exponential":
        
        if len(x_list) != len(y_list):
            print("Error: 'x_list' and 'y_list' are not equal length")
            return None
        
        i = 0
        while i < len(x_list):
            x_list[i] = math.pow(base,x_list[i])
            i += 1
        
        #trendline calculation from: https://classroom.synonym.com/calculate-trendline-2709.html#calculating-the-slope-(m)-of-the-trendline 

        #n is the length of the lists
        n = len(x_list)

        #a is 'n times the summation of all x-values multiplied by their corresponding y-values'

        i = 0
        result = 0
        while i < n:
            result += (x_list[i] * y_list[i])

            i += 1

        a = n * (result)

        #b is 'the sum of all x-values times the sum of all y-values'
        i = 0
        result_x = 0
        result_y = 0
        while i < n:
            result_x += x_list[i]
            result_y += y_list[i]

            i += 1

        b = result_x*result_y

        #c is 'n times the sum of all squared x-values'
        i = 0
        result = 0
        while i < n:
            result += (x_list[i] ** 2)

            i += 1

        c = n * result

        #d is 'the squared sum of all x-values'
        i = 0
        result = 0
        while i < n:
            result += x_list[i]

            i += 1

        d = result ** 2

        #calculate m
        m = (a - b) / (c - d)
        #print(m)

        ### Calculating the y-intercept (b) of the Trendline, https://classroom.synonym.com/calculate-trendline-2709.html

        #Let e equal the sum of all y-values

        i = 0
        e = 0
        while i < len(y_list):
            e += y_list[i]
            i += 1

        #Let f equal the slope times the sum of all x-values
        i = 0
        x_sum = 0
        while i < len(x_list):
            x_sum += x_list[i]
            i += 1

        f = m*x_sum

        #Y-intercept = k

        k = (e-f)/n
        
        return m, k

def get_trend(file_name):
    x,y = get_data(file_name)
    trend = find_linear_trend_from_list(x,y)
    return trend

def get_trend_v2(file_name,type,base,input_value):
    x,y = get_data(file_name)
    trend = find_trend_v2(x,y,type,base,input_value)
    return trend
    
        
        
