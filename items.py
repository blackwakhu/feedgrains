import pandas as pd
import numpy as np

data = pd.read_csv('FeedGrains.csv')

def GroupCommod():
    list_commod = list(data.SC_GroupCommod_Desc.unique())
    list_commod_id = list(data.SC_GroupCommod_ID.unique())
    return list_commod, list_commod_id

def GroupGeography():
    list_geography = list(data.SC_GeographyIndented_Desc.unique())
    list_geography_id = list(data.SC_Geography_ID.unique())
    return list_geography, list_geography_id

def Commodity():
    list_commodity = list(data.SC_Commodity_Desc.unique())
    list_commodity_id = list(data.SC_Commodity_ID.unique())
    return list_commodity, list_commodity_id

def Attribute():
    list_attribute = list(data.SC_Attribute_Desc.unique())
    list_attribute_id = list(data.SC_Attribute_ID.unique())
    return list_attribute, list_attribute_id

def Unit():
    list_unit = list(data.SC_Unit_Desc.unique())
    list_unit_id = list(data.SC_Unit_ID.unique())
    return list_unit, list_unit_id

def SortOrder():
    list_sortorder = list(data.SortOrder.unique())
    return list_sortorder

def TimePeriod():
    list_timeperiod = list(data.Timeperiod_Desc.unique())
    list_timeperiod_id = list(data.Timeperiod_ID.unique())
    return list_timeperiod, list_timeperiod_id