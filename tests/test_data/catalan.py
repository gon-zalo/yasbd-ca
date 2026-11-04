ISO_CODE = "ca"
TEST_DATA = [
    # Basic punctuation
    "Hola, món.| Com estàs?| Bé, gràcies.",
    "Com et dius?| Em dic Carlos.",
    "Vas veure la pel·lícula anit?| Sí, va ser increïble.| Em va encantar!| L'actuació va ser excel·lent.",

    # Abbreviations
    "El Sr. García va arribar ahir.| La Sra. López també.",
    "La Prof. María va donar una conferència.",
    "El Llic. Pérez i el Jtge. Torres són amics.",
    "El Sr. José i la Sra. María són els amos.",
    "El Cmdt. Rodríguez va saludar el Col. Díaz.",
    "Vegeu la pàg. 55 del llibre.",
    "Vegeu el cap. 3 en el t. II de l'obra.",
    "L'art. 4 i el núm. 8 són clau.",
    "Es va demanar als nens que llegissin els par. 5 i 6 de l'art. 4 de la constitució.",
    "Consulteu el par. 5 per a més informació.",
    "Truca al dir. gral. al tel. 555-1234.",
    "Truca al tel. 555-0199.",
    "Vaig comprar pa, llet, etc. per al sopar.",
    "La temperatura del motor va arribar als 120,5 °C.| Afortunadament, el sistema va continuar funcionant.",
    "La ruta fa 10 km.| Després comença el sender.",
    "Llegiu, p. ex., el capítol 5",
    "Ahir li vaig dir que no.| 5 persones van arribar després.",
    "Ho deixo entre nosaltres.| 3 persones ho saben.",
    "El corredor núm. 103 va arribar 4t.",
    "El tren s'atura.| 5 passatgers se'n baixen.",
    "La reunió és el dl. 15 de gener.",
    "Va néixer el 5 d'abr. de 1990.",
    "La comunió és el dg. 20 de març.",
    "L'empresa Rodríguez i Cia. va signar el contracte juntament amb l'Assoc. Internacional de Comerç.",
    "Treballa a l'Assoc.| Demà en té una reunió.",

    # structural headings
    "Capítol 1. El començament.| Era fosc a fora. | Res no es movia.",
    "Part II. Introducció.| El sistema comença aquí. | Segueix la inicialització.",
    "L'informe s'ha completat.| Capítol 3. Anàlisi de resultats.",

    # Addresses & Locations
    "Jo vaig veure un ocell.| L'has vist també?", # esto fuera, no?
    "Viu a l'av. Diagonal.",
    "Viuen al c. Major, 12.",
    "L'accident va ser a la ctra. 50 amb el c. 100.",
    "Gira a la trav. 3 i segueix per la diag. 5.",
    "La casa és a la urb. Les Roses, c/ Balaguer núm. 20, bl. B, esc. esq.", # ¿?

    # Common Starters after abbreviations
    "Va arribar el Sr. Afortunadament va portar el paquet.",
    "Vaig anar a la ctra. per veure la desfilada.",
    "Va arribar el Sr. García.| Com que no hi era, va marxar.",

    # Parentheses and quotes
    "El problema —¿i qui ho havia de dir?— es va resoldre ràpidament.",
    "La decisió —increïblement difícil!— ho va canviar tot.",
    "Ell va dir (No estic llest.) durant la reunió.",
    "Ell va preguntar: Estàs llest?| Vaig respondre que sí.",
    """Ella va dir: "No n'estic segura."| Després va marxar.""",

    # Pronoun heuristic (Ud./Vd.)
    "Em dirigeixo a Vè. Marco, per saludar-lo.",
    "Em dirigeixo a Vè.| Demà li enviaré el paquet.",
    "Els ho vaig donar a Vè.| Ells ho van confirmar.",
    "Vaig preguntar per Vè.| Malauradament no hi eren.",
    "Em dirigeixo a Vè.| Quan m'enviarà el paquet?",
    "Espero que Vè. comprengui el problema.",

    # Ellipsis
    "El projecte estava gairebé acabat... però vam trobar un problema.",
]