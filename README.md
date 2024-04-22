FaceBook's __dyn encrypts a list of javascript module numbers available in the page html, there is also the __rsc parameter which works with the same logic.

!! `dyn.fixed.py` works now (only tested for `__dyn`)
I am working on reversing __rsc as it changed and I cannot reproduce the result when fetching modules from html.

Dyn is located in [G3Nm7rYDpD0.js](https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/G3Nm7rYDpD0.js%3F_nc_x=Ij3Wp8lg5Kz) on [meta.ai](meta.ai)
It is called by `CSRBitmap`, referring to `__csr` but encrypts `__dyn` aswell

<img width="506" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/bb86887a-7d66-418d-a57b-2934c984f88c">

<img width="610" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/5b7c2891-3e7f-44e4-ba5b-991e6afe507b">
<img width="695" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/911add94-08c9-4c3c-9bf4-d0955993eee0">

here `"BootloaderEndpointConfig"` number 5094 is added/set.
callstack: 

<img width="280" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/9c78877a-fd34-420a-8ad7-34252bf0c484">



Module numbers are set:  
<img width="550" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/c3aea258-540e-4835-a56b-84ac71106cbd">

then their value is equated to 1 in a list where the module number is the index. This list is then transformed to binary and encrypted/hashed.

On other sites look for `toCompressedString`.

<img width="564" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/af848816-0688-4d46-ad9f-3765ee504575">

A simple `console.log` statement here can console log the arrays used to encrypt.

Better scripts and documentation to come soon, a function to extract module numbers is available in `dyn.py`
the algorithm in .py is not working right, refer to `dyn.js`.

<img width="1142" alt="image" src="https://github.com/xtekky/FaceBook-Dyn/assets/98614666/4e9475e6-6ba9-4a60-8b48-394d20ac6a92">

dyn.py (for __dyn)

```
7xeUmwlEnwn8K2Wmh0cm5U4e0yoW3q32360CEbo19oe8hw2nVE4W0om0MU2awpUO0n24o5-0Bo7O2l0Fwqo31w9O0H8-U2zxe2Gew9O22362W2K0zK1swa-7U1bobodEGdw46wbS1LwTwNw4mwr86Dwlo18ouwKxvzUgw000C7yu
```

from meta.ai 

```
7xeUmwlEnwn8K2Wmh0cm5U4e0yoW3q32360CEbo19oe8hw2nVE4W0om0MU2awpUO0n24o5-0Bo7O2l0Fwqo31w9O0H8-U2zxe2Gew9O22362W2K0zK1swa-7U88138bodEGdw46wbS1LwTwNw4mwr86Dwlo18ouwKxvzUgw
```

`000C7yu` is added in py, probably because of some inaccuracy.

dyn.py (with module extraction) for `__rsc`

```
gTdLExd2pbGiK00qz0gbwBga8gw46wEzi1i0oO3RwzgrFet2F6aw6boS1jwr41Iw2vQ0a2wnm1fix6ce1zg0009wuU2
```

dyn.js

```
gTdLExd2pbGiK00qz0gbwBga8gw46wEzi1i0oO3RwzgrFet2F6aw6boS1jwr41Iw2vQ0a2wnm1fix6ce1zg
```

the ending bytes differ somehow, I am not sure why that Is so.

__dyn module list 

```
[
    7,
    27,
    31,
    54,
    141,
    165,
    258,
    270,
    317,
    323,
    328,
    329,
    527,
    551,
    619,
    757,
    772,
    827,
    876,
    926,
    1081,
    1127,
    1421,
    1478,
    1496,
    2104,
    2111,
    2190,
    2580,
    2776,
    2915,
    3019,
    3032,
    3401,
    3419,
    3515,
    3665,
    3790,
    3828,
    3829,
    3871,
    3977,
    4171,
    4328,
    4501,
    4517,
    4521,
    4685,
    4705,
    4748,
    4763,
    4920,
    4953,
    5003,
    5050,
    5094,
    5237,
    5239,
    5332,
    5508,
    5540,
    5573,
    5842,
    5888,
    5943,
    5954,
    5968,
    6231,
    6421,
    6533,
    6589,
    6639,
    6918,
    7027,
    7133,
    7135,
    7221,
    7511,
    7542,
    7589,
    7613,
    7615,
    7631,
    7648
]
```

(search for these in html to understand where these numbers are comming from)

module list for __rsc

```
[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    37,
    39,
    42,
    46,
    47,
    54,
    55,
    56,
    62,
    67,
    76,
    82,
    88,
    93,
    100,
    27468,
    27472,
    27473,
    27474,
    27475,
    27476,
    27478,
    27479,
    27480,
    27481,
    27482,
    27483,
    27484,
    27560,
    27589,
    27590,
    27594,
    27595,
    27596,
    27597,
    27598,
    27599,
    27600,
    27601,
    27602,
    27603,
    27604,
    27605,
    27606,
    27607,
    27609,
    27611,
    27612,
    27613,
    27614,
    27615,
    27616,
    27617,
    27618,
    27619,
    27620,
    27621,
    27622,
    27623,
    27624,
    27625,
    27628,
    27707,
    27708,
    27790,
    27811,
    27812,
    27813,
    27818,
    27819,
    27821,
    27822,
    27823,
    27970,
    27972,
    27973,
    27974,
    27975,
    27976,
    27980,
    27981,
    28032,
    28192,
    28193,
    28202,
    28285,
    28286,
    28287,
    28288,
    28289,
    28290,
    28291,
    28294,
    28312,
    28313,
    28319,
    28325,
    28326,
    28334,
    28336,
    28337,
    28338,
    28355,
    28375,
    28391,
    28392,
    28394,
    28396,
    28397,
    28398,
    28399,
    28400,
    28401,
    28403,
    28404,
    28405,
    28406,
    28407,
    28408,
    28409,
    28410,
    28411,
    28412,
    28413,
    28414,
    28415,
    28416,
    28417,
    28418,
    28419,
    28420,
    28421,
    28423,
    28425,
    28433,
    28463,
    28599,
    28603,
    28615,
    28908,
    28910,
    28911,
    28912,
    28921,
    28922,
    28923,
    28924,
    28925,
    28926,
    28929,
    28937,
    28938,
    28949,
    28955,
    28956,
    30577,
    30578,
    30579,
    30655,
    30657,
    30658,
    30665,
    30673,
    30695
]
```
