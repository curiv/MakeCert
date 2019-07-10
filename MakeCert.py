#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def MakeCert(FONT,CORD_FIO_C,CORD_TEAM_C,COLOR,TEMPLATE_NAME,line):
    img  = Image.open( TEMPLATE_NAME )
    draw = ImageDraw.Draw( img )
    
    FIO,TEAM   = line.split(',')
    TSIZE_FIO  = draw.textsize( FIO, FONT )
    TSIZE_TEAM = draw.textsize( TEAM, FONT )
    
    # calibrating a text position 
    # depending on text size
    CORD_FIO_C[0]  -=  TSIZE_FIO[0]/2
    CORD_TEAM_C[0] -= TSIZE_TEAM[0]/2

    draw.text( CORD_TEAM_C, TEAM, COLOR, font=FONT )
    draw.text( CORD_FIO_C, FIO, COLOR, font=FONT )
   
    # saving the picture at the current directory 
    # with that name
    img.save( f"{TEAM.strip()}-{FIO.strip()}.png" )


TEMPLATE_NAME = "cert.png"
LIST_NAME = "cert.lst"
FONT = ImageFont.truetype( "arial.ttf", 20 )
COLOR = ( 0, 0, 0 )

with open( LIST_NAME,"r" ) as file:
    for line in file:
        # static gaps centre 
        CORD_FIO_C  = [ 270, 620 ]
        CORD_TEAM_C = [ 270, 740 ]

        MakeCert(FONT,CORD_FIO_C,CORD_TEAM_C,COLOR,TEMPLATE_NAME,line)
