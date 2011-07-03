#!/usr/bin/python
# -*- coding: utf-8 -*-
#python octree implementation
# Code © Spencer Krum June 2011
# Released underl GPLv3 See LICENSE file in this repository

"""
pywy.py
Takes the output of iwlist wlan0 scan from a file and puts it
into an array of objects which can be ordered based on dynamic
factors such as SNR, signal strength, encryption, essid
"""


import sys



class Network():
    """
    Holds information about a node, as returned by iwlist
    """
    def __init__(self,cell):
        extra = cell[0]
        del cell[0]
        i = 0
        for i in range(len(cell)):
            if "Quality" in cell[i]:
                qual,sig,noise = cell[i].split('  ')
                index = i

        del cell[index]
        cellnum, address = extra.split('-')
        qnum = qual.split('=')[1]
        num,dem = qnum.split('/')
        qvalflt = float(num)/float(dem)

        self.facts['Quality'] = qvalflt
        self.facts['Signal level'] = float(sig.split('=')[1].split(' ')[0])
        self.facts['Noise level'] = float(noise.split('=')[1].split(' ')[0])
        self.facts['Cell'] = int(cellnum.split(' ')[1])
        self.facts['Address'] = address.split(' ')[2]

        for k,v in self.facts.iteritems():
            for i in cell:
                if k in i:
                    self.facts[k] = i.split(':')[1]
        self.quality = self.facts["Quality"]
        self.essid = self.facts["ESSID"]
        self.mac = self.facts["Address"]
        self.encrypt = self.facts['Encryption key']
        self.channel = int(self.facts['Channel'])
    facts = { 
            'Cell' :  '', 
            'Address' : '',
            'ESSID' : '',
            'Protocol' : '',
            'Mode' : '',
            'Channel' : '',
            'Encryption key' : '',
            'Bit Rates' : '',
            'Extra'     :  '',
            'Quality'   : '',
            'Signal level' : '',
            'Noise level'  : '',
            'IE'  : '',
            'Group Cipher' :  '',
            'Pairwise Ciphers'  : '',
            'Authentication Suites' : '',
            'IE' : '',
            'Extra' : '',
            }
            
class iwlist():
    def __init__(self, lines):
        self.nets = self.parse_lines(lines)
    def parse_lines(self, lines):
        z = []
        for i in lines:
            z.append((i.rstrip()).lstrip())

        z = z[1:]

        cells = []

        i = 0
        cell_delimiters = []
        while i < len(z):
            if "Cell" in z[i]:
                cell_delimiters.append(i)
            i += 1


        cell_delimiters = cell_delimiters[1:]

        foo = 0
        for i in cell_delimiters:
            cell = z[foo:i]
            cells.append(cell)
            foo = i
        nets = []
        for cell in cells:
            net = Network(cell)
            nets.append(net)
        return nets
    def order_by_quality(self):
        networks = []
        for net in self.nets:
            networks.append((net.quality, net.mac, net.essid,net.channel))
        networks.sort()
        self.printout(networks)
    def printout(self, networks):
        for net in networks:
            print "\t".join(map(str,net))


    
if __name__ == "__main__":

    filename = sys.argv[1]

    with open( filename, 'r') as f:
        lines = f.readlines()
    f.closed
    scan = iwlist(lines)
    scan.order_by_quality()





