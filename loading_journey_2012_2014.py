import pandas as pd
import glob 

#paths in my computer
#datapath_2012 = 'Y:\\okofm\\tfl\\journey_data\\cyclehireusagestats-2012\\'
#datapath_2013 = 'Y:\\okofm\\tfl\\journey_data\\cyclehireusagestats-2013\\'
#datapath_2014 = 'Y:\\okofm\\tfl\\journey_data\\cyclehireusagestats-2014\\'

#paths at the university cluster
datapath_2012 = 'Y:\\tfl\\journey_data\\cyclehireusagestats-2012\\'
datapath_2013 = 'Y:\\tfl\\journey_data\\cyclehireusagestats-2013\\'
datapath_2014 = 'Y:\\tfl\\journey_data\\cyclehireusagestats-2014\\'

#load files for 2012
count = 0
d2012 = {}
for filename in glob.glob(datapath_2012 + '*.csv'):
    d2012[count] = pd.read_csv(filename, encoding = "ISO-8859-1")
    print(count)
    count += 1

#load files for 2013
count = 0
d2013 = {}
for filename in glob.glob(datapath_2013 + '*.csv'):
    d2013[count] = pd.read_csv(filename, encoding = "ISO-8859-1")
    print(count)
    count += 1
    
#load files for 2014
count = 0
d2014 = {}
for filename in glob.glob(datapath_2014 + '*.csv'):
    d2014[count] = pd.read_csv(filename, encoding = "ISO-8859-1")
    print(count)
    count += 1
    
data2012 = d2012[0].append(d2012[1])
for i in range(2,len(d2012)-1):
    data2012 = data2012.append(d2012[i])
    
data2013 = d2013[0].append(d2013[1])
for i in range(2,len(d2013)-1):
    data2013 = data2013.append(d2013[i])
    
data2014 = d2014[0].append(d2014[1])
for i in range(2,len(d2014)-1):
    data2014 = data2014.append(d2014[i])

data = data2012.append(data2013)
data= data.append(data2014)

data_random_sample = data.sample(frac=0.01)

#transform duration into minutes
data['Duration'] = data['Duration']/60

#adding day of the week, year, quarter, month, week, day, hour, minute
data['year'] = pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.year
data['quarter'] = pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.quarter
data['month'] = pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.month
data['week'] =  pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.week
data['day'] =  pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.day
data['hour'] =  pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.hour
data['minute'] =  pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.minute
data['day_of_week'] = pd.to_datetime(data['Start Date'],format='%d/%m/%Y %H:%M').dt.dayofweek
days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}
data['day_of_week'] = data['day_of_week'].apply(lambda x: days[x])

data.to_csv('Y:\\okofm\\tfl\\journey_data\\data_2012_2014.csv')