#find and return the min, max and average values for the 2nd Column
#find and return the time value for the min and max entries
#the time values should be returned as Python tuples

import sys
import xlrd
from zipfile import ZipFile
datafile = "filename.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
  
    coastCol = set([sheet.cell_value(row, 1) 
                    for row in range(1, sheet.nrows)])
    
    minValue = sys.maxint
    maxValue = 0
    minRow = 0
    maxRow = 0
    for row in range(1, sheet.nrows):
        value = sheet.cell_value(row, 1)
        if value < minValue:
            minValue=value
            minRow = row
        if value > maxValue:
            maxValue=value
            maxRow = row
      
    avgValue = sum(coastCol)/len(coastCol)

    exceltimeMax = sheet.cell_value(maxRow, 0)
    maxTime = xlrd.xldate_as_tuple(exceltimeMax, 0)
    
    exceltimeMin = sheet.cell_value(minRow, 0)
    minTime = xlrd.xldate_as_tuple(exceltimeMin, 0)
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    data['maxtime'] = maxTime
    data['maxvalue'] = maxValue
    data['mintime'] = minTime
    data['minvalue'] = minValue
    data['avgcoast'] = avgValue
    
    print data
    
    return data
