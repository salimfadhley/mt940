# mt940parser

A  parser for Swift MT940 documents built using the [PLY](http://www.dabeaz.com/ply/) parser generator, tested on Python 3

## About this project

This package is intended to help extract meaningful information from MT940 documents, a format commonly used by banks to
exchange financial information.

MT940 can be parsed as a context-free grammar. This project attempts to describe the syntax of MT940 in [Backus–Naur Form](http://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)
which is understood by [PLY](http://www.dabeaz.com/ply/), a widely used Parser generator written in pure Python.

## Project Status

[![Build Status](https://travis-ci.org/salimfadhley/mt940.svg?branch=master)](https://travis-ci.org/salimfadhley/mt940)
[![Code Health](https://landscape.io/github/salimfadhley/mt940/master/landscape.svg?style=flat)](https://landscape.io/github/salimfadhley/mt940/master)
[![Wheel Status](https://pypip.in/wheel/mt940parser/badge.svg)](https://pypi.python.org/pypi/mt940parser/)
[![Requirements Status](https://requires.io/github/salimfadhley/mt940/requirements.svg?branch=master)](https://requires.io/github/salimfadhley/mt940/requirements/?branch=master)

This project is not under active development - it was originally written as a technical demo of how financial data can be
parsed using the PLY tool. You have my permission to use this code in your commercial project (subject to license), and I
am happy to answer technical questions if they are raised as issues on the GitHub project.

## Installation

The project is hosted on the Python Package Index. You can install it into your current Python environment using the Pip
installation tool:

```bash
pip install mt940parser
```

## Demo

```python
from mt940.parser import parse
import pprint

message = """{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{3:{108:0000000019708714}}{4:
:20:2267602902375194
:25:301775/00059707
:28C:00065/001
:60M:C140401GBP10,10
:61:1404010401C1,NCHGNONREF
REFUNDED CHARGES         REF : 493
:86:4547
:61:1404010401D1,NINTNONREF
O/DRAFT INTEREST
:61:1404010401C1,NMSCNONREF
F/FLOW ACCOUNTNAME    TFRPAYMENTRE
:86:FERENCE12
:61:1404010401D1,NMSCNONREF
PHOENIX DIS F/FLOW    TFRPAYROLL85
:86:412368943
:61:1404010401C1,NMSCNONREF
LTCPTTAM1CBK137       BGCPAYMENTRE
:86:FERENCE34
:61:1404010401D1,NMSCNONREF
TEST BENEFICIARY       DDPAYMENTRE
:86:FERENCE34
:61:1404010401D1,NSTONONREF
LTCPTTAM1CBK138        SO
:61:1404010401C1,NMSCNONREF
REDLIONCOURTLONDON    FPI
:86:FASTERPAYMENTREF01
100000000000000315
301775     10
12MAR14 07:24
:61:1404010401C1,NMSCNONREF
REDLIONCOURTLONDON    FPI
:86:STANDINGORDER12345
FTRT00000000000315
301775     30
12MAR14 07:24
:61:1404010401D1,NMSCNONREF
BENEFICIARY           FPO
:86:200000000000000890
REFERENCE123456
301775     10
18APR14 10:44
:61:1404010401C1,NMSCNONREF
500021
:61:1404010401D1,NMSCNONREF
000016
:61:1404010401C1,NMSCNONREF
FROM A/C              TFR00059618
:86:301775
:61:1404010401D1,NMSCNONREF
TO A/C                TFR00059707
:86:301775
:61:1404010401C1,NMSCNONREF
FROM A/C              TFR00059618
:86:301775
:61:1404010401D1,NMSCNONREF
TO A/C                TFR00059707
:86:301775
:61:1404010401C2,NMSCNONREF
INTEREST (NET)
:61:1404010401D1,NMSCNONREF
FT148090898341           FOREIGN E
:86:UR
:61:1404010401D1,NMSCNONREF
FT148090949341           FOREIGN U
:86:SD
:62F:C140401GBP10,10
:64:C140401GBP10,10
:65:C140402GBP10,10
:65:C140406GBP10,10
:65:C140407GBP10,10
-}"""

pprint.pprint(parse(message))
```

The output looks like this:

```python
{'1': 'F01HBOSXXXXAXXX9999999999',
 '2': 'I940HBOSXXXXXXXXN',
 '3': {'108': '19708714'},
 '4': [('20', '2267602902375194'),
       ('25', '301775/59707'),
       ('28C', '65/1'),
       ('60M', 'C140401GBP10,10'),
       ('61', '1404010401C1,NCHGNONREF\nREFUNDED CHARGES         REF : 493'),
       ('86', '4547'),
       ('61', '1404010401D1,NINTNONREF\nO/DRAFT INTEREST'),
       ('61', '1404010401C1,NMSCNONREF\nF/FLOW ACCOUNTNAME    TFRPAYMENTRE'),
       ('86', 'FERENCE12'),
       ('61', '1404010401D1,NMSCNONREF\nPHOENIX DIS F/FLOW    TFRPAYROLL85'),
       ('86', '412368943'),
       ('61', '1404010401C1,NMSCNONREF\nLTCPTTAM1CBK137       BGCPAYMENTRE'),
       ('86', 'FERENCE34'),
       ('61', '1404010401D1,NMSCNONREF\nTEST BENEFICIARY       DDPAYMENTRE'),
       ('86', 'FERENCE34'),
       ('61', '1404010401D1,NSTONONREF\nLTCPTTAM1CBK138        SO'),
       ('61', '1404010401C1,NMSCNONREF\nREDLIONCOURTLONDON    FPI'),
       ('86',
        'FASTERPAYMENTREF01\n'
        '100000000000000315\n'
        '301775     10\n'
        '12MAR14 07:24'),
       ('61', '1404010401C1,NMSCNONREF\nREDLIONCOURTLONDON    FPI'),
       ('86',
        'STANDINGORDER12345\n'
        'FTRT00000000000315\n'
        '301775     30\n'
        '12MAR14 07:24'),
       ('61', '1404010401D1,NMSCNONREF\nBENEFICIARY           FPO'),
       ('86',
        '200000000000000890\nREFERENCE123456\n301775     10\n18APR14 10:44'),
       ('61', '1404010401C1,NMSCNONREF\n500021'),
       ('61', '1404010401D1,NMSCNONREF\n16'),
       ('61', '1404010401C1,NMSCNONREF\nFROM A/C              TFR00059618'),
       ('86', '301775'),
       ('61', '1404010401D1,NMSCNONREF\nTO A/C                TFR00059707'),
       ('86', '301775'),
       ('61', '1404010401C1,NMSCNONREF\nFROM A/C              TFR00059618'),
       ('86', '301775'),
       ('61', '1404010401D1,NMSCNONREF\nTO A/C                TFR00059707'),
       ('86', '301775'),
       ('61', '1404010401C2,NMSCNONREF\nINTEREST (NET)'),
       ('61', '1404010401D1,NMSCNONREF\nFT148090898341           FOREIGN E'),
       ('86', 'UR'),
       ('61', '1404010401D1,NMSCNONREF\nFT148090949341           FOREIGN U'),
       ('86', 'SD'),
       ('62F', 'C140401GBP10,10'),
       ('64', 'C140401GBP10,10'),
       ('65', 'C140402GBP10,10'),
       ('65', 'C140406GBP10,10'),
       ('65', 'C140407GBP10,10')]}
```

## Further Reading

For more information please refer to:

* [MT940 Explained](http://www.scribd.com/doc/4714259/MT940-Bank-Format-Explained#scribd)
* [TECHNICAL DESCRIPTION OF THE MT940
   STATEMENT FORMAT FOR BUSINESS 24](http://www.csas.cz/static_internet/en/Obchodni_informace-Produkty/Prime_bankovnictvi/Spolecne/Prilohy/MT940_B24.pdf)
* [SWIFT MT 940
   Customer Statement Message and
   SWIFT MT 942 Interim
   Transaction Report](http://martin.hinner.info/bankconvert/swift_mt940_942.pdf)
   
## Software License

Copyright (c) 2015 Salim Fadhley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
