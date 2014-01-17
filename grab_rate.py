#!/usr/bin/python
#/*Copyright (c) 2013 Chris Knorowski <cknorow@gmail.com>
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program.  If not, see <http://www.gnu.org/licenses/>.
# */

__author__ = 'cknorow@gmail.com (Chris knorowski)'

import os
import sys
import urllib2

cryptsy_markets = {"LTC/BTC":"3",
"FTC/BTC":"5",
"MNC/BTC":"7",
"CNC/BTC":"8",
"BQC/BTC":"10",
"YAC/BTC":"11",
"ELC/BTC":"12",
"NVC/BTC":"13",
"WDC/BTC":"14",
"CNC/LTC":"17",
"WDC/LTC":"21",
"YAC/LTC":"22",
"BTB/BTC":"23",
"DGC/BTC":"26",
"TRC/BTC":"27",
"PPC/BTC":"28",
"NMC/BTC":"29",
"GLD/BTC":"30",
"PXC/BTC":"31",
"NBL/BTC":"32",
"FRK/BTC":"33",
"LKY/BTC":"34",
"JKC/LTC":"35",
"GLD/LTC":"36",
"RYC/LTC":"37",
"IXC/BTC":"38",
"FRC/BTC":"39",
"AMC/BTC":"43",
"FST/BTC":"44",
"MEC/BTC":"45",
"DBL/LTC":"46",
"ARG/BTC":"48",
"BTE/BTC":"49",
"BTG/BTC":"50",
"SBC/BTC":"51",
"DVC/LTC":"52",
"CAP/BTC":"53",
"NRB/BTC":"54",
"EZC/LTC":"55",
"MEM/LTC":"56",
"ALF/BTC":"57",
"CRC/BTC":"58",
"IFC/LTC":"60",
"FLO/LTC":"61",
"MST/LTC":"62",
"XPM/BTC":"63",
"KGC/BTC":"65",
"ANC/BTC":"66",
"XNC/LTC":"67",
"CSC/BTC":"68",
"EMD/BTC":"69",
"CGB/BTC":"70",
"QRK/BTC":"71",
"DMD/BTC":"72",
"CMC/BTC":"74",
"ORB/BTC":"75",
"GLC/BTC":"76",
"GLX/BTC":"78",
"HBN/BTC":"80",
"SPT/BTC":"81",
"GDC/BTC":"82",
"GME/LTC":"84",
"ZET/BTC":"85",
"PHS/BTC":"86",
"RED/LTC":"87",
"SRC/BTC":"88",
"NEC/BTC":"90",
"CPR/LTC":"91",
"PYC/BTC":"92",
"ELP/LTC":"93",
"ADT/LTC":"94",
"CLR/BTC":"95",
"DGC/LTC":"96",
"SXC/LTC":"98",
"MEC/LTC":"100",
"PXC/LTC":"101",
"BUK/BTC":"102",
"TIX/XPM":"103",
"NET/XPM":"104",
"IFC/XPM":"105",
"XPM/LTC":"106",
"TIX/LTC":"107",
"NET/LTC":"108",
"COL/LTC":"109",
"COL/XPM":"110",
"ASC/LTC":"111",
"ASC/XPM":"112",
"ADT/XPM":"113",
"TEK/BTC":"114",
"XJO/BTC":"115",
"LK7/BTC":"116",
"TAG/BTC":"117",
"PTS/BTC":"119",
"Poi/nt":"120",
"ANC/LTC":"121",
"DVC/XPM":"122",
"CGB/LTC":"123",
"FST/LTC":"124",
"PPC/LTC":"125",
"QRK/LTC":"126",
"ZET/LTC":"127",
"SBC/LTC":"128",
"BET/BTC":"129",
"TGC/BTC":"130",
"DEM/BTC":"131",
"DOGE/BTC":"132",
"UNO/BTC":"133"}

def btce(pair):
    # btc-e
    try:
        parts = pair.split('/')
        r = urllib2.urlopen('https://btc-e.com/api/2/%s/ticker'%(parts[0].lower()+'_'+parts[1].lower()))
        #btce_markets[pair])
        s = r.readlines()[0]
        tp = s.rfind('last')
        rate =  float(s[tp+6:tp+26].split(',')[0])
        print "BTC-E:", pair, rate
        return rate
    except:
        return "noupdate"


def cryptsy(pair):
	#get dgc to btc price
    try:
        r = urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=%s'%cryptsy_markets[pair])
        s = r.readlines()[0]
        tp = s.rfind('lasttradeprice')
        rate =  float(s[tp:tp+35].split('"')[2])
        print "CRYPTSY:", pair, rate
        return rate
    except:
        return "noupdate"


def coinbasebtc():
	#get btc to usd price
    try:
        r = urllib2.urlopen('https://coinbase.com/api/v1/currencies/exchange_rates')
        s = r.readlines()[0]
        tp = s.rfind('btc_to_usd')
        BtcUsd =  float(s[tp:tp+35].split('"')[2])
        print "COINBASE: BTC/USD", BtcUsd
        return BtcUsd
    except:
        return "noupdate"


def mtgoxbtc():
	#get btc to usd price
    try:
        r = urllib2.urlopen('https://data.mtgox.com/api/2/BTCUSD/money/ticker')
        s = r.readlines()[0]
        tp = s.rfind('"last"')
        BtcUsd =  float(s[tp:tp+35].split('"')[5])
        print "MTGOX: BTC/USD", BtcUsd
        return BtcUsd
    except:
        print 'mtgox failed'
        return "noupdate"

def dgex():
    #get dgex
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
        r = opener.open('http://dgex.com/API/trades.json')
        #r = urllib2.urlopen('http://dgex.com/API/trades.json')
        s = r.readlines()[4]
        tp = s.rfind('"unitprice"')
        rate =  float(s[tp+13:tp+23])
        print "DGEX: NXT/BTC", rate
        return rate
    except:
        print 'mtgox failed'
        return "noupdate"



def btc_balance(address):
    #get balance
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
        r = opener.open('https://blockchain.info/q/addressbalance/'+address)
        s = r.readlines()[0]
        amount =  float(s) * 1e-8
        print "BTC BALANCE:", address, amount
        return amount
    except:
        print 'btc_balance failed'
        return "noupdate"
