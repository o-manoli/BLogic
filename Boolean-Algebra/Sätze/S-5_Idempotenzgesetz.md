# [Idempotenz](https://de.wikipedia.org/wiki/Idempotenz)

#S-5

> Wortbildung: [Idempotenz](https://de.wiktionary.org/wiki/Idempotenz) vom [lat. idem](https://de.wiktionary.org/wiki/idem#Latein) und bedeutet dasselbe. #Etymologie

## Idempotenzgsetz der Konjunktion

$A \cdot A = A$ #S-5K

### Beweis S-5K

$A \cdot A = A \cdot A + 0$  #A-3

$A \cdot A + 0 = A \cdot A + A \cdot \bar A$  #A-4

$A \cdot A + A \cdot \bar A = A \cdot (A + \bar A)$  #A-2

$A \cdot (A + \bar A) = A \cdot 1$  #A-4

$A \cdot 1 = A$  #A-3

---

## Idempotenzgsetz der Disjunktion

$A + A = A$ #S-5D

### Beweis S-5D

$A + A = (A + A) \cdot 1$  #A-3

$(A + A) \cdot 1 = (A + A) \cdot (A + \bar A)$  #A-4

$(A +  A) \cdot (A + \bar A) = A + A \cdot \bar A$  #A-2

$A + A \cdot \bar A = A + 0$  #A-4

$A + 0 = A$  #A-3

---

## Questionable-Proof

### Im Bezug auf der Konjunktion

```math
\begin{equation}
  A \land A = A \tag{\#S-5K}
\end{equation}
```

```math
\begin{equation}
  A \land A = (A \lor 0) \land (A \lor 0) \tag{\#A-3}
\end{equation}
```

```math
\begin{equation}
  (A \lor 0) \land (A \lor 0) = A \lor (0 \land 0) \tag{\#A-2}
\end{equation}
```

> Hier liegt das Problem! $0 \land 0 = 0$ ist noch nicht ganz bewiesen!
>
> Aber $A \land 0 = 0$ ist eigentlich das Dominanzgesetz #S-6K

```math
\begin{equation}
  A \lor (0 \land 0) = A \lor 0 = A \tag{\#A-3}
\end{equation}
```

### Im Bezug auf der Disjunktion

```math
\begin{equation}
  A \lor A = A \tag{\#S-5D}
\end{equation}
```

```math
\begin{equation}
  A \lor A = (A \land 1) \lor (A \land 1) \tag{\#A-3}
\end{equation}
```

```math
\begin{equation}
  (A \land 1) \lor (A \land 1) = A \land (1 \lor 1) \tag{\#A-2}
\end{equation}
```

```math
\begin{equation}
  A \land (1 \lor 1) = A \land 1 \tag{\#S-6D}
\end{equation}
```

```math
\begin{equation}
  A \land 1 = A \tag{\#A-3}
\end{equation}
```

