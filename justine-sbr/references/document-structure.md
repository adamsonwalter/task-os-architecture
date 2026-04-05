# Strategic Business Review — Document Structure

## Document Setup (python-docx)

```python
from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Page setup
doc = Document()
sections = doc.sections
for section in sections:
    section.page_width = Cm(21.0)  # A4 width
    section.page_height = Cm(29.7)  # A4 height
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)

# Font setup for all text
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(11)
```

---

## Section 1: Opening Letter

**Purpose:** Establish personal connection in under 250 words.

**Format:**
```
Prepared for you, [Owner Name] — [Month Year] (Australia/Melbourne time)

[Owner Name], [personalised opening that reflects their business context and stated goals].

[One paragraph connecting emotionally to their journey — what they've built, what they're seeking].

In my book, I tell the truth that most founders learn the hard way: [relevant insight]. The fix is rarely more hustle. It's rhythm, visibility, and a few small levers pulled consistently.

What follows is written to you like a private letter, because that's how real strategy lands — not as a report you admire, but as a rhythm you live.
```

**Tone:** Warm, personal, forward-looking.

---

## Section 2: Executive Overview

**Purpose:** Deliver 3–5 key findings as truths to hold.

**Format:**
```
1. Executive Overview — the three truths I want you to hold steady

[Truth 1: Current state assessment]
[Truth 2: Core strength or constraint]
[Truth 3: Leadership/wellbeing connection]

So the leverage points are clear: [3-4 specific levers].

With those truths held gently but firmly, we can look at where you actually are in the lifecycle, and what tools fit this season.
```

**Word count:** ~300 words maximum.

---

## Section 3: Business Reality & Context

**Purpose:** Establish lifecycle stage and dashboard visibility.

**Format:**
```
2. Business Reality & Context — what stage you're in (and what that means)

[Business snapshot: years operating, revenue band, team size, markets served]

This means you are [not/in] "[stage name]" yet. You are in what I'd call [specific stage with qualifier]. In the lifecycle lens from the book: [relevant lifecycle description].

Right now, you are doing the correct founder things: [list their positive actions].

But your survey answer contains a quiet warning: [identify gaps in visibility/measurement].

This is what I mean by dashboard visibility. The wheel is turning, but the dials aren't readable yet.

[Bridge → to next section]
```

---

## Section 4: Client Care

**Purpose:** Transform their differentiation into systemised trust.

**Format:**
```
3. Client Care — [personalised subtitle based on their differentiation]

In [their industry], the customer is not buying [commodity] first. They are buying [deeper need — certainty, trust, reliability].

[Connect to their stated reasons why customers choose them]

Here is the trap I want you to avoid: [relevant risk for their situation].

So, we make [their differentiator] visible.

**The "Moments of Truth" map**

[List 5-6 moments relevant to their business]

**Reflective call-out:**
[Question that connects their values to operational reality]
```

**Action Box — Client Care Rhythm**
```
☐ [First moment to tighten]
☐ [Response standard to set]
☐ [Documentation to create]
☐ [Protocol to establish]
☐ [Handover practice to implement]
```

**Bridge →** Once trust is systemised, your marketing and sales stop relying on charisma and start relying on process.

---

## Section 5: Sales & Marketing

**Purpose:** Shape pipeline from volume to precision.

**Format:**
```
4. Sales & Marketing — [personalised subtitle]

[Acknowledge their current marketing efforts and tools]

So the question is not "How do we get more leads?"
It's: How do we turn [their volume] into real, bankable [outcomes] — with a conversion rhythm you can trust?

**Your offer must become a "fast yes"**

[Explain staged offer concept relevant to their business]

**Build the simple pipeline math**

[Explain pipeline tracking relevant to their situation]

We can't improve what we refuse to measure.
```

**Action Box — Sales Rhythm**
```
☐ Define "qualified lead" in one sentence
☐ Add a "disqualify fast" rule
☐ Create pipeline stages in [their tool]
☐ Set weekly 30-minute review
☐ Write one "fast yes" offer and test with warm leads
```

**Reflective call-out:**
If you had to halve your leads next month, what would you keep doing because it produces the highest quality conversations?

---

## Section 6: Operations & Systems

**Purpose:** Build minimum viable operating system.

**Format:**
```
5. Operations & Systems — you're building the stage, not just doing the show

[Acknowledge their tools and current systems efforts]

The operational question for you is: what are the few repeatable processes that make the business feel "real" to an outsider?

**Your minimum viable operating system (MVOS)**

In your stage, you don't need a big SOP library. You need a "minimum viable system" for:
- [List 5-6 critical processes]

**Automation: choose relief, not novelty**

[Guidance on automation priorities]

**Reflective call-out:**
Where is the business currently relying on your memory, your energy, or your personal pushing — instead of a simple system?
```

**Action Box — Systems Rhythm**
```
☐ Choose one process to document this week
☐ Add one short video walkthrough
☐ Create single "source of truth" folder structure
☐ Define weekly "ops reset" ritual
☐ Set work-in-progress limit
```

---

## Section 7: People & Leadership

**Purpose:** Transform family-style culture into scalable clarity.

**Format:**
```
6. People & Leadership — [personalised subtitle based on their culture description]

[Acknowledge their current team culture]

But it becomes risky the moment pressure increases, because [their style] without clarity can quietly become:
- [List relevant risks]

Clarity is kindness. And standards protect relationships.

**The tiny org chart that will change your life**

[Function-first explanation]

**Training doesn't have to be fancy — it has to be rhythmic**

[Simple training cadence]

**Reflective call-out:**
What behaviours do you tolerate right now (in yourself or others) that your future business cannot afford?
```

**Action Box — Leadership Rhythm**
```
☐ Write role outcomes for each person in 10 lines
☐ Choose one non-negotiable standard
☐ Start weekly team rhythm
☐ Schedule deep work blocks
☐ Decide health minimums and calendar them
```

---

## Section 8: Financial Rhythm

**Purpose:** Transform cashflow from fear to steering mechanism.

**Format:**
```
7. Financial Rhythm — cashflow is not your weakness; it's your current constraint

[Acknowledge their stated cashflow situation]

So let me speak plainly: cashflow is the boss of your current stage.
[Reason specific to their business model]

If you want the freedom you described — [their personal success definition] — cashflow must become a weekly practice, not a monthly surprise.

**The three rhythms that calm the nervous system**

[Daily/Weekly/Monthly structure]

**Your business model needs "now money" and "later wealth"**

[Staged commercial model explanation]

**Truth-telling moment:**
A mission without margin becomes martyrdom. If you want to [their goal] at scale, your numbers must be kind enough to keep you alive.
```

**Action Box — Cashflow Rhythm**
```
☐ Build 13-week cash forecast (update every Friday)
☐ Set one deal term non-negotiable
☐ Separate pipeline value from cash collected
☐ Identify top 3 expenses and decide one trim
☐ Book monthly numbers and decisions meeting
```

---

## Section 9: Risk & Opportunity Lens

**Purpose:** Frame risk as information and identify courage lever.

**Format:**
```
8. Risk & Opportunity — your courage lever is [specific to their situation]

**The key risks (framed as information, not threat)**

[Risk 1: Specific to their survey responses]
[Risk 2: Systemic business risk]
[Risk 3: Founder dependency risk]

**The opportunities (and they're real)**

[Opportunity 1: Their differentiation advantage]
[Opportunity 2: Their systems/tool investment]
[Opportunity 3: Their ambition/narrative advantage]

**Your courage lever:**
The decision that will feel uncomfortable but change everything is [specific action].
```

**Action Box — Risk & Opportunity**
```
☐ Name one risk to neutralise (write it as a sentence)
☐ Name one opportunity to activate (also a sentence)
☐ Choose the one behaviour shift required
```

---

## Section 10: 12-Month Coaching Invitation

**Purpose:** Natural progression from insight to structured partnership.

**Format:**
```
9. Twelve-Month Coaching Invitation — a guided rhythm, quarter by quarter

[Owner Name], you don't need more ideas. You already have vision. What you need is a structure that protects the vision — and a rhythm that turns your intent into repeatable progress.

If we worked together for 12 months, the coaching would not be "motivation." It would be a steady drumbeat: truth-telling, small improvements, systems that breathe, and leadership decisions made while you're calm.

**Quarter 1 — Clarity, Cash, and the First Offer** (Months 1-3)
Focus: [2-3 sentences]
Actions: [3-4 bullet points]
Outcome: [Transformation result]

**Quarter 2 — Conversion, Delivery Cadence, and Standards** (Months 4-6)
Focus: [2-3 sentences]
Actions: [3-4 bullet points]
Outcome: [Transformation result]

**Quarter 3 — Team Leverage and Systems That Breathe** (Months 7-9)
Focus: [2-3 sentences]
Actions: [3-4 bullet points]
Outcome: [Transformation result]

**Quarter 4 — Scale With Integrity, and Prepare for Optionality** (Months 10-12)
Focus: [2-3 sentences]
Actions: [3-4 bullet points]
Outcome: [Transformation result]
```

---

## Section 11: Closing Reflection

**Purpose:** Return to signature themes with gentle invitation.

**Format:**
```
10. Closing Reflection — truth, rhythm, courage, and freedom through structure

[Owner Name], your vision is big enough to pull you forward for years. But vision alone can quietly become a demand — "prove it, prove it, prove it" — unless you build a kinder structure underneath it.

So here is my closing truth: businesses don't collapse from a lack of ambition. They collapse from a lack of rhythm.

You've already shown the trait that matters most: you're willing to name what's true. [Specific acknowledgment of their honesty in survey responses]. That honesty is not just [their differentiator] — it's your leadership gift.

Now we take that gift and give it a home:
- [Key rhythm 1]
- [Key rhythm 2]
- [Key standard]
- [Key system]
- [Key leadership practice]

**Final reflective call-out:**
[Question connecting their stated personal goals to business structure]

If you'd like, we can turn this review into a 12-month guided rhythm — steady, practical, and deeply aligned with the world you're here to build. Not hustle. Not hype. Just consistent, committed, courageous, imperfect, inspired action — the kind that compounds quietly until one day the business feels inevitable.
```

---

## Action Box Formatting (python-docx)

```python
def add_action_box(doc, title, items):
    """
    Add bordered Action Box that won't split across pages.
    """
    # Add paragraph before for spacing
    doc.add_paragraph()
    
    # Create single-cell table with borders
    table = doc.add_table(rows=1, cols=1)
    table.autofit = True
    
    # Set table borders
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement('w:tblPr')
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '12')
        border.set(qn('w:color'), '000000')
        tblBorders.append(border)
    tblPr.append(tblBorders)
    tbl.append(tblPr)
    
    # Prevent row from splitting
    row = table.rows[0]
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    cantSplit = OxmlElement('w:cantSplit')
    trPr.append(cantSplit)
    
    # Add content to cell
    cell = table.cell(0, 0)
    
    # Title
    title_para = cell.paragraphs[0]
    title_run = title_para.add_run(f"Action Box — {title}")
    title_run.bold = True
    title_run.font.name = 'Arial'
    title_run.font.size = Pt(11)
    
    # Items
    for item in items:
        para = cell.add_paragraph()
        run = para.add_run(f"☐ {item}")
        run.font.name = 'Arial'
        run.font.size = Pt(11)
    
    return table
```

---

## Final CTA Box

Same bordered format as Action Box but with different content:

```
What's Next?

[Owner Name], your next 90 days are the proof phase. If this review has clarified your direction, let's refine your 12-month plan together. Your rhythm begins now.
```

---

## Word Count Targets by Section

| Section | Target Words |
|---------|--------------|
| Opening Letter | 200-250 |
| Executive Overview | 250-350 |
| Business Reality | 300-400 |
| Client Care | 400-500 |
| Sales & Marketing | 500-600 |
| Operations & Systems | 400-500 |
| People & Leadership | 400-500 |
| Financial Rhythm | 400-500 |
| Risk & Opportunity | 300-400 |
| 12-Month Invitation | 400-500 |
| Closing Reflection | 250-350 |
| **Total** | **3,800-4,850** |

---

## Quality Gates

Before finalising document:

1. **Voice check:** Read opening paragraph aloud — does it sound like a mentor or a consultant?
2. **Rhythm check:** Does each section follow analysis → reflection → action pattern?
3. **Personalisation check:** Are owner's words/goals mirrored back at least 3 times?
4. **Bridge check:** Are there at least 2 "Bridge →" transitions?
5. **Action Box check:** Are there at least 3 properly formatted Action Boxes?
6. **Lived experience check:** Is there at least 1 reference to deli/dry cleaner/clinic?
7. **Courage lever check:** Is there one clear uncomfortable decision identified?
8. **CTA check:** Does closing invitation feel gentle, not pushy?
