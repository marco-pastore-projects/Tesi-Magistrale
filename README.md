# Tesi Magistrale in Scienze Statistiche ed Economiche (CLAMSES)
# Confronto tra Modelli GARCH e Reti Neurali nella Previsione della Matrice di Varianza-Covarianza dei Titoli Azionari

Descrizione del progetto
Questo progetto è parte di una tesi magistrale in ambito econometrico-finanziario e ha l'obiettivo di confrontare la capacità previsiva delle matrici di varianza-covarianza future dei rendimenti azionari, utilizzando due approcci metodologici distinti:

Modelli GARCH multivariati

Reti Neurali (Deep Learning)

L'analisi si concentra sui titoli azionari che hanno fatto parte ininterrottamente dell’indice MIB 30 (oggi FTSE MIB) dal 2008 ad oggi, garantendo così una coerenza temporale e una base dati stabile.

Obiettivi principali
Costruzione e stima delle matrici di varianza-covarianza con modelli econometrici GARCH (es. DCC-GARCH).

Progettazione e addestramento di modelli di rete neurale per la previsione delle stesse matrici.

Valutazione e confronto della performance previsiva dei due approcci tramite metriche quantitative (es. Frobenius norm, log-likelihood out-of-sample, errori di previsione su portafogli simulati, ecc.).

Analisi della robustezza dei modelli in differenti contesti di volatilità (crisi finanziaria, ripresa, shock macroeconomici, ecc.).

Struttura del repository
data/ – Dataset utilizzati (o script per la loro raccolta)

notebooks/ – Notebook Jupyter con le fasi di preprocessing, modellazione e analisi

models/ – Implementazioni dei modelli GARCH e delle reti neurali

results/ – Risultati delle simulazioni e delle valutazioni

utils/ – Funzioni di supporto (metriche, gestione dei dati, visualizzazione)

README.md – Questa descrizione del progetto

Tecnologie utilizzate
Python (NumPy, Pandas, SciPy)

Statsmodels, Arch, yFinance

TensorFlow / PyTorch per le reti neurali

Matplotlib / Seaborn per la visualizzazione

Jupyter Notebook

Git per il versionamento

Note
Il progetto ha finalità accademiche e si inserisce in un percorso di approfondimento metodologico sull’utilizzo di tecniche di machine learning in ambito finanziario, confrontandole con approcci statistici tradizionali.
