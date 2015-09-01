# Copyright (C) 2015 Impact
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

__author__ = "Impact"
__date__ = "$30-jul-2015 12:13:01$"

import langid
import sys
import codecs


if (len(sys.argv) > 1):
    name = sys.argv[1]
else:
    print "no parametros"

corrects = 0
total = 0

langid.set_languages(['es','fr','it','en','pt','ro'])

if (name):
    f = open(name,"r")    
    
    for line in f:        
        text,lang = line.split(";")
        lang = lang.strip()
        total = total + 1
        ident,conf = langid.classify(text)
        ident = ident.strip()        
        if (lang == ident):
            corrects = corrects + 1
    
    print "Aciertos ",corrects,"de",total,"Porcentaje",(float(corrects) / float(total))*100
    
    
#lang,conf = langid.classify("This is a test")




