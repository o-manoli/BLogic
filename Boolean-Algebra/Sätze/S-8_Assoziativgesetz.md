# [Assoziativgesetz](https://de.wikipedia.org/wiki/Assoziativgesetz)

#S-8

> lat. associare "vereinigen, verbinden, verknüpfen, vernetzen"   #Etymologie

## Konjunktion-Form

$A \cdot (B \cdot C) = (A \cdot B) \cdot C$ #S-8K

### Beweis S-8K

$A \cdot (B \cdot C) = A \cdot (B \cdot C) + 0$ #A-3

$A \cdot (B \cdot C) + 0 = A \cdot (B \cdot C) + A \cdot \bar A$ #A-4

- I:

$A \cdot (B \cdot C) + A \cdot \bar A = ((A \cdot (B \cdot C)) + A) \cdot ((A \cdot (B \cdot C)) + \bar A)$ #A-2

- Exkurs-I_I:

$(A \cdot (B \cdot C)) + A = A$ #S-7

$A = A \cdot (A + C)$ #S-7

$A \cdot (A + C) = (A + A \cdot B) \cdot (A + C)$ #S-7

$(A + A \cdot B) \cdot (A + C) = A + ((A \cdot B) \cdot C)$ #A-2

- Exkurs-I_II:

$(A \cdot (B \cdot C)) + \bar A = \bar A + (A \cdot (B \cdot C))$ #A-1

$\bar A + (A \cdot (B \cdot C)) = (\bar A + A) \cdot (\bar A + B \cdot C)$ #A-2

$(\bar A + A) \cdot (\bar A + B \cdot C) = 1 \cdot (\bar A + B \cdot C)$ #A-4

$1 \cdot (\bar A + B \cdot C) = \bar A + B \cdot C$ #A-3

$\bar A + B \cdot C = (\bar A + B) \cdot (\bar A + C)$ #A-2

$(\bar A + B) \cdot (\bar A + C) = (1 \cdot (\bar A + B)) \cdot (\bar A + C)$ #A-3

$(1 \cdot (\bar A + B)) \cdot (\bar A + C) = ((\bar A + A) \cdot (\bar A + B)) \cdot (\bar A + C)$ #A-4

$((\bar A + A) \cdot (\bar A + B)) \cdot (\bar A + C) = (\bar A + (A \cdot B)) \cdot (\bar A + C)$ #A-2

$(\bar A + (A \cdot B)) \cdot (\bar A + C) = \bar A + ((A \cdot B) \cdot C)$ #A-2

- In I einsetzen:

$((A \cdot (B \cdot C)) + A) \cdot ((A \cdot (B \cdot C)) + \bar A) = (A + ((A \cdot B) \cdot C)) \cdot (\bar A + ((A \cdot B) \cdot C))$

$(A + ((A \cdot B) \cdot C)) \cdot (\bar A + ((A \cdot B) \cdot C)) = A \cdot \bar A +  (A \cdot B) \cdot C$ #A-2

$A \cdot \bar A + (A \cdot B) \cdot C = 0 + (A \cdot B) \cdot C$ #A-4

$0 + (A \cdot B) \cdot C = (A \cdot B) \cdot C$ #A-3

## Disjunktion-Form

$A + (B + C) = (A + B) + C$ #S-8D

### Beweis S-8D

$A + (B + C) = (A + (B + C)) \cdot 1$ #A-3

$(A + (B + C)) \cdot 1 = (A + (B + C)) \cdot (A + \bar A)$ #A-4

- II:

$(A + (B + C)) \cdot (A + \bar A) = ((A + (B + C)) \cdot A) + ((A + (B + C)) \cdot \bar A)$ #A-2

- Exkurs-II_I:

$(A + (B + C)) \cdot A = A$ #S-7

$A = A \cdot (A + C)$ #S-7

$A \cdot (A + C) = (A \cdot (A + B)) \cdot (A + C)$ #S-7

$(A \cdot (A + B)) \cdot (A + C) = A \cdot ((A + B) + C)$ #A-2


- Exkurs-II_II:

$(A + (B + C)) \cdot \bar A = (\bar A \cdot (B + C)) + (\bar A \cdot A)$ #A-2

$(\bar A \cdot (B + C)) + (\bar A \cdot A) = (\bar A \cdot (B + C)) + 0$ #A-4

$(\bar A \cdot (B + C)) + 0 = \bar A \cdot (B + C)$ #A-3

$\bar A \cdot (B + C) = (\bar A \cdot B) + (\bar A \cdot C)$ #A-2

$(\bar A \cdot B) + (\bar A \cdot C) = (0 + \bar A \cdot B) + (\bar A \cdot C)$ #A-3

$(0 + \bar A \cdot B) + (\bar A \cdot C) = (\bar A \cdot A + \bar A \cdot B) + (\bar A \cdot C)$ #A-4

$(\bar A \cdot A + \bar A \cdot B) + (\bar A \cdot C) = (\bar A \cdot (A + B)) + (\bar A \cdot C)$ #A-2

$(\bar A \cdot (A + B)) + (\bar A \cdot C) = \bar A \cdot ((A + B) + C)$ #A-2

- In II einsetzen:

$((A + (B + C)) \cdot A) + ((A + (B + C)) \cdot \bar A) = (A \cdot ((A + B) + C)) + (\bar A \cdot ((A + B) + C))$

$(A \cdot ((A + B) + C)) + (\bar A \cdot ((A + B) + C)) = (A + \bar A) \cdot ((A + B) + C)$ #A-2

$(A + \bar A) \cdot ((A + B) + C) = 1 \cdot ((A + B) + C)$ #A-4

$1 \cdot ((A + B) + C) = (A + B) + C$ #A-3

