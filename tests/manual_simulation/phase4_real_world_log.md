# PHASE 4 REAL WORLD SIMULATION LOG

## RULE
- Each scenario = new chat
- Max 5 turns
- No meta questions inside chat
- Record exactly what happened
- Do NOT interpret here

---

## TEMPLATE

### SCENARIO ID:
### SERVICE:
### TEST TYPE: (price resistance / silence / competitor)

### CUSTOMER FLOW:
1.
2.
3.
4.

### BOT RESPONSES:
1.
2.
3.
4.

### OBSERVATION (RAW ONLY):
- stayed in phase: yes/no
- natural tone: yes/no
- drift detected: yes/no
- issue summary (1 line):

---


### SCENARIO ID: P4-001
### SERVICE: PPF
### TEST TYPE: price resistance

### CUSTOMER FLOW:
1. ppf camry 2022 how much
2. expensive

### BOT RESPONSES:
1. هلا 👋
   حياك الله

   عشان أعطيك السعر مضبوط، هل تبي حماية للمقدمة فقط ولا كامل السيارة؟ 👍

2. أتفهمك 👍
   بس خليني أعرف أول، ناوي على حماية أي جزء بالضبط؟ عشان أقدر أساعدك بالأنسب لك

### OBSERVATION (RAW ONLY):
- stayed in phase: yes
- natural tone: yes
- drift detected: no
- issue summary (1 line): objection handled by returning to qualification (coverage not confirmed)

---


### SCENARIO ID: P4-002
### SERVICE: PPF
### TEST TYPE: price resistance after full qualification

### CUSTOMER FLOW:
1. ppf camry 2022 full
2. ok how much
3. expensive

### BOT RESPONSES:
1. asked again full vs parts
2. asked trim (standard vs full option)
3. returned to coverage question instead of handling objection

### OBSERVATION (RAW ONLY):
- stayed in phase: no
- natural tone: yes
- drift detected: yes
- issue summary (1 line): system stuck in over-qualification loop and failed to trigger price + objection flow

---


### SCENARIO ID: P4-003
### SERVICE: PPF
### TEST TYPE: front coverage price + objection

### CUSTOMER FLOW:
1. ppf camry 2022 front
2. price
3. expensive

### BOT RESPONSES:
1. asked front full vs parts (re-qualification)
2. repeated same question again (no progression)
3. moved to budget suggestion without giving price

### OBSERVATION (RAW ONLY):
- stayed in phase: no
- natural tone: yes
- drift detected: yes
- issue summary (1 line): system loops in qualification, fails to release price, and jumps to objection without price context

---


### SCENARIO ID: P3A-PPF-001
### SERVICE: PPF
### TEST TYPE: qualification completion chain

### CUSTOMER FLOW:
1. ppf camry 2022 front
2. highway
3. price

### BOT RESPONSES:
1. 
2. 
3. 

### OBSERVATION (RAW ONLY):
- stayed in phase: 
- natural tone: 
- drift detected: 
- issue summary (1 line): 

---


### SCENARIO ID: P3A-PPF-002
### SERVICE: PPF
### TEST TYPE: coverage normalization failure

### CUSTOMER FLOW:
1. ppf camry 2022 front

### BOT RESPONSE:
حياك الله 👋
للمقدمة فقط لسيارة كامري 2022، تبغى الحماية تشمل كامل المقدمة ولا أجزاء معينة؟

### OBSERVATION:
- coverage "front" was already provided
- system re-asked same qualifier (coverage)
- failed to move to driving pattern question
- Phase 3A normalization not respected

### ISSUE:
PPF_COVERAGE_INTENT normalization not honored by Phase 3A gate

---

