import xml.etree.ElementTree as ET
import pandas as pd
import urllib.request
import datetime
import time

starttime=time.time()
while True:
    print("tick")
    urllib.request.urlretrieve('https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml', "stations.xml")
    hour = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tree = ET.parse('stations.xml')
    root = tree.getroot()

    columns = []

    for child in root[0]:
        columns.append(child.tag)
        print(child.tag)

    station_list = []
    station_info = []

    for child in root:
        #print child.tag, child.attrib
        for grandchild in child:
            station_info.append(grandchild.text)
        station_list.append(station_info)
        station_info = []
        
    df = pd.DataFrame(station_list, columns=columns)
    df.to_csv("tfl " + hour[0:4]+'_'+hour[5:7]+'_'+hour[8:10]+'_'+hour[11:13]+'_'+hour[14:16] + ".csv")
    #df
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))