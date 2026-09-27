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
| `les5` | magiër, wapen, vuurballen en vijanden | wapeneigenschappen en eigen uitbreiding |
| `les6` | kleine werkende arena | zelfgekozen beperkte uitbreiding |

De bestandsindeling groeit mee met de omvang van de game:

| Les | Waar vind je de lescode? |
| --- | --- |
| 1 | `main.py`: speler, sterren en game samen |
| 2 | `main.py`: game; `objects.py`: speler en munt |
| 3 | `main.py`: gameclass, objecten plaatsen en starten; `actors.py`: speler en vijanden |
| 4 | `main.py`: spelwereld en starten; `actors.py`: speler en vijand; `items.py`: munt |
| 5 | `main.py`: spelwereld en starten; `player.py` en `enemy.py`: figuren; `combat.py`: wapen en vuurbol; `hud.py`: healthbar |
| 6 | `main.py`: arena en starten; verder als les 5, met extra `coin.py` en een achtervolgende vijand |

In iedere les staat de class die van `Game` erft in `main.py`. Daar worden
objecten gemaakt en wordt de game gestart. Het gedrag van de speler, vijanden
en andere objecten staat vanaf les 3 in bestanden per onderwerp.

`game_core.py` is in elke map dezelfde gedocumenteerde basis. Die bevat
`GameObject` en `Game`, met beweging, botsing, update, draw en de game loop.
Begin bij `main.py` en volg de imports naar de class die je voor de opdracht
nodig hebt. Zoek in `game_core.py` op wat een methode doet als je dat wilt
weten. Dit is ook een startpunt voor het latere
**aparte gameproject**, maar dat project krijgt zijn eigen ontwerp en beoordeling.

## Gedeelde sprites

Alle zes lessen gebruiken de enige map `assets/` in de hoofdmap van de repository.
Je hoeft afbeeldingen niet naar een lesmap te kopiëren. `load_image("naam.png", (breedte, hoogte))`
zoekt vanuit elk lesbestand automatisch in die gedeelde map. De startgames laden
meteen afbeeldingen; als een afbeelding ontbreekt, verschijnt een gekleurde vorm.

| Rol in de lessen | Bestand in `assets/` |
| --- | --- |
| Speler (les 1 t/m 4) | `warriorman_voor.png` |
| Magiër (les 5 en 6) | `mageheroman_voor.png` |
| Ster (les 1) | `ster.png` |
| Munt (les 2, 4 en 6) | `gold_coin.png` |
| Vijand (les 3 t/m 6) | `ratman_voor.png` |
| Vuurbol (les 5 en 6) | `blue_fire_small.png` |

De map bevat daarnaast varianten van de personages voor achter, links en rechts,
andere personages, een zilveren munt, magieprojectielen en achtergronden. De namen
`warriorman` en `warriorwoman` zijn bewust gecorrigeerd; gebruik de exacte
bestandsnamen. De vuurballen in de startgame gaan alleen naar rechts. Een andere
richting of animatie toevoegen is een mogelijke uitbreiding, geen vereiste
voor het starten van de lessen.

## Achtergronden

`Game` tekent de achtergrond vóór de objecten en de HUD. Les 1 tot en met 4
gebruiken `assets/field.png`, les 5 gebruikt `assets/grotto.png` en les 6
gebruikt `assets/dungeon.png`. `load_image()` schaalt de achtergrond naar het
spelvenster. Het veld komt uit `game_core.py`; les 5 en 6 kiezen hun eigen
achtergrond in `main.py`. Bij een ontbrekend bestand gebruikt de game een
effen achtergrondkleur.

## Geluiden

De geluiden staan in `assets/audio/`. `fire_magic.mp3` past bij een vuuraanval en kan door leerlingen zelf
aan het schieten worden gekoppeld. `arrow_shoot.mp3` is beschikbaar voor
een eigen boogschutter; `forest_ambience.mp3`, `cave_ambience.mp3` en
`dungeon_ambience.mp3` zijn sfeer voor een eigen level. Geen van de geluiden
speelt in de startcode vanzelf af: zelf koppelen blijft een uitbreiding.
In [`assets/audio/README.md`](assets/audio/README.md) staan de bronvermeldingen,
de oorspronkelijke bestandsnamen en een opmerking over de lengte van de geluiden.
Neem die bronvermeldingen ook over als je het spel verder verspreidt.

## Samenwerken (Les A)

Oefen Git in je eigen repository. Werk eerst individueel een kleine branch af,
commit en synchroniseer, controleer de pull request, merge en werk `main` bij.
Voor het keurmerk Teamplayer laat je dit zelfstandig zien vóór of in les 6.
Deze repository bevat geen AI-extensies of ingebouwde AI-functies.
