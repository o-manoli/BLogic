# [De Morgans Gesetz](https://de.wikipedia.org/wiki/De-morgansche_Gesetze)

#S-10


## Konjunktion-Form

$\overline{A \cdot B} = \bar A + \bar B$

### Beweis S-10K

$\overline{A \cdot B} = \overline{(A \cdot B) \cdot 1}$ #A-3

$\overline{(A \cdot B) \cdot 1} = \overline{(A \cdot B) \cdot ((\bar A + \bar B) + \overline{\bar A + \bar B})}$ #A-4

$\overline{(A \cdot B) \cdot ((\bar A + \bar B) + \overline{\bar A + \bar B})} = \overline{((A \cdot B) \cdot (\bar A + \bar B)) + ((A \cdot B) \cdot \overline{\bar A + \bar B})}$ #A-2

$\overline{((A \cdot B) \cdot (\bar A + \bar B)) + ((A \cdot B) \cdot \overline{\bar A + \bar B})} = \overline{( (A \cdot B \cdot \bar A) + (A \cdot B \cdot \bar B) ) + ((A \cdot B) \cdot \overline{\bar A + \bar B})}$ #A-2

$\overline{((A \cdot B \cdot \bar A) + (A \cdot B \cdot \bar B)) + ((A \cdot B) \cdot \overline{\bar A + \bar B})} = \overline{( 0 + 0 ) + ((A \cdot B) \cdot \overline{\bar A + \bar B})}$ #A-4

$\overline{(0 + 0 ) + ((A \cdot B) \cdot \overline{\bar A + \bar B})} = \overline{0 + ((A \cdot B) \cdot \overline{\bar A + \bar B})}$ #A-3

$\overline{0 + ((A \cdot B) \cdot \overline{\bar A + \bar B})} = \overline{((\bar A + \bar B) \cdot \overline{\bar A + \bar B}) + ((A \cdot B) \cdot \overline{\bar A + \bar B})}$ #A-4

$\overline{((\bar A + \bar B) \cdot \overline{\bar A + \bar B}) + ((A \cdot B) \cdot \overline{\bar A + \bar B})} = \overline{\overline{\bar A + \bar B} \cdot ( (\bar A + \bar B) + (A \cdot B))}$ #A-2

$\overline{\overline{\bar A + \bar B} \cdot ( (\bar A + \bar B) + (A \cdot B))} = \overline{\overline{\bar A + \bar B} \cdot ( (\bar A + \bar B + A) \cdot (\bar A + \bar B + B))}$ #A-2

$\overline{\overline{\bar A + \bar B} \cdot ( (\bar A + \bar B + A) \cdot (\bar A + \bar B + B))} = \overline{\overline{\bar A + \bar B} \cdot (1 \cdot 1)}$ #A-4

$\overline{\overline{\bar A + \bar B} \cdot (1 \cdot 1)} = \overline{\overline{\bar A + \bar B}}$ #A-3

$\overline{\overline{\bar A + \bar B}} = \bar A + \bar B$

## Disjunktion-Form

$\overline{A + B} = \bar A \cdot \bar B$

### Beweis S-10D

$\overline{A + B} = \overline{(A + B) + 0}$ #A-3

$\overline{(A + B) + 0} = \overline{(A + B) + ((\bar A \cdot \bar B) \cdot \overline{\bar A \cdot \bar B})}$ #A-4

$\overline{(A + B) + ((\bar A \cdot \bar B) \cdot \overline{\bar A \cdot \bar B})} = \overline{((A + B) + (\bar A \cdot \bar B)) \cdot ((A + B) + \overline{\bar A \cdot \bar B})}$ #A-2

$\overline{((A + B) + (\bar A \cdot \bar B)) \cdot ((A + B) + \overline{\bar A \cdot \bar B})} = \overline{((A + B + \bar A) \cdot (A + B + \bar B)) \cdot ((A + B) + \overline{\bar A \cdot \bar B})}$ #A-2

$\overline{((A + B + \bar A) \cdot (A + B + \bar B)) \cdot ((A + B) + \overline{\bar A \cdot \bar B})}= \overline{(1 \cdot 1) \cdot ((A + B) + \overline{\bar A \cdot \bar B})}$ #A-4

$\overline{(1 \cdot 1) \cdot ((A + B) + \overline{\bar A \cdot \bar B})} = \overline{1 \cdot ((A + B) + \overline{\bar A \cdot \bar B})}$ #A-3

$\overline{1 \cdot ((A + B) + \overline{\bar A \cdot \bar B})} = \overline{((\bar A \cdot \bar B) + \overline{\bar A \cdot \bar B}) \cdot ((A + B) + \overline{\bar A \cdot \bar B})}$ #A-4

$\overline{((\bar A \cdot \bar B) + \overline{\bar A \cdot \bar B}) \cdot ((A + B) + \overline{\bar A \cdot \bar B})} = \overline{\overline{\bar A \cdot \bar B} + ((\bar A \cdot \bar B) \cdot (A + B))}$ #A-2

$\overline{\overline{\bar A \cdot \bar B} + ((\bar A \cdot \bar B) \cdot (A + B))} = \overline{\overline{\bar A \cdot \bar B} + ((\bar A \cdot \bar B \cdot A) + (\bar A \cdot \bar B \cdot B))}$ #A-2

$\overline{\overline{\bar A \cdot \bar B} + ((\bar A \cdot \bar B \cdot A) + (\bar A \cdot \bar B \cdot B))} = \overline{\overline{\bar A \cdot \bar B} + (0 + 0)}$ #A-4

$\overline{\overline{\bar A \cdot \bar B} + (0 + 0)} = \overline{\overline{\bar A \cdot \bar B}}$ #A-3

$\overline{\overline{\bar A \cdot \bar B}} = \bar A \cdot \bar B$ #S-9

