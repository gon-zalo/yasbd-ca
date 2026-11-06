import re

from yasbd.rules.base import Rules
from yasbd.utils.trie import build_optimized_pattern


# fmt: off
class CaRules(Rules):

    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        # Social / Professional
        "sr", "sra", "srta", "dr", "dra", "llic", "pres",
        "prof", "arq", "adv", "dir. gral", "ag", "acad",
        "secr", "jtge", "jtgssa",

        # Military / Religious
        "cpt", "com", "cmdt", "tt", "subtt", "fr", "frs",
        "mn", "alm", "cnel", "col", "gral", "st", "sta",
        "sgt", "sgta", "cpl", "cpla",

        # Noble / Royal
        "a", "m", "r", "s", "excm", "excma", "il·lm", 
        "il·lma", "im", "ima",
    }

    # Case-sensitive pattern matching would cover the supress ones
    REFERENCE_ABBRVS = (Rules.REFERENCE_ABBRVS - {"no", "vols", "vol"}) | {
        "pàg", "p", "núm", "n", "dir", "t", "trad", "assoc", "aprox",
        "cf", "incl", "cia", "seg", "par", "ap", "art", "cap", "ed",
        "vol", "pròl", "cit",
    }

    CORP_ENTITY_ABBRVS = Rules.CORP_ENTITY_ABBRVS | {
        "assoc", "cia", "adm", "aj", "ajt", "bibl", "del", "soc",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Article", "Annex", "Capítol", "Secció", "Subsecció",
        "Unitat", "Mòdul", "Divisió",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS - {"ca"} | {
        "ext", "v", "veg", "c", "cró", "diag", "trav", "trv", 
        "terr", "urb", "dept", "prov", "ed", "bxs", "bda",
        "of", "av", "ctra", "pl", "bv", "b", "att", "sign", "apmt", "àt",
        "bnc", "pol. ind", "rbla", "tel", "bl", "cant", "cas",
        "cint", "com", "distr", "drec", "dta", "entl", "esc",
        "esq", "fca", "hab", "parc", "pdís", "ptge", "pg", "pcta",
        "pobl", "pta", "ptal", "pda", "ra", "ex", "ntra", "ntre"
    }

    DATE_ABBRVS = Rules.DATE_ABBRVS | {
        "gen", "febr", "abr", "jul", "ag", "set", "oct", 
        "nov", "des", "dl" , "dt" ,"dc", "dj", "dv", 
        "ds", "dg",
    }

    COMMON_SENT_STARTERS = {
        # Articles
        "El", "La", "Els", "Les", "Un", "Una", "Uns", "Unes",

        # Pronouns
        "Aquell", "Aquella", "Aquelles", "Aquells",
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
        "Pròximament", "Potser", "Realment", "Malgrat això",
        "Segon", "Segurament", "Sempre", "Simultàniament",
        "No obstant això", "Solament", "Únicament", "Subsegüentment",
        "Successivament", "També", "Tampoc", "Tard", "Tercer", 
        "Ja", "Per últim", "Últimament", "Últim", "Nogensmenys",
        "Això no obstant", "A fora", "Fora", "Res",

        # Question words
        "Com", "Com que", "Quants", "Quan", "On", "Perquè", "Per què", "Què",
    }

    # fmt: on
    @classmethod
    def _compile_regex_dynamically(cls):
        """Override base regex compilation to fix pronouns/ref abbrvs behavior."""
        super()._compile_regex_dynamically()

        # Vè./Vós.
        cls.MID_SENTENCE_FINDER_LST.extend([
            re.compile(rf"""
                \b(?i:{build_optimized_pattern({"vè", "vós"})})\.
                (?!\s+(?:{cls.COMMON_STARTERS_PATTERN})\b)
            """, re.VERBOSE),

            # (Attempt to handle) whitespace separated abbreviations (a. C., d. C.)
            re.compile(r"\b[a-z]{1}\.(?=\s[A-Z]{1}\.)"),

        ])
