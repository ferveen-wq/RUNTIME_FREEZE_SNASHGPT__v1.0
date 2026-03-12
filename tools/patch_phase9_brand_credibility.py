from pathlib import Path

file_path = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
content = file_path.read_text()

replacement = """

### PHASE4_INSTALLATION_CREDIBILITY_L1
EN:
Many films in the market perform well, but what usually determines how clean the result looks after a few years is the preparation and installation quality, not just the film name.

AR:
الكثير من أفلام الحماية في السوق تؤدي بشكل جيد، لكن ما يحدد غالبًا كيف سيبدو الشكل بعد عدة سنوات هو جودة التحضير ودقة التركيب، وليس اسم الفيلم فقط.


### PHASE4_INSTALLATION_CREDIBILITY_L2
EN:
What usually makes the difference is the preparation behind the installation and how carefully the film is aligned on each panel.

AR:
الفرق الحقيقي غالبًا يأتي من جودة التحضير قبل التركيب ومدى دقة محاذاة الفيلم على كل جزء من السيارة.


### PHASE4_PROTECTION_LOGIC_L1
EN:
Ceramic coating mainly improves gloss and makes cleaning easier. For protection against stone chips and road impact, the layer that actually absorbs the damage is PPF.

AR:
طبقة السيراميك تعزز اللمعان وتسهّل التنظيف، لكن للحماية من ضربات الحصى وتأثير الطريق فإن الطبقة التي تمتص الصدمات فعليًا هي طبقة الحماية PPF.


### PHASE4_VISUAL_PROOF_INVITE_L1
EN:
Sometimes the easiest way to understand the finish is to see a similar car we completed recently so you can judge the edges and reflections yourself.

AR:
أحيانًا أسهل طريقة لفهم النتيجة هي رؤية سيارة مشابهة قمنا بإنهائها مؤخرًا حتى تتمكن من تقييم الحواف والانعكاسات بنفسك.


### PHASE4_PROCESS_TRANSPARENCY_L1
EN:
If you like, I can briefly explain how the preparation and installation steps work so expectations stay clear.

AR:
إذا رغبت، يمكنني شرح خطوات التحضير والتركيب بإيجاز حتى تكون التوقعات واضحة.


### PHASE4_REAL_WORLD_DURABILITY_L1
EN:
In GCC conditions, stability over time usually matters more than just the initial appearance.

AR:
في ظروف الخليج، الاستقرار على المدى الطويل غالبًا يكون أهم من المظهر الأولي فقط.

"""

content = content.replace(
    "[PLACEHOLDER — BRAND CREDIBILITY PHRASES]",
    replacement
)

file_path.write_text(content)
print("Phase 9 persuasion phrases inserted successfully.")
