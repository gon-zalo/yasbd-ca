# yasbd-ca
External Catalan (`ca`) support for yasbd-lib. 

The language profile was created by a native speaker and experienced translator, mainly on the basis of the (corrected) official Spanish profile, using different Catalan language resources. The test data were automatically translated from Spanish, post-edited and adapted by the same individual.

## Install

`pip install git+https://github.com/gon-zalo/yasbd-ca.git`

## Usage


```
from yasbd import BoundaryDetector

detector = BoundaryDetector(lang="ca", external_lang_packs=["yasbd_ca"])

sentences = list(
    detector.segment(
        "Vas veure la pel·lícula anit? Sí, va ser increïble. Em va encantar! L'actuació va ser excel·lent."
    )
)

# ['Vas veure la pel·lícula anit?', 'Sí, va ser increïble.', 'Em va encantar!', "L'actuació va ser excel·lent."]

```