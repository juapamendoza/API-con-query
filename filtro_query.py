from fastapi import FastAPI

#pydantic va a obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

# crear el objeto a partir de la clase
discosQuery = FastAPI()

#definir la entidad Disco con sus atributos y su tipo de datos
class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str
    year: int
    label: str

discos_list=[Disco(id=1, title="Midnights", artist="Taylor Swift", genre="Pop", year=2022, label="Republic Records"),
            Disco(id=2, title="reputation", artist="Taylor Swift", genre="Pop", year=2017, label="Big Machine Records"),
            Disco(id=3, title="Lover", artist="Taylor Swift", genre="Pop", year=2019, label="Republic Records"),
            Disco(id=4, title="1989", artist="Taylor Swift", genre="Pop", year=2014, label="Big Machine Records"),
            Disco(id=5, title="Taylor Swift", artist="Taylor Swift", genre="Country", year=2006, label="Big Machine Records"),
            Disco(id=6, title="Fearless", artist="Taylor Swift", genre="Country", year=2008, label="Big Machine Records"),
            Disco(id=7, title="Speak Now", artist="Taylor Swift", genre="Country", year=2010, label="Big Machine Records"),
            Disco(id=8, title="Red", artist="Taylor Swift", genre="Pop", year=2012, label="Big Machine Records"),
            Disco(id=9, title="folklore", artist="Taylor Swift", genre="Indie", year=2020, label="Republic Records"),
            Disco(id=10, title="evermore", artist="Taylor Swift", genre="Indie", year=2020, label="Republic Records"),
            Disco(id=11, title="Did you know that there's a tunnel under Ocean Blvd", artist="Lana del Rey", genre="Alternative", year=2023, label="Interscope Records"),
            Disco(id=12, title="Blue Banisters", artist="Lana del Rey", genre="Alternative", year=2021, label="Interscope Records"),
            Disco(id=13, title="Chemtrails Over The Country Club", artist="Lana del Rey", genre="Alternative", year=2021, label="Interscope Records"),
            Disco(id=14, title="Norman Fucking Rockwell", artist="Lana del Rey", genre="Alternative", year=2019, label="Interscope Records"),
            Disco(id=15, title="Lust For Life", artist="Lana del Rey", genre="Alternative", year=2017, label="Interscope Records"),
            Disco(id=16, title="Honeymoon", artist="Lana del Rey", genre="Alternative", year=2015, label="Interscope Records"),
            Disco(id=17, title="Ultraviolence", artist="Lana del Rey", genre="Alternative", year=2014, label="Interscope Records"),
            Disco(id=18, title="Born to Die", artist="Lana del Rey", genre="Alternative", year=2012, label="Interscope Records"),
            Disco(id=19, title="Paradise", artist="Lana del Rey", genre="Alternative", year=2012, label="Interscope Records"),
            Disco(id=20, title="Pure Heroine", artist="Lorde", genre="Alternative", year=2013, label="Universal Music"),
            Disco(id=21, title="The Love Club", artist="Lorde", genre="Alternative", year=2013, label="Universal Music"),
            Disco(id=22, title="Melodrama", artist="Lorde", genre="Pop", year=2017, label="Republic Records"),
            Disco(id=23, title="Solar Power", artist="Lorde", genre="Alternative", year=2021, label="Universal Music"),
            Disco(id=24, title="Bubblebath", artist="Poppy", genre="Pop", year=2016, label="Island Records"),
            Disco(id=25, title="Poppy.Computer", artist="Poppy", genre="Pop", year=2017, label="Mad Decent"),
            Disco(id=26, title="Am I a Girl?", artist="Poppy", genre="Pop", year=2018, label="Mad Decent"),
            Disco(id=27, title="Choke", artist="Poppy", genre="Experimental", year=2019, label="Mad Deent"),
            Disco(id=28, title="I Disagree", artist="Poppy", genre="Rock", year=2020, label="Sumerian Records"),
            Disco(id=29, title="A Very Poppy Christmas", artist="Poppy", genre="Rock", year=2020, label="Sumerian Records"),
            Disco(id=30, title="EAT (NXT Soundtrack)", artist="Poppy", genre="Rock", year=2021, label="Sumerian Records"),
            Disco(id=31, title="Flux", artist="Poppy", genre="Rock", year=2021, label="Sumerian Records"),
            Disco(id=32, title="Stagger", artist="Poppy", genre="Rock", year=2022, label="Republic Records"),
            Disco(id=33, title="Knockoff", artist="Poppy", genre="Rock", year=2023, label="Republic Records"),
            Disco(id=34, title="World War Joy", artist="The Chainsmokers", genre="Pop", year=2019, label="Columbia Records"),
            Disco(id=35, title="So Far So Good", artist="The Chainsmokers", genre="Pop", year=2022, label="Columbia Records"),
            Disco(id=36, title="Bouquet", artist="The Chainsmokers", genre="Pop", year=2015, label="Columbia Records"),
            Disco(id=37, title="Collage", artist="The Chainsmokers", genre="Pop", year=2016, label="Columbia Records"),
            Disco(id=38, title="Memories...Do Not Open", artist="The Chainsmokers", genre="Pop", year=2017, label="Columbia Records"),
            Disco(id=39, title="Sick Boy", artist="The Chainsmokers", genre="Pop", year=2018, label="Columbia Records"),
            Disco(id=40, title="Los Angeles", artist="ROSALIA", genre="Indie", year=2017, label="Universal Music"),
            Disco(id=41, title="El Mal Querer", artist="ROSALIA", genre="Alternative", year=2018, label="Columbia Records"),
            Disco(id=42, title="MOTOMAMI", artist="ROSALIA", genre="Pop", year=2022, label="Columbia Records"),
            Disco(id=43, title="MTV Unplugged", artist="Katy Perry", genre="Pop", year=2019, label="Capitol Records"),
            Disco(id=44, title="One Of The Boys", artist="Katy Perry", genre="Pop", year=2008, label="Capitol Records"),
            Disco(id=45, title="Teenage Dreams", artist="Katy Perry", genre="Pop", year=2010, label="Capitol Records"),
            Disco(id=46, title="PRISM", artist="Katy Perry", genre="Pop", year=2013, label="Capitol Records"),
            Disco(id=47, title="Witness", artist="Katy Perry", genre="Pop", year=2017, label="Capitol Records"),
            Disco(id=48, title="Smile", artist="Katy Perry", genre="Pop", year=2020, label="Capitol Records"),
            Disco(id=49, title="Glass Animals", artist="Glass Animals", genre="Indie", year=2013, label="Harvest Records"),
            Disco(id=50, title="ZABA", artist="Glass Animals", genre="Indie", year=2014, label="Harvest Records"),
            Disco(id=51, title="How To Be A Human Being", artist="Glass Animals", genre="Indie", year=2016, label="Harvest Records"),
            Disco(id=52, title="Dreamland", artist="Glass Animals", genre="Pop", year=2020, label="Harvest Records"),
            Disco(id=53, title="I Don't Wanna Grow Up", artist="Bebe Rexha", genre="Pop", year=2015, label="Warner Records"),
            Disco(id=54, title="All Your Fault Pt. 1", artist="Bebe Rexha", genre="Pop", year=2017, label="Warner Records"),
            Disco(id=55, title="All Your Fault Pt. 2", artist="Bebe Rexha", genre="Pop", year=2017, label="Warner Records"),
            Disco(id=56, title="Expectations", artist="Bebe Rexha", genre="Pop", year=2018, label="Warner Records"),
            Disco(id=57, title="Better Mistakes", artist="Bebe Rexha", genre="Pop", year=2021, label="Warner Records"),
            Disco(id=58, title="Bebe", artist="Bebe Rexha", genre="Pop", year=2023, label="Warner Records"),
            Disco(id=59, title="For You", artist="Selena Gomez", genre="Pop", year=2014, label="Hollywood Records"),
            Disco(id=60, title="Kiss & Tell", artist="Selena Gomez", genre="Pop", year=2009, label="Hollywood Records"),
            Disco(id=61, title="A Year Without Rain", artist="Selena Gomez", genre="Pop", year=2010, label="Hollywood Records"),
            Disco(id=62, title="When the Sun Goes Down", artist="Selena Gomez", genre="Pop", year=2011, label="Hollywood Records"),
            Disco(id=63, title="Stars Dance", artist="Selena Gomez", genre="Pop", year=2013, label="Hollywood Records"),
            Disco(id=64, title="Revival", artist="Selena Gomez", genre="Pop", year=2015, label="Interscope Records"),
            Disco(id=65, title="Rare", artist="Selena Gomez", genre="Pop", year=2020, label="Interscope Records"),
            Disco(id=66, title="Revelacion", artist="Selena Gomez", genre="Latin", year=2021, label="Interscope Records"),
            Disco(id=67, title="Whatever People Say I Am, That's What I Am Not", artist="Arctic Monkeys", genre="Indie", year=2006, label="Domino Recording Company"),
            Disco(id=68, title="Who The Fuck Are Arctic Monkeys?", artist="Arctic Monkeys", genre="Indie", year=2006, label="Domino Recording Company"),
            Disco(id=69, title="Brainstorm", artist="Arctic Monkeys", genre="Indie", year=2007, label="Domino Recording Company"),
            Disco(id=70, title="Favourite Worst Nightmare", artist="Arctic Monkeys", genre="Indie", year=2007, label="Domino Recording Company"),
            Disco(id=71, title="Fluorescent Adolescent", artist="Arctic Monkeys", genre="Indie", year=2007, label="Domino Recording Company"),
            Disco(id=72, title="Teddy Picker", artist="Arctic Monkeys", genre="Indie", year=2007, label="Domino Recording Company"),
            Disco(id=73, title="Humbug", artist="Arctic Monkeys", genre="Indie", year=2009, label="Domino Recording Company"),
            Disco(id=74, title="Cornerstone", artist="Arctic Monkeys", genre="Indie", year=2009, label="Domino Recording Company"),
            Disco(id=75, title="My Propeller", artist="Arctic Monkeys", genre="Indie", year=2010, label="Domino Recording Company"),
            Disco(id=76, title="Suck It and See", artist="Arctic Monkeys", genre="Indie", year=2011, label="Domino Recording Company"),
            Disco(id=77, title="AM", artist="Arctic Monkeys", genre="Indie", year=2013, label="Domino Recording Company"),
            Disco(id=78, title="Tranquility Base Hotel & Casino", artist="Arctic Monkeys", genre="Indie", year=2018, label="Domino Recording Company"),
            Disco(id=79, title="The Car", artist="Arctic Monkeys", genre="Indie", year=2022, label="Domino Recording Company"),
            Disco(id=80, title="Aprendiendo a Aprender", artist="Carla Morrison", genre="Alternative", year=2009, label="Independent"),
            Disco(id=81, title="Mientras Tu Dormias", artist="Carla Morrison", genre="Alternative", year=2010, label="Independent"),
            Disco(id=82, title="Dejenme Llorar", artist="Carla Morrison", genre="Alternative", year=2012, label="Cosmica Records"),
            Disco(id=83, title="Jugando en Serio", artist="Carla Morrison", genre="Alternative", year=2013, label="Cosmica Records"),
            Disco(id=84, title="Amor Supremo", artist="Carla Morrison", genre="Alternative", year=2015, label="Cosmica Records"),
            Disco(id=85, title="El Renacimiento", artist="Carla Morrison", genre="Alternative", year=2022, label="Cosmica Records"),
            Disco(id=86, title="The Slow Rush", artist="Tame Impala", genre="Alternative", year=2020, label="Interscope Records"),
            Disco(id=87, title="Currents", artist="Tame Impala", genre="Alternative", year=2015, label="Interscope Records"),
            Disco(id=88, title="Lonerism", artist="Tame Impala", genre="Alternative", year=2012, label="Modular Recordings"),
            Disco(id=89, title="InnerSpeaker", artist="Tame Impala", genre="Alternative", year=2010, label="Modular Recordings"),
            Disco(id=90, title="Sentio", artist="Martin Garrix", genre="Electronic", year=2022, label="Stmpd"),
            Disco(id=91, title="Martin Garrix Presents STMPD RCRDS, Vol. 001", artist="Martin Garrix", genre="Electronic", year=2018, label="Stmpd"),
            Disco(id=92, title="2019 Remixed", artist="Martin Garrix", genre="Electronic", year=2019, label="Sony Music"),
            Disco(id=93, title="Gold Skies", artist="Martin Garrix", genre="Electronic", year=2014, label="Spinnin"),
            Disco(id=94, title="Seven", artist="Martin Garrix", genre="Electronic", year=2016, label="Sony Music"),
            Disco(id=95, title="Joytime", artist="Marshmello", genre="Electronic", year=2016, label="Joytime Collective"),
            Disco(id=96, title="Joytime II", artist="Marshmello", genre="Electronic", year=2018, label="Joytime Collective"),
            Disco(id=97, title="Joytime III", artist="Marshmello", genre="Electronic", year=2019, label="Joytime Collective"),
            Disco(id=98, title="Shockwave", artist="Marshmello", genre="Electronic", year=2021, label="Joytime Collective"),
            Disco(id=99, title="Mellokillaz", artist="Marshmello", genre="Electronic", year=2023, label="Joytime Collective"),
            Disco(id=100, title="With Hearts As One", artist="Hillsong United", genre="Christian", year=2008, label="Hillsong Music"),
            Disco(id=101, title="Of Dirt And Grace", artist="Hillsong United", genre="Christian", year=2016, label="Capitol CMG"),
            Disco(id=102, title="The White Album", artist="Hillsong United", genre="Christian", year=2014, label="Sparrow"),
            Disco(id=103, title="Everyday (Live)", artist="Hillsong United", genre="Christian", year=1999, label="Hillsong Music"),
            Disco(id=104, title="Best Friend: United Live", artist="Hillsong United", genre="Christian", year=2000, label="Hillsong Music"),
            Disco(id=105, title="King of Magesty", artist="Hillsong United", genre="Christian", year=2001, label="Hillsong Music"),
            Disco(id=106, title="To The Ends Of The Earth", artist="Hillsong United", genre="Christian", year=2002, label="Hillsong Music"),
            Disco(id=107, title="More Than Life (Live)", artist="Hillsong United", genre="Christian", year=2004, label="Hillsong Music"),
            Disco(id=108, title="Look To You", artist="Hillsong United", genre="Christian", year=2005, label="Hillsong Music"),
            Disco(id=109, title="United We Stand", artist="Hillsong United", genre="Christian", year=2006, label="Hillsong Music"),
            Disco(id=110, title="Across The Earth: Tear Down The Walls", artist="Hillsong United", genre="Christian", year=2009, label="Hillsong Music"),
            Disco(id=111, title="Live In Miami", artist="Hillsong United", genre="Christian", year=2012, label="Hillsong Music"),
            Disco(id=112, title="People (Live)", artist="Hillsong United", genre="Christian", year=2019, label="Hillsong Music"),
            Disco(id=113, title="All Of The Above", artist="Hillsong United", genre="Christian", year=2007, label="Hillsong Music"),
            Disco(id=114, title="Aftermath", artist="Hillsong United", genre="Christian", year=2011, label="EMI"),
            Disco(id=115, title="Zion", artist="Hillsong United", genre="Christian", year=2013, label="EMI"),
            Disco(id=116, title="Empires", artist="Hillsong United", genre="Christian", year=2015, label="Capitol CMG"),
            Disco(id=117, title="Wonder", artist="Hillsong United", genre="Christian", year=2017, label="Capitol CMG"),
            Disco(id=118, title="(in the meantime)", artist="Hillsong United", genre="Christian", year=2021, label="Hillsong Music"),
            Disco(id=119, title="(in the meantime) Vol. II", artist="Hillsong United", genre="Christian", year=2021, label="Hillsong Music"),
            Disco(id=120, title="Are We There Yet?", artist="Hillsong United", genre="Christian", year=2022, label="Capitol CMG"),
            Disco(id=121, title="LAS QUE NO IBAN A SALIR", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=122, title="X 100PRE", artist="Bad Bunny", genre="Latin", year=2018, label="Rimas Entertainment"),
            Disco(id=123, title="OASIS", artist="Bad Bunny", genre="Latin", year=2019, label="Universal Music"),
            Disco(id=124, title="YHLQMDLG", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=125, title="EL ULTIMO TOUR DEL MUNDO", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=126, title="Un Verano Sin Ti", artist="Bad Bunny", genre="Latin", year=2022, label="Rimas Entertainment"),
            Disco(id=127, title="Todo Es Diferente", artist="Natanael Cano", genre="Latin", year=2019, label="Hyphy Music"),
            Disco(id=128, title="Corridos Tumbados", artist="Natanael Cano", genre="Latin", year=2019, label="Rancho Humilde"),
            Disco(id=129, title="Trap Tumbado", artist="Natanael Cano", genre="Latin", year=2020, label="Rancho Humilde"),
            Disco(id=130, title="Soy El Nata", artist="Natanael Cano", genre="Latin", year=2020, label="Rancho Humilde"),
            Disco(id=131, title="Las 3 Torres", artist="Natanael Cano", genre="Latin", year=2020, label="WEA Latina"),
            Disco(id=132, title="Mi Nuevo Yo", artist="Natanael Cano", genre="Latin", year=2019, label="Rancho Humilde"),
            Disco(id=133, title="Nata", artist="Natanael Cano", genre="Latin", year=2021, label="Rancho Humilde"),
            Disco(id=134, title="A Mis 20", artist="Natanael Cano", genre="Latin", year=2021, label="WEA Latina"),
            Disco(id=135, title="NataKong", artist="Natanael Cano", genre="Latin", year=2022, label="WEA Latina"),
            Disco(id=136, title="Nata Montana", artist="Natanael Cano", genre="Latin", year=2023, label="WEA Latina"),
            Disco(id=137, title="MAÑANA SERA BONITO", artist="Karol G", genre="Latin", year=2023, label="Universal Music"),
            Disco(id=138, title="KG0516", artist="Karol G", genre="Latin", year=2021, label="Universal Music"),
            Disco(id=139, title="OCEAN", artist="Karol G", genre="Latin", year=2019, label="Universal Music"),
            Disco(id=140, title="Unstoppable", artist="Karol G", genre="Latin", year=2017, label="Universal Music"),
            Disco(id=141, title="72 Seasons", artist="Metallica", genre="Metal", year=2023, label="Blackened"),
            Disco(id=142, title="Metallica Live At Woodstck '94", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=143, title="The Metallica Blacklist", artist="Metallica", genre="Metal", year=2021, label="Blackened"),
            Disco(id=144, title="Hardwired...To Self-Destruct", artist="Metallica", genre="Metal", year=2016, label="Blackened"),
            Disco(id=145, title="Death Magnetic", artist="Metallica", genre="Metal", year=2008, label="Warner Records"),
            Disco(id=146, title="St. Anger", artist="Metallica", genre="Metal", year=2003, label="Elektra"),
            Disco(id=147, title="Reload", artist="Metallica", genre="Metal", year=1997, label="Elektra"),
            Disco(id=148, title="Load", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=149, title="Remaining Memories: The Interview", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=150, title="Live S**t: Binge & Purge", artist="Metallica", genre="Metal", year=1993, label="Elektra"),
            Disco(id=151, title="Metallica", artist="Metallica", genre="Metal", year=1991, label="Elektra"),
            Disco(id=152, title="...And Justice For All", artist="Metallica", genre="Metal", year=1988, label="Elektra"),
            Disco(id=153, title="Master of Puppets", artist="Metallica", genre="Metal", year=1986, label="Elektra"),
            Disco(id=154, title="Ride The Lightning", artist="Metallica", genre="Metal", year=1984, label="Elektra"),
            Disco(id=155, title="UTOPIA", artist="Travis Scott", genre="Hip-Hop", year=2023, label="Epic Cactus Jack"),
            Disco(id=156, title="ASTROWORLD", artist="Travis Scott", genre="Hip-Hop", year=2018, label="Epic Cactus Jack"),
            Disco(id=157, title="Huncho Jack, Jack Huncho", artist="Travis Scott", genre="Hip-Hop", year=2017, label="Capitol CMG"),
            Disco(id=158, title="Birds in the Trap Sing McKnight", artist="Travis Scott", genre="Hip-Hop", year=2016, label="Epic"),
            Disco(id=159, title="Rodeo (Expanded Edition)", artist="Travis Scott", genre="Hip-Hop", year=2015, label="Epic"),
            Disco(id=160, title="JACKBOYS", artist="Travis Scott", genre="Hip-Hop", year=2019, label="Epic"),
            Disco(id=161, title="Her Loss", artist="Drake", genre="Hip-Hop", year=2022, label="Epic"),
            Disco(id=162, title="Honestly, Nevermind", artist="Drake", genre="Hip-Hop", year=2022, label="Republic Records"),
            Disco(id=163, title="Certified Lover Boy", artist="Drake", genre="Hip-Hop", year=2021, label="Republic Records"),
            Disco(id=164, title="Scorpion", artist="Drake", genre="Hip-Hop", year=2018, label="Young Money"),
            Disco(id=165, title="More Life", artist="Drake", genre="Hip-Hop", year=2017, label="Young Money"),
            Disco(id=166, title="Views", artist="Drake", genre="Hip-Hop", year=2016, label="Young Money"),
            Disco(id=167, title="If You're Reading This It's Too Late", artist="Drake", genre="Hip-Hop", year=2015, label="Young Money"),
            Disco(id=168, title="Nothing Was The Same", artist="Drake", genre="Hip-Hop", year=2013, label="Republic Records"),
            Disco(id=169, title="Take Care (Deluxe)", artist="Drake", genre="Hip-Hop", year=2011, label="Republic Records"),
            Disco(id=170, title="Thank Me Later", artist="Drake", genre="Hip-Hop", year=2010, label="Republic Records"),
            Disco(id=171, title="Dark Lane Demo Tapes", artist="Drake", genre="Hip-Hop", year=2020, label="Republic Records"),
            Disco(id=172, title="Care Package", artist="Drake", genre="Hip-Hop", year=2019, label="Republic Records"),
            Disco(id=173, title="What a Time To Be Alive", artist="Drake", genre="Hip-Hop", year=2015, label="Young Money"),
            Disco(id=174, title="So Far Gone", artist="Drake", genre="Hip-Hop", year=2009, label="OVO"),
            Disco(id=175, title="Tarzan (Banda Sonora Original)", artist="Various Artists", genre="Soundtrack", year=1999, label="Walt Disney"),
            Disco(id=176, title="UNDERTALE Soundtrack", artist="Various Artists", genre="Soundtrack", year=2015, label="Materia Collective"),
            Disco(id=177, title="Sing 2 (Original Motion Picture Soundtrack)", artist="Various Artists", genre="Soundtrack", year=2021, label="Republic"),
            Disco(id=178, title="A Star Is Born Soundtrack", artist="Lady Gaga", genre="Soundtrack", year=2018, label="Interscope"),
            Disco(id=179, title="Euphoria (Original Score from the HBO Series)", artist="Labirinth", genre="Soundtrack", year=2019, label="Sony Music"),
            Disco(id=180, title="Love For Sale (Deluxe)", artist="Lady Gaga", genre="Jazz", year=2021, label="Interscope"),
            Disco(id=181, title="Chromatica", artist="Lady Gaga", genre="Pop", year=2020, label="Interscope"),
            Disco(id=182, title="Joanne", artist="Lady Gaga", genre="Indie", year=2016, label="Interscope"),
            Disco(id=183, title="Cheek to Cheek", artist="Lady Gaga", genre="Jazz", year=2014, label="Interscope"),
            Disco(id=184, title="ARTPOP", artist="Lady Gaga", genre="Pop", year=2013, label="Interscope"),
            Disco(id=185, title="Born this Way", artist="Lady Gaga", genre="Pop", year=2011, label="Interscope"),
            Disco(id=186, title="The Fame Monster", artist="Lady Gaga", genre="Pop", year=2009, label="Interscope"),
            Disco(id=187, title="The Fame", artist="Lady Gaga", genre="Pop", year=2008, label="Interscope"),
            Disco(id=188, title="Like a Prayer", artist="Madonna", genre="Pop", year=1989, label="Sire Records"),
            Disco(id=189, title="La La Land (Original Motion Picture Soundtrack)", artist="Various Artists", genre="Soundtrack", year=2016, label="Interscope"),
            Disco(id=190, title="Mexico And Mariachis", artist="Various Artists", genre="Soundtrack", year=2004, label="Milan Records"),
            Disco(id=191, title="Minecraft - Volume Alpha", artist="C418", genre="Soundtrack", year=2011, label="Independent"),
            Disco(id=192, title="Sonic Frontiers Original Soundtrack", artist="SEGA", genre="Soundtrack", year=2022, label="SEGA"),
            Disco(id=193, title="Mamma Mia! The Movie Soundtrack", artist="Various Artists", genre="Soundtrack", year=2008, label="Polydor Records"),
            Disco(id=194, title="Up (Original Motion Picture Soundtrack)", artist="Various Artists", genre="Soundtrack", year=2019, label="Walt Disney"),
            Disco(id=195, title="Elemental (Original Motion Picture Soundtrack)", artist="Various Artists", genre="Soundtrack", year=2023, label="Wlat Disney"),
            Disco(id=196, title="Beam Me Up Scotty", artist="Nicki Minaj", genre="Hip-Hop", year=2021, label="Young Money"),
            Disco(id=197, title="Queen", artist="Nicki Minaj", genre="Hip-Hop", year=2018, label="Republic Records"),
            Disco(id=198, title="The Pinkprint", artist="Nicki Minaj", genre="Hip-Hop", year=2014, label="Republic Records"),
            Disco(id=199, title="Pink Friday...Roman Reloaded", artist="Nicki Minaj", genre="Hip-Hop", year=2012, label="Young Money"),
            Disco(id=200, title="Pink Friday 2", artist="Nicki Minaj", genre="Hip-Hop", year=2023, label="Young Money")]

#***Get con 1 Filtro Query
@discosQuery.get("/discosclass/")
async def discosclass(id:int):
    discosfiltrados = filter (lambda disco:disco.id == id, discos_list)  #Función de orden superior
    try:
        return list(discosfiltrados)[0]
    except:
        return{"error":"No se ha encontrado el disco :("}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
 #***Get con 2 Filtros Query
@discosQuery.get("/discosclass2/")
async def discosArtistGenre(artist:str, genre:str):
    discosfiltrados=filter (lambda disco: disco.artist == artist, discos_list)#Función de orden superior
    discosfiltrados2=filter (lambda disco: disco.genre == genre, discosfiltrados)#Función de orden superior
    try:
        return list(discosfiltrados2)
    except:
        return{"error":"No se ha encontrado el disco :("}

@discosQuery.get("/discosclass3/")
async def discosArtistYear(artist:str, year:int):
    discosfiltrados=filter (lambda disco: disco.artist == artist, discos_list)#Función de orden superior
    discosfiltrados2=filter (lambda disco: disco.year == year, discosfiltrados)#Función de orden superior
    try:
        return list(discosfiltrados2)
    except:
        return{"error":"No se ha encontrado el disco :("}

@discosQuery.get("/discosclass4/")
async def discosLabelYear(label:str, year:int):
    discosfiltrados=filter (lambda disco: disco.label == label, discos_list)#Función de orden superior
    discosfiltrados2=filter (lambda disco: disco.year == year, discosfiltrados)#Función de orden superior
    try:
        return list(discosfiltrados2)
    except:
        return{"error":"No se ha encontrado el disco :("}

@discosQuery.get("/discosclass5/")  
async def discosGenreYear(genre:str, year:int):
    discosfiltrados=filter (lambda disco: disco.genre == genre, discos_list)#Función de orden superior
    discosfiltrados2=filter (lambda disco: disco.year == year, discosfiltrados)#Función de orden superior
    try:
        return list(discosfiltrados2)
    except:
        return{"error":"No se ha encontrado el disco :("}
    
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass2/?age=30&name=Juan

 # uvicorn [title_archivo]:[title_objeto] --reload