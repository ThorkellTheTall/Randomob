from mobs import *

from level import *

def vie(niveau, hp):


    vie = hp * niveau

    vie = round(vie)


    return vie


hpsquelette = vie (level, squelette[1])

hparcher = vie (level, archer[1])

hpbarbare = vie (level, barbare[1])

hpboss1 = vie(level, boss1[1])

hpboss2 = vie(level, boss2[1])

hpboss3 = vie(level, boss3[1])