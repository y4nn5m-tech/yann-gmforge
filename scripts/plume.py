#!/usr/bin/env python3
"""
plume.py — faire qu'une écriture manuscrite n'ait pas l'air d'une police.

    from plume import ecrire, FILTRES

    html += FILTRES                       # une fois, dans le <body>
    note = ecrire("Suffisant. Classer.", graine=4)          # au stylo
    note = ecrire("Je note, c'est tout.", graine=7, encre=True)   # à la plume

Le défaut de Caveat n'est pas la forme de ses lettres : c'est que **le
troisième `e` d'une phrase est exactement le premier**. Une main ne
répète jamais, et l'œil le voit tout de suite — même sans savoir quoi
regarder.

Trois traitements, qui se cumulent :

    lettre à lettre   chaque caractère prend sa propre inclinaison, sa
                      hauteur, son échelle et son encrage. **C'est le
                      gain principal** : la répétition disparaît
    l'ondulation      un filtre déforme le tracé — la ligne n'est plus
                      droite, les jambages tremblent
    l'encre mangée    une seconde turbulence ronge le trait par
                      endroits, comme une plume qui accroche

`encre=False` s'arrête à l'ondulation : le rendu d'un stylo, pour une
note jetée vite. `encre=True` ajoute la morsure : une plume, pour un
document qu'on a pris le temps d'écrire.

**Tout est déterministe.** La graine est fixe, donc deux générations
donnent la même écriture au caractère près — comme le reste des
accessoires.

Ce que ça ne corrige pas : l'épaisseur du trait reste constante, là où
une plume fait des pleins et des déliés ; et les lettres ne se
raccordent pas entre elles comme dans une cursive tracée d'un geste. Il
faudrait vectoriser chaque lettre, ce qui n'en vaut pas le prix.
"""
import random
import re

FILTRES = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
 <filter id="plume" x="-5%" y="-20%" width="110%" height="140%">
   <feTurbulence type="fractalNoise" baseFrequency="0.035 0.12" numOctaves="3" seed="7"
                 result="n"/>
   <feDisplacementMap in="SourceGraphic" in2="n" scale="1.6"
                      xChannelSelector="R" yChannelSelector="G"/>
 </filter>
 <filter id="plume-encre" x="-5%" y="-20%" width="110%" height="140%">
   <feTurbulence type="fractalNoise" baseFrequency="0.035 0.12" numOctaves="3" seed="7"
                 result="n"/>
   <feDisplacementMap in="SourceGraphic" in2="n" scale="1.6"
                      xChannelSelector="R" yChannelSelector="G" result="d"/>
   <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="19" result="t"/>
   <feColorMatrix in="t" type="matrix"
     values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  .9 0 0 0 -.25" result="m"/>
   <feComposite in="d" in2="m" operator="out"/>
 </filter>
</svg>
"""

# On découpe le texte en balises et en morceaux de texte : une balise ne
# se tremble pas, et un `<br>` doit rester entier.
_MORCEAUX = re.compile(r"(<[^>]+>|&[a-zA-Z]+;|&#\d+;)")


def ecrire(texte, graine=0, encre=False, amplitude=1.0):
    """Le texte, caractère par caractère, sous le filtre qui convient.

    `amplitude` resserre ou élargit le tremblé — en dessous de 1 pour
    une main appliquée, au-dessus pour une main pressée.
    """
    r = random.Random(graine)
    out = []
    for part in _MORCEAUX.split(texte):
        if not part:
            continue
        if _MORCEAUX.fullmatch(part):
            out.append(part)
            continue
        # Les mots d'abord, les lettres ensuite. Chaque caractère est un
        # inline-block, et sans cette enveloppe le navigateur coupe une
        # ligne entre deux lettres du même mot. Tout blanc du source —
        # retour à la ligne compris — redevient une espace, sans quoi on
        # obtient « ressourcesminières ».
        for mot in part.split():
            lettres = []
            for ch in mot:
                a = r.uniform(-3.4, 3.4) * amplitude
                dy = r.uniform(-0.5, 0.5) * amplitude
                s = r.uniform(0.955, 1.05)
                o = r.uniform(0.82, 1.0)
                lettres.append(
                    f'<span style="display:inline-block;'
                    f"transform:rotate({a:.1f}deg) translateY({dy:.2f}px) scale({s:.3f});"
                    f'opacity:{o:.2f}">{ch}</span>')
            out.append(f'<span style="display:inline-block">{"".join(lettres)}</span> ')
    f = "plume-encre" if encre else "plume"
    return f'<span style="filter:url(#{f})">{"".join(out)}</span>'
