# Game Development - startcode

Deze repository hoort bij het lesboek en werkboek **Game Development**.
Iedere les heeft een **eigen map**. Open steeds `lesN/main.py` van de les waar je
mee bezig bent. De opdrachten laten je de bestaande game onderzoeken en zelf
kleine onderdelen veranderen. Een volgende lesmap begint opnieuw met haar eigen
startgame: wijzigingen uit een vorige les worden niet automatisch meegenomen.

## Leerlinggegevens

Naam:
Klas:

## Starten in Codespaces

1. Wacht tot de installatie in de terminal klaar is.
2. Open bijvoorbeeld `les1/main.py` en klik op **Play** rechtsboven in VS Code.
3. Open onderin **Poorten** de poort **6080 (Gamevenster / GUI)**. Daar staat
   het Pygame-venster op de virtuele desktop. Klik in het gamevenster voordat je
   de pijltjestoetsen of spatiebalk gebruikt.
4. Stop de game met het kruisje van het Pygame-venster of met Ctrl+C in de
   terminal. Start daarna desgewenst de volgende `lesN/main.py`.

Verschijnt de game niet? Kijk of de Python-installatie klaar is, of de juiste
lesmap openstaat, of het programma nog draait en of je poort **6080** bekijkt.
In les 1 staan de stappen uitgebreider in het werkboek.

## Bestanden per les

| Map | Startgame | Wat vul je zelf aan? |
| --- | --- | --- |
| `les1` | speler beweegt naar rechts, sterren | overige richtingen, snelheid, sprint |
| `les2` | twee munten | derde instantie, eigen waarde per munt |
| `les3` | gewone en achtervolgende vijand | gedrag en `FastEnemy` |
| `les4` | munt werkt, vijand herkent botsing | schade, verwijderen, `take_damage()` |
| `les5` | wapen, kogels, vijanden, speler met healthbar | wapeneigenschappen en eigen uitbreiding |
| `les6` | kleine werkende arena | zelfgekozen beperkte uitbreiding |

De bestandsindeling groeit mee met de omvang van de game:

| Les | Waar vind je de lescode? |
| --- | --- |
| 1 | `main.py`: speler, sterren en game samen |
| 2 | `main.py`: game; `objects.py`: speler en munt |
| 3 | `main.py`: starten; `game.py`: objecten plaatsen; `actors.py`: speler en vijanden |
| 4 | `game.py`: spelwereld; `actors.py`: speler en vijand; `items.py`: munt |
| 5 | `game.py`: spelwereld; `player.py` en `enemy.py`: figuren; `combat.py`: wapen en kogel; `hud.py`: healthbar |
| 6 | als les 5, met een extra `coin.py` en een achtervolgende vijand |

Vanaf les 3 is `main.py` alleen nog het startpunt. Een object toevoegen doe je
in `game.py`; het gedrag wijzig je in het bestand van die groep.

`game_core.py` is in elke map dezelfde gedocumenteerde basis. Die bevat
`GameObject` en `Game`, met beweging, botsing, update, draw en de game loop.
Begin bij `main.py` en volg de imports naar de class die je voor de opdracht
nodig hebt. Zoek in `game_core.py` op wat een methode doet als je dat wilt
weten. Dit is ook een startpunt voor het latere
**aparte gameproject**, maar dat project krijgt zijn eigen ontwerp en beoordeling.

## Vormen later door afbeeldingen vervangen

Bij de objectclass of in `game.py`/`main.py` staat een commentaarregel **VERVANG DOOR PLAATJE**.
Zet bijvoorbeeld `player.png` in `les5/assets/` en wijzig:

```python
# VERVANG DOOR PLAATJE: image = load_image("player.png", (36, 36))
super().__init__(None, x, y, width=36, height=36, color=(115, 211, 255))
```

in:

```python
image = load_image("player.png", (36, 36))
super().__init__(image, x, y, width=36, height=36, color=(115, 211, 255))
```

Ook bij een ontbrekend bestand blijft de vorm zichtbaar: `load_image()` geeft
dan `None` terug. Een afbeelding met transparante achtergrond werkt het best.
Pas de grootte in de aanroep aan de gewenste afmetingen aan. Zie per les het
commentaar voor de namen van munt, vijand, kogel en ster.

## Samenwerken (Les A)

Oefen Git in je eigen repository. Werk eerst individueel een kleine branch af,
commit en synchroniseer, controleer de pull request, merge en werk `main` bij.
Voor het keurmerk Teamplayer laat je dit zelfstandig zien vóór of in les 6.
Deze repository bevat geen AI-extensies of ingebouwde AI-functies.
