# Zusammenfassung: Informationstheorie und die optimale Wordle-Strategie

## I. Einleitung und Quantifizierung der Unsicherheit

Das Ziel des Vortrags ist es, die **Informationstheorie** – eine universelle Methode zur Quantifizierung von Unsicherheit – anhand des populären Spiels Wordle zu erklären.

### 1.1 Die Herausforderung
Wordle erfordert das Erraten eines geheimen Fünf-Buchstaben-Wortes in maximal sechs Versuchen. Das Feedback (Grau, Gelb, Grün) liefert Informationen darüber, wie der Raum der möglichen Antworten eingeschränkt werden kann. Anfängliche, intuitive Strategien, die auf Buchstabenhäufigkeit basieren (z. B. 'other' oder 'weary'), sind nicht systematisch genug, um die *optimale* Vermutung zu finden.

### 1.2 Information und das Bit (M10.1: Logarithmus)
Information wird danach gemessen, wie stark eine Beobachtung den Raum der Möglichkeiten **reduziert**.

*   **Definition Bit:** Eine Beobachtung, die den Möglichkeitsraum halbiert, enthält **1 Bit** an Information. Eine Reduktion um den Faktor $4$ entspricht $2$ Bits, eine Reduktion um den Faktor $8$ entspricht $3$ Bits.
*   **Logarithmische Formel:** Die Information ($I$) wird durch den Logarithmus zur Basis 2 der Kehrwahrscheinlichkeit $(1/P)$ ausgedrückt:
    $$I = \log_2 \left(\frac{1}{P}\right) = - \log_2 (P)$$
    Diese Formel entspricht der Frage, wie oft man die Menge der Möglichkeiten halbieren müsste.
*   **Vorteil der Logarithmen:** Während Wahrscheinlichkeiten sich multiplizieren, **addieren** sich Bits, was die Berechnung von Informationsmengen vereinfacht.
*   **Informationsgehalt:** **Unwahrscheinliche Ereignisse** (z. B. ein seltenes Farbmuster, das nur 58 Wörter übrig lässt) sind **hoch informativ**, während wahrscheinliche Muster (meist Grau) wenig Information liefern.

## II. Entropie: Der Erwartungswert

### 2.1 Definition der Entropie
Um die Qualität einer Vermutung objektiv zu bewerten, wird die **Entropie ($H$)** verwendet, welche die **erwartete Menge an Information** darstellt, die man von der Verteilung aller möglichen Farbmuster erhält.

*   **Berechnung (M10.2: Erwartungswert):** Die Entropie ist der gewichtete Durchschnitt aller möglichen Farbmuster: Die Wahrscheinlichkeit jedes Musters wird mit dem Informationsgehalt dieses Musters multipliziert.
*   **Interpretation:** Die Entropie misst die **Gleichmäßigkeit (Flachheit) der Musterverteilung** und die Gesamtanzahl der verbleibenden Möglichkeiten.
*   **Vergleich:** Eine Vermutung wie 'Slate' (5.8 Bit erwartet) ist besser als 'Weary' (4.9 Bit erwartet), da 'Slate' zu einer flacheren (gleichmäßigeren) Verteilung der möglichen Folgemuster führt.
*   **Namensgebung:** Der Begriff "Entropie" wurde von John von Neumann vorgeschlagen, da er bereits in der statistischen Mechanik verwendet wurde und dadurch einen Debattenvorteil verschaffte, da "niemand weiß, was Entropie wirklich ist".

### 2.2 Modellierung der Plausibilität (M10.2: Simulation)
Der naive Bot, der lediglich die Entropie maximiert, erreicht einen Durchschnitt von $\approx 4.124$ Zügen. Um dies zu verbessern, muss die **Worthäufigkeit** berücksichtigt werden, da der Bot obskure Wörter als gleich wahrscheinlich ansieht wie gebräuchliche.

*   **Verfeinerte Wahrscheinlichkeit:** Externe Worthäufigkeitsdaten (z. B. Google Books Ngram) werden genutzt, um zu modellieren, wie wahrscheinlich ein Wort die endgültige Antwort ist.
*   **Sigmoidfunktion:** Zur Modellierung der Plausibilität wird eine Sigmoidfunktion verwendet, die eine Abgrenzung zwischen sehr wahrscheinlichen und sehr unwahrscheinlichen Wörtern schafft und so obskuren Wörtern eine sehr geringe Wahrscheinlichkeit zuweist (z. B. 1 zu 1000).

## III. Algorithmen und die optimale Lösung

### 3.1 Die Metrik des Erwarteten Endergebnisses
Im späteren Spielverlauf reicht die reine Maximierung der Information (Entropie) nicht aus. Die verbesserte Strategie zielt auf die **Minimierung des erwarteten Endergebnisses** des gesamten Spiels ab.

*   **Erwartungswert:** Die erwartete Endpunktzahl wird berechnet, indem die verbleibende Unsicherheit (Entropie in Bits nach einer Vermutung) mittels einer **Funktion $f$** mit der durchschnittlich benötigten Anzahl an *zusätzlichen* Zügen verknüpft wird.
*   **Kalibrierung:** Diese Funktion $f$ wird durch **Regression** an Simulationsdaten aus früheren Spieldurchläufen angepasst.
*   **Leistung:** Mit dieser Metrik erreicht der Algorithmus (Version 2.0) einen Durchschnitt von $\approx 3.6$ Zügen.

### 3.2 Korrigierte Bestleistung und theoretische Grenze
Das anfängliche Ergebnis zur besten Eröffnung (Crane) enthielt einen kleinen Fehler in der Codierung der Farbzuweisung bei doppelten Buchstaben. Die finale, korrigierte Analyse, die **schamlos** die offizielle Wordle-Antwortliste in die Modellierung einbezieht, ergab eine höhere theoretische Bestleistung.

*   **Technisch Optimaler Zug:** Die Simulation, welche die niedrigste durchschnittliche Punktzahl erzielt, kommt auf **Salé** (eine alternative Schreibweise für einen mittelalterlichen Helm).
*   **Praktische Alternativen:** **Trace** und **Crate** erbringen eine nahezu identische Leistung und haben den Vorteil, als offensichtlich gebräuchliche Wörter selbst mögliche Antworten zu sein.
*   **Die Theoretische Grenze:** Die absolut beste erreichbare Leistung liegt bei $\approx 3.43$. Dies liegt daran, dass der anfängliche Unsicherheitsraum von ca. 11 Bits nach den ersten beiden optimalen Zügen nur auf $\approx 1$ Bit reduziert werden kann. Da 1 Bit Unsicherheit im Wesentlichen zwei verbleibende Möglichkeiten bedeutet, kann die Antwort im dritten Zug nicht fehlerfrei garantiert werden, wodurch der Durchschnitt nicht auf 3 gesenkt werden kann.

### 3.3 Fazit für den menschlichen Spieler
Obwohl diese Algorithmen die theoretische Grenze der Leistung zeigen, ist die gefundene technisch beste Lösung ("Salé") wahrscheinlich nicht die beste für menschliche Spieler. Menschen verlassen sich auf Intuition und haben die offizielle Wortliste nicht auswendig gelernt. Das Ziel der Übung ist das Verständnis der Informationstheorie, nicht das ruinieren des Spiels.