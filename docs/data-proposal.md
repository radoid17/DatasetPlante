# Dataset: Fise de ingrijire pentru plante
**Echipa:** Avramescu Isaac, Poenaru Andrei, Radoi Dragos, Vasile Marina

## 1. De ce acest dataset?

Vom face fise de ingrijire pentru plante observate in Europa. Fiecare fisa va avea informatii despre udare, lumina, sol si conditii de cultivare, cu linkuri catre sursele folosite.

Setul este destinat persoanelor care incep sa cultive plante acasa sau in gradina. Utilizatorul va putea selecta o planta si vedea o fisa scurta de ingrijire. Ghiduri de ingrijire exista deja, dar informatiile sunt raspandite in surse diferite. Contributia noastra va fi organizarea lor intr-un format comun si pastrarea provenientei fiecarui camp.

Pana acum am colectat din GBIF un esantion de 50 de observatii din Romania, cu 37 de nume distincte. Acesta ne ajuta sa selectam plante candidate, nu contine inca fise de ingrijire.

## 2. Surse

- **Observatii si selectia plantelor:** [GBIF Occurrence API](https://techdocs.gbif.org/en/openapi/v1/occurrence). Folosita deja pentru esantion, vom extinde cautarea la europa (momentan avem doar din romania). Esantionul curatat actual are 50 de randuri si aproximativ 10,5 KB. Licentele imaginilor din el sunt pastrate per rand.
- **Verificarea numelor stiintifice:** [Plants of the World Online (POWO)](https://powo.science.kew.org/). Sursa planificata pentru confirmarea numelor si a statutului taxonomic.
- **Informatii de ingrijire:** [RHS - Aloe vera](https://www.rhs.org.uk/shows-events/rhs-urban-show/houseplant-profiles/houseplants-for-sunlight) si [RHS - spinach](https://www.rhs.org.uk/vegetables/spinach/grow-your-own). Surse planificate pentru informatii despre lumina, udare si sol.
- **Imagini optionale:** [Wikimedia Commons](https://commons.wikimedia.org/). Pentru fiecare imagine folosita vom pastra autorul, pagina fisierului si licenta indicata acolo.


## 3. Date sensibile

Fisele noastre nu au nevoie de date personale.

Esantionul GBIF contine imagini cu licente CC BY-NC 4.0, CC BY 4.0 si CC0 1.0. Licenta se verifica pentru fiecare imagine inainte de reutilizare. Imaginile nu vor fi incluse fara informatiile necesare despre autor si licenta.
**Datele brute si imaginile nu vor fi incarcate pe GitHub.** Repository-ul va contine documentatia, fisele realizate de echipa si esantionul de metadate, in conditiile permise de sursa.

## 4. Schema si exemple

O inregistrare din setul final reprezinta **o fisa de ingrijire**:

| Camp | Continut |
|---|---|
| `nume_stiintific` | Numele verificat al plantei |
| `nume_comun` | Numele comun, daca este confirmat dintr-o sursa |
| `udare` | Recomandare scurta despre apa |
| `lumina` | Conditiile de lumina |
| `sol` | Tipul de sol sau substrat |
| `observatii` | Alte conditii importante pentru cultivare |
| `surse` | Linkurile care sustin informatiile din fisa |
| `image_url` | Linkul |

Informatiile care nu pot fi confirmate vor fi marcate "necunoscut". Aloe vera si spanacul de mai jos sunt doar exemple. Pentru fiecare planta selectata vom cauta si indica separat sursele care sustin recomandarile.

| nume_stiintific | udare | lumina | sol | sursa |
|---|---|---|---|---|
| Aloe vera | Udare rara, lasam substratul sa se usuce intre udari | Lumina multa, indirecta | Substrat bine drenat | RHS - Aloe vera |
| Spinacia oleracea | Udare regulata, solul nu trebuie sa se usuce | Umbrire usoara pe vreme calda | Sol fertil, care retine umezeala | RHS - spinach |

Esantionul de 50 de randuri contine observatii reale din GBIF si este folosit ca punct de plecare pentru alegerea plantelor. Nu contine recomandari de ingrijire, pentru fiecare planta din setul final vom cauta si cita separat sursele de ingrijire.

## 5. Cum vom arata ca setul este util?

Ne mai gandim.
