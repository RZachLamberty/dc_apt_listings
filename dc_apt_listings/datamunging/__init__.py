#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: __init__.py
Author: zlamberty
Created: 2015-07-12

Description:
    data munging routines used to clean the data collected from our web
    scraping

Usage:
    <usage>

"""

import json
import logging
import lxml.html
import numpy as np
import os
import pandas
import psycopg2
import pylab

from shapely.geometry import shape, MultiPolygon, Point


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

DC_GEOJSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'data', 'dcneighorhoodboundarieswapo.geojson'
)

logger = logging.getLogger(__name__)


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def main(user='dcapa', password='dcapa', dbname='dc_apa_scraping',
         host='localhost'):
    """ clean that ish """
    d = load_table(user=user, password=password, dbname=dbname, host=host)

    d = clean_df(d)
    d = add_neighborhood_data(d)

    return d


def load_table(user='dcapa', password='dcapa', dbname='dc_apa_scraping',
               host='localhost'):
    conn = psycopg2.connect(
        user=user, dbname=dbname, host=host, password=password
    )
    return pandas.read_sql("SELECT * FROM raw_data", conn)


# ----------------------------- #
#   cleaning routines           #
# ----------------------------- #

def clean_df(d):
    d = clean_title(d)
    d = clean_content(d)
    d = clean_price(d)
    return d


def clean_title(d):
    d.title = d.title.str.lower()
    d.title = d.title.str.strip()
    d.title = d.title.str.replace('[^a-zA-Z0-9$]', ' ')
    return d


def clean_content(d):
    d.content = d.content.apply(clean_html)
    d.content = d.content.str.lower()
    d.content = d.content.str.strip()
    d.content = d.content.str.replace('[^a-zA-Z0-9$]', ' ')
    return d


def clean_price(d):
    d.price = d.price.str.replace(',', '')
    d.price = d.price.str.replace('$', '')
    d.price = d.price.astype(float)
    return d


# ----------------------------- #
#   neighborhood data           #
# ----------------------------- #

def add_neighborhood_data(d, fjson=DC_GEOJSON, namekey='subhood'):
    """ read in neighborhood definitions from a geojson file, and attempt to
        update the dataframe with neighborhood names

    """
    nbhdDat = load_dc_geojson(fjson)
    shapelist = dc_geojson_to_shapelist(nbhdDat)

    lnglt = d[['longitude', 'latitude']]
    neigh = pandas.Series(name="neighborhood", index=d.index)

    for (subfeat, shape) in zip(nbhdDat['features'], shapelist):
        name = subfeat['properties'][namekey]
        matches = lnglt.apply(lambda pt: shape.contains(Point(pt[0], pt[1])), 1)
        neigh[matches] = name

    d['neigh'] = neigh
    return d


def load_dc_geojson(fjson=DC_GEOJSON):
    """ given a geojson of dc neighborhoods, load that shit """
    with open(fjson, 'rb') as f:
        return json.load(f, strict=False)


def dc_geojson_to_shapelist(dcdat):
    shapes = []

    for subfeat in dcdat['features']:
        s = shape(subfeat['geometry'])
        shapes.append(s)

    return shapes


# ----------------------------- #
#   plotting functions          #
# ----------------------------- #

def plot_neighborhood_geom(ax, shapeList):
    """ takes a list of multipolygon shapes and plots them to an axis """
    for mp in shapeList:
        fill_multipolygon(ax, mp, 'b')
    fill_multipolygon(ax, shapeList[0], 'r')


def fill_polygon(ax, polygon, color):
    x, y = polygon.exterior.xy
    ax.fill(x, y, color, alpha=0.5)


def fill_multipolygon(ax, mp, color):
    for polygon in mp:
        fill_polygon(ax, polygon, color)


# ----------------------------- #
#   helper functions            #
# ----------------------------- #

def clean_html(html):
    return lxml.html.document_fromstring(html).text_content()
