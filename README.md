# HashTable

L’elaborato riportato in questa relazione consiste nell’analisi del comportamentodelle tabelle Hash con gestione delle collisioni basate su concatenamento e indirizzamento aperto. La funzione hash viene calcolata attraverso il metodo delle divisioni.

In informatica un’hash table, è una struttura dati usata per mettere in corrispondenza una data chiave con un dato valore. Viene usata per l’implementazione distrutture dati astratte associative come Map o Set. È molto utilizzata nei metodi di ricerca nominati hashing ovvero un’estensionedella ricerca indicizzata da chiavi che gestisce problemi di ricerca nei quali lechiavi di ricerca non presentano queste proprietà. Una ricerca basata su hashing è completamente diversa da una basata su confronti: invece di muoversi nellastruttura data in funzione dell’esito dei confronti tra chiavi, si cerca di accedereagli elementi nella tabella in modo diretto tramite operazioni aritmetiche chetrasformano le chiavi in indirizzi della tabella.

Esistono vari tipi di algoritmi di hashing. Per quanto affermato, in una tabella dihashing ben dimensionata il costo medio di ricerca di ogni elemento è indipen-dente dal numero di elementi. L’hashing è un problema classico dell’informatica;molti algoritmi sono stati proposti, studiati a fondo e impiegati in pratica. Duemetodi molto diffusi sono l’hashing statico e l’hashing estendibile e lineare, meto-di utilizzati anche dai programmi DBMS. Le operazioni elementare implementatein questo applicativo sono:
- inserimento
- cancellazione 
- ricerca
