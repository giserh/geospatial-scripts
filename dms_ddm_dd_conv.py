# -*- coding: utf-8 -*-

import re

def dd_to_dms(lat,lon):
    
    d_EW = "W" if int(lon)<0 else "E"
    d_NS = "S" if int(lat)<0 else "N"
    
    d_lon,d_lat = abs(int(lon)),abs(int(lat))
    m_lon,m_lat = abs((lon-int(lon)) * 60), abs((lat-int(lat)) * 60)
    s_lon,s_lat = (m_lon-int(m_lon)) * 60, (m_lat-int(m_lat)) * 60
    
    dms_lon = "%i%s%i%s%.4f%s%s" % (d_lon,chr(176),m_lon,chr(39),s_lon,chr(34),d_EW)
    dms_lat = "%i%s%i%s%.4f%s%s" % (d_lat,chr(176),int(m_lat),chr(39),s_lat,chr(34),d_NS)
    
    return [dms_lat,dms_lon]

def dms_to_dd(dms_lat,dms_lon):
    
    d_lat,m_lat,s_lat, d_NS = re.split('[°\'"]+', dms_lat)
    d_lon,m_lon,s_lon, d_EW = re.split('[°\'"]+', dms_lon)

    dd_lon = (float(s_lon)/3600) + (float(m_lon)/60) + float(d_lon)
    dd_lat = (float(s_lat)/3600) + (float(m_lat)/60) + float(d_lat)
    
    dd_lon = round(dd_lon*-1 if d_EW == "W" else dd_lon,6)
    dd_lat = round(dd_lat*-1 if d_NS == "S" else dd_lat,6)
    return [dd_lat,dd_lon]

def dd_to_ddm(lat,lon):
    d_EW = "W" if int(lon)<0 else "E"
    d_NS = "S" if int(lat)<0 else "N"
    
    d_lon,d_lat = abs(int(lon)),abs(int(lat))
    m_lon,m_lat = abs((lon-int(lon)) * 60), abs((lat-int(lat)) * 60)
    
    ddm_lon = "%i%s%.4f%s%s" % (d_lon,chr(176),m_lon,chr(39),d_EW)
    ddm_lat = "%i%s%.4f%s%s" % (d_lat,chr(176),m_lat,chr(39),d_NS)
    
    return [ddm_lat,ddm_lon]

def ddm_to_dd(ddm_lat,ddm_lon):
    d_lat,m_lat, d_NS = re.split('[°\']+', ddm_lat)
    d_lon,m_lon, d_EW = re.split('[°\']+', ddm_lon)
    
    dd_lon = (float(m_lon)/60) + float(d_lon)
    dd_lat = (float(m_lat)/60) + float(d_lat)
    
    dd_lon = round(dd_lon*-1 if d_EW == "W" else dd_lon,6)
    dd_lat = round(dd_lat*-1 if d_NS == "S" else dd_lat,6)
    return [dd_lat,dd_lon]

latlon = [(41.89193,12.51133),
          (35.227085,-80.843124),
          (34.052235,-118.243683),
          (-33.865143,151.209900)]

for lat,lon in latlon:
    
    # EXAMPLE: DD to DMS
    dms_lat,dms_lon = dd_to_dms(lat,lon)
    
    # EXAMPLE: DMS TO DD
    dd_lat,dd_lon = dms_to_dd(dms_lat,dms_lon)
    
    # EXAMPLE: DD TO DDM
    ddm_lat, ddm_lon = dd_to_ddm(lat,lon)
    
    # EXAMPLE: DDM TO DD
    dd_lat, dd_lon = ddm_to_dd(ddm_lat,ddm_lon)

    print("DD:",lat,lon)
    print("DD TO DMS:",dms_lat,dms_lon)
    print("DD TO DDM:",ddm_lat, ddm_lon,"\n")