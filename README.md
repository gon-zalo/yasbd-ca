# yasbd-ca
External Catalan (`ca`) support for [`yasbd-lib`](https://github.com/speedyk-005/yasbd-lib). 

The language profile was created by a native speaker and experienced translator, mainly on the basis of the (corrected) official Spanish profile, using different Catalan language resources. The test data were automatically translated from Spanish, post-edited, and adapted by the same individual.

## Install

`pip install git+https://github.com/gon-zalo/yasbd-ca.git`

## Usage

```python
from yasbd import BoundaryDetector

detector = BoundaryDetector(lang="ca", external_lang_packs=["yasbd_ca"])

# Basic punctuation
sentences = list(detector.segment("Vas veure la pel·lícula? Sí, va ser increïble. Me n'alegro."))
# ['Vas veure la pel·lícula?', 'Sí, va ser increïble.', "Me n'alegro"]

# Abbreviations
address = list(detector.segment("La casa és a la urb. Les Roses, c/ Balaguer núm. 20, bl. B, esc. esq."))
# ['La casa és a la urb. Les Roses, c/ Balaguer núm. 20, bl. B, esc. esq.']

```