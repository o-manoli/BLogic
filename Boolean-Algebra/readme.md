# Einführung in die boolesche Algebra

# Grundfunktionen

## Inversion

Negation aka `NOT-Gate`

- LaTeX `\neg` or just a `\bar`

|  $A$  | $\bar A$ |
| :---: | :------: |
| True  |  False   |
| False |   True   |

## [Konjunktion](<https://de.wikipedia.org/wiki/Konjunktion_(Logik)>)

> lat. `coniungere` verbinden. Ausschließend.   #Etymologie

`AND-Gate`

- $\land$ **u**nd, weil es **u**nten offen ist.
- LaTeX `\land` or `\cdot` für $\cdot$

|  $A$  |  $B$  | $A \land B$ |
| :---: | :---: | :---------: |
| True  | True  |    True     |
| True  | False |    False    |
| False | True  |    False    |
| False | False |    False    |

## [Disjunktion](https://de.wikipedia.org/wiki/Disjunktion)

> lat. `disiungere` trennen. Nicht-Ausschließend    #Etymologie

`OR-Gate`

- $\lor$ **o**der, weil es **o**ben offen ist.
- LaTeX `\lor` or `+`

`coniungere-disiungere` <-> `connect-disconnect`

|  $A$  |  $B$  | $A \lor B$ |
| :---: | :---: | :--------: |
| True  | True  |    True    |
| True  | False |    True    |
| False | True  |    True    |
| False | False |   False    |

# Axiome

Es gibt **vier** Axiome der booleschen. Mit jeweils zwei Sätze.

Axiome brauchen keine Beweise. Sie sind einfach da, damit man darauf bauen kann.

Einmal für die [Konjunktion-Verknüpfung.](#Konjunktion) `UND-Gatter`
Und einmal für das [Disjunktion-Verknüpfung](#Disjunktion). `ODER-Gatter`

Beiden seiten der Gleichung sind miteinander Äquivalent.
Das heißt, dass man die eine Seite immer mit der Anderen vertauschen kann.
**THAT WORKS BOTH WAYS!!**

Ich muss gestehen, dass ist mir nicht sofort eingefallen!

---

## [Kommutativgesetz](https://de.wikipedia.org/wiki/Kommutativgesetz)   #A-1

> lat. `commutare` vertauschen.

1. $A \cdot B = B \cdot A$ #A-1K

2. $A + B = B + A$ #A-1D

## [Distributivgesetz](https://de.wikipedia.org/wiki/Distributivgesetz)   #A-2

> lat. `distribuere` verteilen.

1. $A \cdot (B + C) = A \cdot B + A \cdot C$ #A-2K

2. $A + B \cdot C = (A + B) \cdot (A + C)$ #A-2D

## [Neutrales Element](https://de.wikipedia.org/wiki/Neutrales_Element)   #A-3

1. $A \cdot 1 = A$ #A-3K

2. $A + 0 = A$ #A-3D

## [Inverses Element](https://de.wikipedia.org/wiki/Inverses_Element)   #A-4

1. $A \cdot \bar A = 0$ #A-4K

2. $A + \bar A = 1$ #A-4D

---

# Summary

|             Konjunktion-Form              |            Disjunktion-Form             |
| :---------------------------------------: | :-------------------------------------: |
|          $A \cdot B = B \cdot A$          |             $A + B = B + A$             |
| $A \cdot (B + C) = A \cdot B + A \cdot C$ | $A + B \cdot C = (A + B) \cdot (A + C)$ |
|              $A \cdot 1 = A$              |               $A + 0 = A$               |
|           $A \cdot \bar A = 0$            |            $A + \bar A = 1$             |

## Axiome

### [Kommutativgesetz](./Axiome/A-1_Kommutativgesetz.md) #A-1

### [Distributivgesetz](./Axiome/A-2_Distributivgesetz.md) #A-2

### [Neutrales Element](./Axiome/A-3_Neutrales_Element.md) #A-3

### [Inverses Element](./Axiome/A-4_Inverses_Element.md) #A-4

## Sätze

### [Idempotenzgsetz](./Sätze/S-5_Idempotenzgesetz.md) #S-5

### [Dominanzgesetz](./Sätze/S-6_Dominanzgesetz.md) #S-6

### [Absorptionsgesetz](./Sätze/S-7_Absorptionsgesetz.md) #S-7

### [Assoziativgesetz](./Sätze/S-8_Assoziativgesetz.md) #S-8

### [Doppelte Negation](./Sätze/S-9_Doppelte-Negation.md) #S-9

### [De Morgans Gesetz](./Sätze/S-10_De_Morgans_Gesetz.md) #S-10

### [The One Gate: NAND](./Sätze/S-0_NAND.md) #S-0

