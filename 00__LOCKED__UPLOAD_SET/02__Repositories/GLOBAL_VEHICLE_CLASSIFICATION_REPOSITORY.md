# GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
STATUS: Frozen
LAYER: SOURCE OF TRUTH
RUNTIME: YES (Knowledge Upload Candidate)

Purpose:
Single source of truth for:
- Vehicle class buckets (VCB)
- Model → VCB mapping
- Alias normalization (many → one)
- Unmapped model handling (flag-only, no silent assignment)
Non-goals:
- No pricing values
- No sales logic
- No phrasing scripts
- No assumptions about customer intent

---


## 1) VCB DEFINITIONS (LOCKED)

VCB_1 — Hatchback / Small Sedan (small surface area)
Examples (non-exhaustive): Yaris, Corolla, Civic (sedan), Mazda 3

VCB_2 — Sedan / Compact SUV / CUV (medium surface area)
Examples (non-exhaustive): Camry, Accord, Altima, CX-5, RAV4, CR-V, Jetour T2, Haval H6

VCB_3 — Large Sedan / SUV / Pickup / Luxury (large surface area)
Examples (non-exhaustive): Patrol, Land Cruiser, Tahoe, Defender, large pickups, full-size luxury SUVs

Rule:
- These VCB definitions are based on practical coverage/surface area, not customer lifestyle labels.

---

## 2) CANONICAL MODEL NAMES (LOCKED FORMAT)

Rule:
- Canonical format: BRAND + MODEL (as commonly searched)
- If trim matters (rare), use: BRAND + MODEL + TRIM

Example canonical:
- Jetour T2
- Haval H6
- Toyota Land Cruiser
- Nissan Patrol
---
## 3) MODEL → VCB MAPPING (EDITABLE LIST)

Alignment rule for converting your old sheet → VCB mapping:

KEEP (only what VCB needs):
- Make (Brand)
- Model (and Trim/Series only when it changes segment/size, e.g., LC200 vs LC300, Patrol Y62, LX570 vs LX600)
- Vehicle segment (body type / market segment)
- VCB (one of our 3 pricing segments, driven by size + segment + work complexity)

REMOVE (not part of VCB mapping):
- All pricing columns (PPF/Ceramic/Polishing prices)
- Age bands (Brand New / 1–3 / 3–5 / 2015+)
- Any “size tier” labels like S/M/L or “Urban Compact / Flagship” unless they directly map to VCB
- Any PPF-specific complexity multipliers / adjustments (keep those in service pricing logic, not in SOURCE OF TRUTH)
- Any duplicated “Category” fields that are just marketing labels (Luxury/EV/Mixed) unless it helps identify segment

Decision basis (VCB assignment):
- Vehicle size class (small/compact/mid/full-size) inferred from model
- Segment/body type (sedan, SUV, pickup, coupe, van)
- Typical panel area + install time (SUV/pickup/full-size higher)
- SNASH pricing model: only 3 buckets (VCB1 / VCB2 / VCB3) — no micro-tiers here

### 3.1 VCB_1 MODELS
- BYD Dolphin
- Changan Alsvin
- Changan Eado
- Changan UNI-V
- Chery Arrizo 5
- Chery Arrizo 6
- Chevrolet Aveo
- Chevrolet Cruze
- Chevrolet Spark
- Citroen C-Elysee
- Citroen C3
- Citroen C4
- Dodge Neon
- Fiat 500
- Fiat Panda
- Fiat Tipo
- Ford Fiesta
- Ford Focus
- Ford Fusion
- Geely Emgrand
- Honda City
- Honda Civic
- Hyundai Accent
- Hyundai Azera
- Hyundai Elantra
- Hyundai i20
- Kia Cerato
- Kia K5
- Kia Picanto
- Kia Rio
- Kia Stinger
- Mazda Mazda 2
- Mazda Mazda 3
- Mitsubishi Attrage
- Mitsubishi Lancer EX
- Nissan Micra
- Nissan Sentra
- Nissan Sunny
- Opel Astra
- Opel Corsa
- Peugeot 208
- Peugeot 301
- Peugeot 308
- Peugeot 408
- Renault Fluence
- Renault Megane
- Renault Symbol
- Renault Talisman
- SEAT Ibiza
- SEAT Leon
- SEAT Toledo
- Skoda Fabia
- Skoda Scala
- Suzuki Baleno
- Suzuki Ciaz
- Suzuki Dzire
- Suzuki Swift
- Toyota Avalon
- Toyota Corolla
- Toyota Crown
- Toyota Yaris
- Toyota Yaris Sedan
- Volkswagen Golf
- Volkswagen Jetta
- Volkswagen Passat
- Volkswagen Polo
- Volvo S60
- Volvo V60

### 3.2 VCB_2 MODELS
- Acura ILX
- Acura Integra
- Acura RDX
- Acura TLX
- Alfa Romeo Giulia
- Alfa Romeo Giulietta
- Alfa Romeo Stelvio
- Audi A3
- Audi A4
- Audi A5
- Audi A6
- Audi Q2
- Audi Q3
- Audi Q4 e-tron
- Audi Q5
- Audi TT
- Audi e-tron
- Audi e-tron GT
- BMW 1 Series
- BMW 2 Series
- BMW 3 Series
- BMW 4 Series
- BMW 5 Series
- BMW X1
- BMW X2
- BMW X3
- BMW i4
- BMW iX1
- BYD Atto 3
- BYD Seal
- BYD Song Plus
- Cadillac ATS
- Cadillac CT4
- Cadillac CT5
- Cadillac CTS
- Cadillac XTS
- Changan CS35 Plus
- Changan CS55 Plus
- Changan CS75
- Changan CS85
- Changan CS95
- Changan Hunter
- Changan UNI-K
- Changan UNI-T
- Chery Tiggo 2
- Chery Tiggo 4
- Chery Tiggo 7
- Chery Tiggo 8
- Chery Tiggo 8 Pro
- Chery Tiggo 9
- Chevrolet Blazer
- Chevrolet Camaro
- Chevrolet Colorado
- Chevrolet Corvette
- Chevrolet Equinox
- Chevrolet Impala
- Chevrolet Malibu
- Chevrolet Trailblazer
- Chevrolet Trax
- Chrysler 300
- Chrysler Grand Voyager
- Chrysler Pacifica
- Citroen Berlingo
- Citroen C3 Aircross
- Citroen C4 Cactus
- Citroen C5
- Citroen C5 Aircross
- Dodge Challenger
- Dodge Charger
- Dodge Durango
- Fiat 500X
- Ford Bronco Sport
- Ford EcoSport
- Ford Edge
- Ford Escape
- Ford Everest
- Ford Explorer
- Ford Mustang
- Ford Ranger
- Ford Taurus
- Ford Tourneo
- GAC Aion S
- GAC Aion Y
- GAC EMKOO
- GAC EMZOOM
- GAC GA4
- GAC GA6
- GAC GS3
- GAC GS4
- GAC GS5
- GMC Acadia
- GMC Terrain
- GWM (Great Wall) Poer
- GWM (Great Wall) Tank 300
- GWM (Great Wall) Tank 500
- Geely Coolray
- Geely Geometry C
- Geely Monjaro
- Geely Okavango
- Geely Tugella
- Genesis G70
- Genesis G80
- Haval H6
- Haval H6 GT
- Haval H9
- Haval Jolion
- Honda Accord
- Honda CR-V
- Honda HR-V
- Honda Odyssey
- Honda Pilot
- Honda ZR-V
- Hongqi H5
- Hongqi H7
- Hongqi H9
- Hongqi HQ9
- Hyundai Bayon
- Hyundai Creta
- Hyundai H-1
- Hyundai Ioniq 5
- Hyundai Ioniq 6
- Hyundai Kona
- Hyundai Kona Electric
- Hyundai Santa Fe
- Hyundai Stargazer
- Hyundai Tucson
- Hyundai Venue
- Infiniti Q30
- Infiniti Q50
- Infiniti Q70
- JAC J7
- JAC S3
- JAC S4
- JAC S5
- JAC S7
- JAC T8
- JAC T9
- Jaguar E-Pace
- Jaguar XE
- Jaguar XF
- Jeep Cherokee
- Jeep Compass
- Jeep Grand Cherokee
- Jeep Renegade
- Jeep Wrangler
- Jetour Dashing
- Jetour X70
- Jetour X70 Plus
- Jetour X90
- Kia Carens
- Kia Cerato
- Kia EV6
- Kia EV9
- Kia Niro EV
- Kia Seltos
- Kia Sonet
- Kia Sorento
- Kia Sportage
- Land Rover Discovery Sport
- Land Rover Range Rover Evoque
- Lexus ES
- Lexus GS
- Lexus IS
- Lexus NX
- Lexus RX
- Lexus UX
- MG 3
- MG 5
- MG 6
- MG GT
- MG HS
- MG One
- MG RX5
- MG RX8
- MG ZS
- MINI Cooper 3-Door
- MINI Cooper 5-Door
- MINI Cooper Clubman
- MINI Cooper Convertible
- MINI Cooper Countryman
- Maserati Ghibli
- Maserati Quattroporte
- Mazda CX-3
- Mazda CX-30
- Mazda CX-5
- Mazda CX-50
- Mazda CX-8
- Mazda CX-9
- Mazda CX-90
- Mazda Mazda 6
- Mercedes-Benz A-Class
- Mercedes-Benz C-Class
- Mercedes-Benz CLA
- Mercedes-Benz CLS
- Mercedes-Benz E-Class
- Mercedes-Benz EQA
- Mercedes-Benz EQB
- Mercedes-Benz EQC
- Mercedes-Benz EQE
- Mitsubishi ASX
- Mitsubishi Eclipse Cross
- Mitsubishi L200
- Mitsubishi L300
- Mitsubishi Montero Sport
- Mitsubishi Outlander
- Mitsubishi Pajero (Classic)
- Nissan Altima
- Nissan Juke
- Nissan Kicks
- Nissan Maxima
- Nissan Navara
- Nissan Pathfinder
- Nissan Qashqai
- Nissan Titan
- Nissan X-Trail
- Nissan Z
- Omoda/Jaecoo Jaecoo 7
- Omoda/Jaecoo Omoda 5
- Opel Grandland
- Opel Insignia
- Opel Mokka
- Peugeot 2008
- Peugeot 3008
- Peugeot 5008
- Peugeot 508
- Peugeot Boxer
- Peugeot Rifter
- Peugeot Traveller
- Porsche Macan
- Renault Captur
- Renault Duster
- Renault Kadjar
- Renault Koleos
- SEAT Arona
- SEAT Ateca
- SEAT Tarraco
- Skoda Kamiq
- Skoda Karoq
- Skoda Kodiaq
- Skoda Octavia
- Skoda Superb
- Subaru Forester
- Subaru Impreza
- Subaru Legacy
- Subaru Outback
- Subaru WRX
- Subaru XV (Crosstrek)
- Suzuki Ertiga
- Suzuki Jimny
- Suzuki Vitara
- Suzuki XL6
- Tesla Model 3
- Tesla Model Y
- Toyota Avanza
- Toyota C-HR
- Toyota Camry
- Toyota Corolla Cross
- Toyota Fortuner
- Toyota Hilux
- Toyota Innova
- Toyota RAV4
- Toyota Raize
- Toyota Rush
- Toyota Veloz
- Volkswagen Arteon
- Volkswagen ID.4
- Volkswagen T-Cross
- Volkswagen T-Roc
- Volkswagen Tiguan
- Volkswagen Tiguan Allspace
- Volkswagen Touareg
- Volvo EX30
- Volvo S90
- Volvo XC40
- Volvo XC60



### 3.3 VCB_3 MODELS


- Acura MDX
- Acura RLX
- Audi A7
- Audi A8
- Audi Q7
- Audi Q8
- Audi Q8 e-tron
- Audi RS Q8
- BMW 7 Series
- BMW 8 Series
- BMW X4
- BMW X5
- BMW X6
- BMW X7
- BMW XM
- BMW Z4
- BMW i7
- BMW iX
- BMW iX3
- BYD Han
- BYD Tang
- Bentley Bentayga
- Bentley Continental GT
- Bentley Flying Spur
- Cadillac Escalade
- Cadillac Escalade ESV
- Cadillac XT4
- Cadillac XT5
- Cadillac XT6
- Chevrolet Silverado
- Chevrolet Suburban
- Chevrolet Tahoe
- Chevrolet Traverse
- Exeed LX
- Exeed TXL
- Exeed VX
- Ford Bronco
- Ford Expedition
- Ford F-150
- Ford Super Duty (F-250/F-350)
- Ford Transit
- GAC GN6
- GAC GN8
- GAC GS8
- GMC Sierra 1500
- GMC Sierra HD
- GMC Yukon
- GMC Yukon XL
- Genesis G90
- Genesis GV70
- Genesis GV80
- Hongqi E-HS9
- Hongqi H9 (Luxury)
- Hongqi HS5
- Hongqi HS7
- Hyundai Palisade
- Hyundai Staria
- Infiniti Q60
- Infiniti QX50
- Infiniti QX55
- Infiniti QX60
- Infiniti QX70
- Infiniti QX80
- Jaguar F-Pace
- Jaguar F-Type
- Jaguar I-Pace
- Jaguar XJ
- Jeep Gladiator
- Jeep Wagoneer
- Jetour T2
- Kia Carnival
- Kia Telluride
- Land Rover Defender
- Land Rover Discovery
- Land Rover Range Rover
- Land Rover Range Rover Sport
- Land Rover Range Rover Velar
- Lexus GX
- Lexus LC
- Lexus LS
- Lexus LX
- Maserati Grecale
- Maserati Levante
- Maserati MC20
- Mercedes-Benz AMG GT
- Mercedes-Benz EQS
- Mercedes-Benz G-Class
- Mercedes-Benz GLA
- Mercedes-Benz GLB
- Mercedes-Benz GLC
- Mercedes-Benz GLE
- Mercedes-Benz GLS
- Mercedes-Benz S-Class
- Nissan Armada
- Nissan GT-R
- Nissan Patrol
- Porsche 718 Boxster
- Porsche 718 Cayman
- Porsche 911
- Porsche Cayenne
- Porsche Panamera
- Porsche Taycan
- RAM RAM 1500
- RAM RAM 2500
- RAM RAM 3500
- Rolls-Royce Cullinan
- Rolls-Royce Dawn
- Rolls-Royce Ghost
- Rolls-Royce Phantom
- Rolls-Royce Spectre
- Rolls-Royce Wraith
- Tesla Model S
- Tesla Model X
- Toyota Granvia
- Toyota Hiace
- Toyota Land Cruiser
- Toyota Prado
- Toyota Sequoia
- Toyota Tundra
- Volkswagen Atlas (Teramont)
- Volvo EX90
- Volvo XC90

---

## 4) ALIAS NORMALIZATION (MANY → ONE)

Purpose:
Convert customer shorthand into a canonical model when safe.

Format:
- alias_string → Canonical Model

Rules:
A) Safe alias (unique) → auto-normalize
B) Ambiguous alias (could mean multiple cars) → MUST CLARIFY
C) Arabic/Latin mixed aliases allowed

### 4.1 SAFE ALIASES (AUTO-NORMALIZE)
- t2 → Jetour T2
- h6 → Haval H6
- lc300 → Toyota Land Cruiser
- y62 → Nissan Patrol

lc200 -> Toyota Land Cruiser
land cruiser -> Toyota Land Cruiser
landcruiser -> Toyota Land Cruiser
v8 -> Toyota Land Cruiser

patrol -> Nissan Patrol
batrol -> Nissan Patrol
nissan patrol -> Nissan Patrol

prado -> Toyota Prado
prado tx -> Toyota Prado
prado txl -> Toyota Prado

camry -> Toyota Camry
corolla -> Toyota Corolla
yaris -> Toyota Yaris

xtrail -> Nissan X-Trail
x-trail -> Nissan X-Trail

rav4 -> Toyota RAV4
crv -> Honda CR-V

fortuner -> Toyota Fortuner
hilux -> Toyota Hilux

g63 -> Mercedes-Benz G-Class
g wagon -> Mercedes-Benz G-Class
gwagon -> Mercedes-Benz G-Class

glc -> Mercedes-Benz GLC
gle -> Mercedes-Benz GLE

lx570 -> Lexus LX
lx600 -> Lexus LX
gx -> Lexus GX
rx -> Lexus RX

tahoe -> Chevrolet Tahoe
suburban -> Chevrolet Suburban
silverado -> Chevrolet Silverado

f150 -> Ford F-150
raptor -> Ford F-150

t2 jetour -> Jetour T2
jetour t2 -> Jetour T2
h6 haval -> Haval H6

cx5 -> Mazda CX-5
cx9 -> Mazda CX-9

santa fe -> Hyundai Santa Fe
palisade -> Hyundai Palisade

tucson -> Hyundai Tucson
elantra -> Hyundai Elantra

sportage -> Kia Sportage
sorento -> Kia Sorento

### 4.2 AMBIGUOUS ALIASES (CLARIFY REQUIRED)
- x90 → [[CLARIFY: Which brand/model?]]
- s90 → [[CLARIFY: Volvo S90 or other?]]
- cx → [[CLARIFY: Mazda CX-?]]

lc -> [[CLARIFY: Land Cruiser or Lexus LC?]]
v6 -> [[CLARIFY: Which model?]]
gt -> [[CLARIFY: Which brand/model?]]
rs -> [[CLARIFY: Which brand/model?]]
amg -> [[CLARIFY: Which Mercedes model?]]
bmw x -> [[CLARIFY: X3, X5, X6, X7?]]
toyota suv -> [[CLARIFY: Which model?]]
nissan suv -> [[CLARIFY: Which model?]]

Clarify rule:
If alias is ambiguous, system must ask ONE clarification question before mapping.

---

## 5) UNMAPPED MODEL HANDLING (LOCKED)

If customer provides a model that is not found in Model → VCB mapping:

System action:
- Mark: UNMAPPED_MODEL = TRUE
- Do NOT auto-assign VCB
- Trigger: Manual VCB assignment required (assistant / ops)

Allowed manual method:
- Assistant checks model quickly (search) and assigns VCB
- After assignment, model MUST be added into Section 3 in the correct VCB list

---

## 6) NORMALIZATION OUTPUT (LOCKED)

When normalization happens, engines must output:
- CANONICAL_MODEL (string)
- VCB (VCB_1/2/3) or NULL if unmapped
- UNMAPPED_MODEL (TRUE/FALSE)
- CLARIFICATION_REQUIRED (TRUE/FALSE)

Execution order (must be followed strictly):

1) Extract vehicle reference from customer message
   - Use free text (English / Arabic / mixed)
   - Do NOT assume intent or service

2) Apply Alias Normalization (Section 4)
   - If alias exists in 4.1 SAFE → auto-normalize
   - If alias exists in 4.2 AMBIGUOUS → ask ONE clarification question
   - If no alias match → continue without failure

3) Resolve Canonical Model
   - Match against Section 3 (Model → VCB mapping)
   - Ignore trims / years unless they change segment size
   - If model exists → proceed
   - If model does NOT exist → mark UNMAPPED_MODEL = TRUE

4) Assign VCB
   - Use Section 3 mapping only
   - Do NOT infer VCB from brand perception
   - Do NOT use pricing, age, or customer intent

5) If UNMAPPED_MODEL = TRUE
   - Do NOT auto-assign VCB
   - Trigger clarification or ops review
   - After resolution, model must be added to Section 3

Rules:
- System must never skip steps
- System must never silently guess
- Only ONE clarification question is allowed per ambiguity

---

## 7) CHANGE CONTROL (LOCKED)

Any edits to:
- VCB definitions
- Unmapped model handling rules
- Alias normalization rules

Require:
- Explicit change note
- Reason
- Date

Mapping list updates (Section 3) do NOT require change notes.

---
END OF FILE