# encoding: utf-8

"""
Copyright (c) 2018, Maintainer: David Lackovic
based on Ernesto Ruge https://github.com/ruhrmobil-E/meine-luftdaten/
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

country_codes = [
    ('AF', 'Afghanistan'),
    ('EG', 'Ägypten'),
    ('AX', 'Aland'),
    ('AL', 'Albanien'),
    ('DZ', 'Algerien'),
    ('AS', 'Amerikanisch-Samoa'),
    ('VI', 'Amerikanische Jungferninseln'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarktis'),
    ('AG', 'Antigua und Barbuda'),
    ('GQ', 'Äquatorialguinea'),
    ('AR', 'Argentinien'),
    ('AM', 'Armenien'),
    ('AW', 'Aruba'),
    ('AC', 'Ascension'),
    ('AZ', 'Aserbaidschan'),
    ('ET', 'Äthiopien'),
    ('AU', 'Australien'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesch'),
    ('BB', 'Barbados'),
    ('BE', 'Belgien'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivien'),
    ('BA', 'Bosnien und Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvetinsel'),
    ('BR', 'Brasilien'),
    ('VG', 'Britische Jungferninseln'),
    ('IO', 'Britisches Territorium im Indischen Ozean'),
    ('BN', 'Brunei'),
    ('BG', 'Bulgarien'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('CL', 'Chile'),
    ('CN', 'China, Volksrepublik'),
    ('CK', 'Cookinseln'),
    ('CR', 'Costa Rica'),
    ('DK', 'Dänemark'),
    ('DE', 'Deutschland'),
    ('SH', 'Die Kronkolonie St. Helena und Nebengebiete'),
    ('DG', 'Diego Garcia'),
    ('DM', 'Dominica'),
    ('DO', 'Dominikanische Republik'),
    ('DJ', 'Dschibuti'),
    ('EC', 'Ecuador'),
    ('SV', 'El Salvador'),
    ('ER', 'Eritrea'),
    ('EE', 'Estland'),
    ('EU', 'Europäische Union'),
    ('FK', 'Falklandinseln'),
    ('FO', 'Färöer'),
    ('FJ', 'Fidschi'),
    ('FI', 'Finnland'),
    ('FR', 'Frankreich'),
    ('GF', 'Französisch-Guayana'),
    ('PF', 'Französisch-Polynesien'),
    ('TF', 'Französische Süd- und Antarktisgebiete'),
    ('GA', 'Gabun'),
    ('GM', 'Gambia'),
    ('GE', 'Georgien'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GD', 'Grenada'),
    ('GR', 'Griechenland'),
    ('GL', 'Grönland'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GG', 'Guernsey'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HM', 'Heard und McDonaldinseln'),
    ('HN', 'Honduras'),
    ('HK', 'Hongkong'),
    ('IN', 'Indien'),
    ('ID', 'Indonesien'),
    ('IQ', 'Irak'),
    ('IR', 'Iran'),
    ('IE', 'Irland'),
    ('IS', 'Island'),
    ('IM', 'Isle of Man'),
    ('IL', 'Israel'),
    ('IT', 'Italien'),
    ('JM', 'Jamaika'),
    ('JP', 'Japan'),
    ('YE', 'Jemen'),
    ('JE', 'Jersey'),
    ('JO', 'Jordanien'),
    ('KY', 'Kaimaninseln'),
    ('KH', 'Kambodscha'),
    ('CM', 'Kamerun'),
    ('CA', 'Kanada'),
    ('IC', 'Kanarische Inseln'),
    ('CV', 'Kap Verde'),
    ('KZ', 'Kasachstan'),
    ('QA', 'Katar'),
    ('KE', 'Kenia'),
    ('KG', 'Kirgisistan'),
    ('KI', 'Kiribati'),
    ('CC', 'Kokosinseln'),
    ('CO', 'Kolumbien'),
    ('KM', 'Komoren'),
    ('CD', 'Kongo, Demokratische Republik'),
    ('HR', 'Kroatien'),
    ('CU', 'Kuba'),
    ('KW', 'Kuwait'),
    ('LA', 'Laos'),
    ('LS', 'Lesotho'),
    ('LV', 'Lettland'),
    ('LB', 'Libanon'),
    ('LR', 'Liberia, Republik'),
    ('LY', 'Libyen'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Litauen'),
    ('LU', 'Luxemburg'),
    ('MO', 'Macao'),
    ('MG', 'Madagaskar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Malediven'),
    ('ML', 'Mali, Republik'),
    ('MT', 'Malta'),
    ('MA', 'Marokko'),
    ('MH', 'Marshallinseln'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauretanien'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MK', 'Mazedonien'),
    ('MX', 'Mexiko'),
    ('FM', 'Mikronesien, Föderierte Staaten von'),
    ('MD', 'Moldawien'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolei'),
    ('ME', 'Montenegro'),
    ('MS', 'Montserrat'),
    ('MZ', 'Mosambik'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NC', 'Neukaledonien'),
    ('NZ', 'Neuseeland'),
    ('NT', 'Neutrale Zone (Irak)'),
    ('NI', 'Nicaragua'),
    ('NL', 'Niederlande'),
    ('AN', 'Niederländische Antillen'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('KP', 'Nordkorea'),
    ('MP', 'Nördliche Marianen'),
    ('NF', 'Norfolkinsel'),
    ('NO', 'Norwegen'),
    ('OM', 'Oman'),
    ('AT', 'Österreich'),
    ('TL', 'Osttimor'),
    ('PK', 'Pakistan'),
    ('PS', 'Palästinensische Autonomiegebiete'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua-Neuguinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippinen'),
    ('PN', 'Pitcairninseln'),
    ('PL', 'Polen'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('CI', 'Republik Côte d’Ivoire'),
    ('CG', 'Republik Kongo'),
    ('RE', 'Réunion'),
    ('RW', 'Ruanda'),
    ('RO', 'Rumänien'),
    ('RU', 'Russische Föderation'),
    ('SB', 'Salomonen'),
    ('ZM', 'Sambia'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'São Tomé und Príncipe'),
    ('SA', 'Saudi-Arabien'),
    ('SE', 'Schweden'),
    ('CH', 'Schweiz'),
    ('SN', 'Senegal'),
    ('RS', 'Serbien'),
    ('CS', 'Serbien und Montenegro'),
    ('SC', 'Seychellen'),
    ('SL', 'Sierra Leone'),
    ('ZW', 'Simbabwe'),
    ('SG', 'Singapur'),
    ('SK', 'Slowakei'),
    ('SI', 'Slowenien'),
    ('SO', 'Somalia, Demokratische Republik'),
    ('SU', 'Sowjetunion'),
    ('ES', 'Spanien'),
    ('LK', 'Sri Lanka'),
    ('KN', 'St. Kitts und Nevis'),
    ('LC', 'St. Lucia'),
    ('PM', 'St. Pierre und Miquelon'),
    ('VC', 'St. Vincent und die Grenadinen'),
    ('ZA', 'Südafrika'),
    ('SD', 'Sudan'),
    ('GS', 'Südgeorgien und die Südlichen Sandwichinseln'),
    ('KR', 'Südkorea'),
    ('SR', 'Suriname'),
    ('SJ', 'Svalbard und Jan Mayen'),
    ('SZ', 'Swasiland'),
    ('SY', 'Syrien'),
    ('TJ', 'Tadschikistan'),
    ('TW', 'Taiwan'),
    ('TZ', 'Tansania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad und Tobago'),
    ('TA', 'Tristan da Cunha'),
    ('TD', 'Tschad'),
    ('CZ', 'Tschechien'),
    ('TN', 'Tunesien'),
    ('TR', 'Türkei'),
    ('TM', 'Turkmenistan'),
    ('TC', 'Turks- und Caicosinseln'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('HU', 'Ungarn'),
    ('UY', 'Uruguay'),
    ('UZ', 'Usbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatikanstadt'),
    ('VE', 'Venezuela'),
    ('AE', 'Vereinigte Arabische Emirate'),
    ('US', 'Vereinigte Staaten'),
    ('GB', 'Vereinigtes Königreich'),
    ('VN', 'Vietnam'),
    ('WF', 'Wallis und Futuna'),
    ('CX', 'Weihnachtsinsel'),
    ('BY', 'Weißrussland'),
    ('EH', 'Westsahara'),
    ('CF', 'Zentralafrikanische Republik'),
    ('CY', 'Zypern, Republik')
]
