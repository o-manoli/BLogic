# Not And

#S-0

## Definition

$\overline{A \land B} = A \otimes B$

|  $A$  |  $B$  | $A \land B$ | $\overline{A \land B}$ |
| :---: | :---: | :---------: | :--------------------: |
| True  | True  |    True     |         False          |
| True  | False |    False    |          True          |
| False | True  |    False    |          True          |
| False | False |    False    |          True          |

One Gate to rule them all.

Alle Grundfunktion kann man nur mit dem `NAND-Gatter` umsetzten.

$\bar A = \text{Some Function Of Only NANDS}(A)$

$A \land B = \text{Some Function Of Only NANDS}(A, B)$

$A \lor B = \text{Some Function Of Only NANDS}(A, B)$

## Negation

$\bar A = \text{Some Function Of Only NANDS}(A)$ #S-0_Neg

### Beweis

$\bar A = \overline{A \cdot A}$ #S-5

$\overline{A \cdot A} = A \otimes A$

## Konjunktion

$A \land B = \text{Some Function Of Only NANDS}(A, B)$

### Beweis

$A \cdot B = \overline{\overline{A \cdot B}}$ #S-9

$\overline{\overline{A \cdot B}} = \overline{A \otimes B}$

$\overline{A \otimes B} = (A \otimes B) \otimes (A \otimes B)$ #S-0_Neg

## Disjunktion

$A \lor B = \text{Some Function Of Only NANDS}(A, B)$

### Beweis

$A \lor B = \overline{\overline{A \lor B }}$ #S-9

$\overline{\overline{A \lor B }} = \overline{\bar A \land \bar B}$ #S-10

$\overline{\bar A \land \bar B} = \bar A \otimes \bar B$

$\bar A \otimes \bar B = (A \otimes A) \otimes (B \otimes B)$ #S-0_Neg
