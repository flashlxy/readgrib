#! /usr/bin/env python
#coding=utf-8
import pygrib
import pandas as pd
#print list(pygrib.open('fnl_20160511_18_00.grib2'))
#print pygrib.open('fnl_20160511_18_00.grib2').read()
txt=pd.read_csv('input.inp')
a=txt['shortName']
b=txt['typeOfLevel']
c=txt['level']
'''
grbs=pygrib.open('fnl_20160511_06_00.grib2')
grbs.seek(0)
for grb in grbs:
    print grb.shortName,grb.typeOfLevel,grb.level
'''
#grbindx=pygrib.index('fnl_20160511_18_00.grib2','shortName','typeOfLevel','level')
#selected_grbs=grbindx(shortName='u',typeOfLevel='unknown',level=0)
#print selected_grbs

grbs = pygrib.open('fnl_20160512_00_00.grib2')
for i in range(len(a)):
    sel_grbs = grbs.select(shortName=a[i],typeOfLevel=b[i],level=c[i])
    grb=sel_grbs[0]
    data = grb['values']
    grbout = open('test.grb','ab')
    msg = grb.tostring()
    ret = grbout.write(msg)
    #print ret
grbout.close()
grbs = pygrib.open('test.grb')
sel_grbs = grbs.select(shortName='u',level=c)
for grb in sel_grbs:
    print grb

    
'''



for i in range(len(sel_grbs)):
    grb=sel_grbs[i]
    data = grb['values']
    #print data
    #lats, lons = grb.latlons()
    #grb['forecastTime'] = 0


grbs = pygrib.open('test.grb')
sel_grbs = grbs.select(shortName='u',level=(850,700,500))
for grb in sel_grbs:
    print grb
    '''
'''
for grb in selected_grbs:
    print grb
grbindx.write('gfs.grb.idx')
grbindx.close()

    
grbindx = pygrib.index('gfs.grb.idx') # re-open index (no keys specified)
grbindx.keys # not set when opening a saved index file.
for grb in selected_grbs:
    data = grb['values']
    lats, lons = grb.latlons()
    grb['forecastTime'] = 0
    grbout = open('test.grb','wb')
    msg = grb.tostring()
    ret = grbout.write(msg)
'''
    
    
