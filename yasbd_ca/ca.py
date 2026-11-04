import re

from yasbd.rules.base import Rules
from yasbd.utils.trie import build_optimized_pattern


# fmt: off
class CaRules(Rules):

    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        # Social / Professional
        "sr", "sra", "srta", "dr", "dra", "llic", "pres",
        "prof", "arq", "adv", "dir. gral", "ag", "acad",
        "secr", "jtge", "jtgssa"

        # Military / Religious
        "cpt", "com", "cmdt", "tt", "subtt", "fr", "frs",
        "mn", "alm", "cnel", "col", "gral", "st", "sta",
        "sgt", "sgta", "cpl", "cpla"

        # Noble / Royal
        "s. m", "s. a. r", "s. a. s", "s. s", "s. a",
        "s. e", "v. e", "s. a. s. r", "a", "m", "r", "s", 
        "excm", "excma", "il·lm", "il·lma", "im", "ima",
    }

    # Case-sensitive pattern matching would cover the supress ones
    REFERENCE_ABBRVS = (Rules.REFERENCE_ABBRVS - {"no", "vols", "vol"}) | {
        "pàg", "p", "núm", "n", "dir", "t", "trad", "assoc", "aprox",
        "cf", "incl", "cia", "seg", "par", "ap", "art", "cap", "ed",
        "trad", "vol", "pròl", "ap", "cit",
    }

    CORP_ENTITY_ABBRVS = Rules.CORP_ENTITY_ABBRVS | {
        "assoc", "cia", "adm", "aj", "ajt", "bibl", "s. coop",
        "del", "s. a", "s. l", "soc",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Article", "Annex", "Capítol", "Secció", "Subsecció",
        "Unitat", "Mòdul", "Divisió",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS - {"ca"} | {
        "ext", "v", "veg", "c", "cró", "diag", "trav", "trv", 
        "terr", "urb", "dept", "prov", "t. m", "ed", "bxs", "bda",
        "of", "av", "ctra", "pl", "bv", "b", "ap. de corr", "s/àt",
        "d. c", "att", "sign", "c. p", "ntra. sra", "apmt", "àt",
        "bnc", "p. d", "pol. ind", "rbla", "tel", "bl", "cant", "cas",
        "cint", "com", "distr", "drec", "dta", "entl", "esc",
        "esq", "fca", "hab", "parc", "pdís", "ptge", "pg", "pcta",
        "pobl", "pta", "ptal", "pda", "ra", "ex", "p. ex"
        # "s/n"
    }

    DATE_ABBRVS = Rules.DATE_ABBRVS | {
        "gen", "febgen", "abr", "jul", "ag", "set", "oct", 
        "nov", "des", "dl" , "dt" ,"dc", "dj", "dv", 
        "ds", "dg",
    }

    COMMON_SENT_STARTERS = {
        # Articles
        "El", "La", "Els", "Les", "Un", "Una", "Uns", "Unes",

        # Pronouns
        "Allí", "Aquell", "Aquella", "Aquelles", "Aquells",
        "Aquí", "Quin", "Quins", "Quant", "Ella", "Elles",
        "Ells", "Aquesta", "Aquestes", "Aquest", "Aquests",
        "Nosaltres", "Qui", "Tu", "Vós", "Vostè", "Vostès",
        "Vosaltres", "Jo", "Ell", "Allà",

        # Adverbs & Transitions
        "Actualment", "A més", "Afortunadament", "Ara",
        "Anit", "Anit passada", "Anteriorment", "Abans", "Antigament",
        "Així que", "Així doncs", "De manera que", "Tot i que", 
        "Encara que", "Ni que", "Ahir", "Encara", "Quasi",
        "Conseqüentement", "Després", "Llavors", "Aleshores",
        "Finalment", "Generalment", "Avui", "Inclús", "Inmediatament",
        "Mai", "Malauradament", "Tot seguit", "De seguida", "Aviat",
        "Per tant", "Tant bon punt", "Demà", "Millor", "Tanmateix",
        "Menys", "Mentrestant", "Mentre", "Més", "Normalment",
        "Tant de bo", "Pitjor", "Però", "Posteriorment",
        "Prèviament", "Primerament", "Primer", "Probablement",
        "Pròximament", "Potser", "Realment", "Malgrat això"
        "Segon", "Segurament", "Sempre", "Simultàniament",
        "No obstant això", "Solament", "Únicament", "Subsegüentment",
        "Successivament", "També", "Tampoc", "Tard", "Tercer", 
        "Ja", "Per últim", "Últimament", "Últim", "Nogensmenys",
        "Això no obstant", "A fora", "Fora", "Res",

        # Question words
        "Com", "Com que", "Quins", "Quants", "Quan", "Quin", 
        "Quant", "On", "Perquè", "Per què", "Qui", "Què"
    }

    # fmt: on
    @classmethod
    def _compile_regex_dynamically(cls):
        """Override base regex compilation to fix pronouns/ref abbrvs behavior."""
        super()._compile_regex_dynamically()


        # Ud./Uds./Vd./Vds. heuristic
        # Don't split if the next word is NOT a common starter (assumes it's a proper name).
        # Resolves the ambiguity "Ud. Marco" vs "Ud. Mañana".
        cls.MID_SENTENCE_FINDER_LST.extend([
            re.compile(rf"""
                \b(?i:{build_optimized_pattern({"vè", "vós"})})\.
                (?!\s+(?:{cls.COMMON_STARTERS_PATTERN})\b)
            """, re.X),

            # Dotted geographic pairs with optional whitespace (EE. UU., EE.UU., FF. AA.)
            # Only protect the first pair so a following sentence still splits.
            re.compile(r"\b[A-Z]{2}\.(?=\s*[A-Z]{1,2}\.)"),

            # In Spanish/Portuguese, these reference abbreviationsare are case-sensitve.
            # re.compile(r"(?:Nos?|Para)\.(?=\s*(\d+|\w))")
        ])