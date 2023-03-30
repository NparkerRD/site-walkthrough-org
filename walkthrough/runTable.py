from walkthrough import db
from walkthrough.models import Company, Location, Site, Door, Controller, DoorBoard

# Companies
inn = Company(name="Innovacare")
ftk = Company(name="Fort Knox Storage")

# Add companies to session
db.session.add_all([inn, ftk])

# Locations - Innovacare
jax = Location(city="Jacksonville", state="Florida", company=inn)
orl = Location(city="Orlando", state="Florida", company=inn)
brd = Location(city="Bradenton", state="Florida", company=inn)
nb = Location(city="New Braunfels", state="Texas", company=inn)

# Locations - Fort Knox Storage
tlh = Location(city="Tallahassee", state="Florida", company=ftk)

# Add locations to session
db.session.add_all([jax, orl, brd, nb])

# Sites - Innovacare - Jacksonville
arl = Site(name="Arlington",
           address="6484 Fort Caroline Rd",
           zip_code="32277",
           location=jax)

nrth = Site(name="Northside",
           address="1215 Dunn Ave, Ste 1",
           zip_code="32218",
           location=jax)

flm = Site(name="Flemming Island",
           address="4565 Highway 17",
           zip_code="32003",
           location=jax)

intr = Site(name="Intracoastal",
            address="14444 Beach Blvd",
            zip_code="32250",
            location=jax)

# Sites - Innovacare - Bradenton
beim = Site(name="BEIM",
           address="8614 State Road 70 E Suite 200",
           zip_code="34202",
           location=brd)

# Sites - Innovacare - Orlando
cln = Site(name="Colonial",
           address="6336 W Colonial Dr",
           zip_code="32818",
           location=orl)


# Sites - Fort Knox Storage
capcir = Site(name="Capital Circle",
              address="2807 Capital Circle NE",
              zip_code="32308",
              location=tlh)

# Add sites to session
db.session.add_all([arl, nrth, flm, intr, beim, cln, capcir])

# Controllers - Innovacare
arlACS = Controller(name="ACS01-ARL", site=arl)
arlEXP = Controller(name="ACS01-ARL-EXP", site=arl, is_expansion=True)

nrthACS = Controller(name="ACS01-NRTH", site=nrth)
nrthEXP = Controller(name="ACS01-NRTH-EXP", site=nrth, is_expansion=True)

flmACS = Controller(name="ACS01-FLM", site=flm)
flmEXP = Controller(name="ACS01-FLM-EXP", site=flm, is_expansion=True)

intrACS = Controller(name="ACS01-INTR", site=intr)
intrEXP = Controller(name="ACS01-INTR-EXP", site=intr, is_expansion=True)

clnACS = Controller(name="ACS01-COLONIAL", site=cln)

# Controllers - Fort Knox
capcirACS = Controller(name="ACS01-CAPITAL_CIRCLE", site=capcir)

# Add controllers to session
db.session.add_all([arlACS, arlEXP, nrthACS, nrthEXP, flmACS, flmEXP, intrACS, intrEXP, capcirACS, clnACS])

# Doorboards - Arlington
arlDB1 = DoorBoard(name="DB01", controller=arlACS)
arlDB2 = DoorBoard(name="DB02", controller=arlACS)
arlDB3 = DoorBoard(name="DB03", controller=arlACS)
arlDB4 = DoorBoard(name="DB04", controller=arlACS)
arlDB5 = DoorBoard(name="DB05", controller=arlACS)
arlDB6 = DoorBoard(name="DB06", controller=arlACS)
arlDB7 = DoorBoard(name="DB07", controller=arlACS)

arlDB8 = DoorBoard(name="DB08", controller=arlEXP)
arlDB9 = DoorBoard(name="DB09", controller=arlEXP)
arlDB10 = DoorBoard(name="DB10", controller=arlEXP)
arlDB11 = DoorBoard(name="DB11", controller=arlEXP)
arlDB12 = DoorBoard(name="DB12", controller=arlEXP)
arlDB13 = DoorBoard(name="DB13", controller=arlEXP)
arlDB14 = DoorBoard(name="DB14", controller=arlEXP)
arlDB15 = DoorBoard(name="DB15", controller=arlEXP)

# Add boards to session
db.session.add_all([
    arlDB1,
    arlDB2,
    arlDB3,
    arlDB4,
    arlDB5,
    arlDB6,
    arlDB7,
    arlDB8,
    arlDB9,
    arlDB10,
    arlDB11,
    arlDB12,
    arlDB13,
    arlDB14,
    arlDB15,
])

# Doorboards - Northside
nrthDB1 = DoorBoard(name="DB01", controller=nrthACS)
nrthDB2 = DoorBoard(name="DB02", controller=nrthACS)
nrthDB3 = DoorBoard(name="DB03", controller=nrthACS)
nrthDB4 = DoorBoard(name="DB04", controller=nrthACS)
nrthDB5 = DoorBoard(name="DB05", controller=nrthACS)
nrthDB6 = DoorBoard(name="DB06", controller=nrthACS)
nrthDB7 = DoorBoard(name="DB07", controller=nrthACS)

nrthDB8 = DoorBoard(name="DB08", controller=nrthEXP)
nrthDB9 = DoorBoard(name="DB09", controller=nrthEXP)
nrthDB10 = DoorBoard(name="DB10", controller=nrthEXP)
nrthDB11 = DoorBoard(name="DB11", controller=nrthEXP)
nrthDB12 = DoorBoard(name="DB12", controller=nrthEXP)
nrthDB13 = DoorBoard(name="DB13", controller=nrthEXP)
nrthDB14 = DoorBoard(name="DB14", controller=nrthEXP)
nrthDB15 = DoorBoard(name="DB15", controller=nrthEXP)

db.session.add_all([
    nrthDB1,
    nrthDB2,
    nrthDB3,
    nrthDB4,
    nrthDB5,
    nrthDB6,
    nrthDB7,
    nrthDB8,
    nrthDB9,
    nrthDB10,
    nrthDB11,
    nrthDB12,
    nrthDB13,
    nrthDB14,
    nrthDB15,
])

# Doorboards - West Colonial
clnDB1 = DoorBoard(name="DB01", controller=clnACS)
clnDB2 = DoorBoard(name="DB02", controller=clnACS)
clnDB3 = DoorBoard(name="DB03", controller=clnACS)
clnDB4 = DoorBoard(name="DB04", controller=clnACS)
clnDB5 = DoorBoard(name="DB05", controller=clnACS)
clnDB6 = DoorBoard(name="DB06", controller=clnACS)
clnDB7 = DoorBoard(name="DB07", controller=clnACS)


db.session.add_all([clnDB1,
    clnDB2,
    clnDB3,
    clnDB4,
    clnDB5,
    clnDB6,
    clnDB7
])


# Doors - West Colonial
clnDR01 = Door(
    name="1DR-001",
    description="Storage 107",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)

clnDR02 = Door(
    name="1DR-002",
    description="Waiting Area A",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)

clnDR03 = Door(
    name="1DR-003",
    description="Waiting Area B",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)
clnDR04 = Door(
    name="1DR-004",
    description="Office 116",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)
clnDR05 = Door(
    name="1DR-005",
    description="Storage 121",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)
clnDR06 = Door(
    name="1DR-006",
    description="West Exit",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)
clnDR07 = Door(
    name="1DR-007",
    description="Janitor's Closet 122",
    has_strike=True,
    has_reader=True,
    has_rex=True,
    has_dpi=True
)

# Add doors to session
db.session.add_all([
    clnDR01, 
    clnDR02, 
    clnDR03, 
    clnDR04, 
    clnDR05, 
    clnDR06, 
    clnDR07
])

# Commit all to session
db.session.commit()