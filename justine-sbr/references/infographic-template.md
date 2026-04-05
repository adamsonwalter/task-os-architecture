# Strategic Infographic SPA — Technical Reference

## Core Requirements

- **Single file:** All HTML, CSS, and JS in one `.html` file
- **Frameworks:** Tailwind CSS (CDN), Chart.js (CDN)
- **NO:** SVG, Mermaid JS, external diagram libraries
- **Icons:** Unicode characters only
- **Responsive:** Must work on all screen sizes

**Boilerplate example:** See `references/infographic-example.html` for a complete working template.

---

## Colour Palette Selection

Select based on client industry and mood:

### Professional Services / Consulting
```css
--primary: #2563eb;      /* Blue-600 */
--secondary: #1e40af;    /* Blue-800 */
--accent: #f59e0b;       /* Amber-500 */
--success: #10b981;      /* Emerald-500 */
--warning: #ef4444;      /* Red-500 */
--neutral: #6b7280;      /* Gray-500 */
```

### Energy / Infrastructure
```css
--primary: #059669;      /* Emerald-600 */
--secondary: #065f46;    /* Emerald-800 */
--accent: #f59e0b;       /* Amber-500 */
```

### Healthcare / Wellness
```css
--primary: #0891b2;      /* Cyan-600 */
--secondary: #155e75;    /* Cyan-800 */
--accent: #8b5cf6;       /* Violet-500 */
```

### Hospitality / Retail
```css
--primary: #dc2626;      /* Red-600 */
--secondary: #991b1b;    /* Red-800 */
--accent: #f59e0b;       /* Amber-500 */
```

---

## Unicode Icons Library

Use these instead of SVG:

```
📊 Analytics/Dashboard     💰 Finance/Money
📈 Growth/Increase         💸 Cashflow
📉 Decline/Decrease        🎯 Target/Goal
⚡ Energy/Action           🔄 Cycle/Recurring
✅ Complete/Success        ⚠️ Warning/Risk
❌ Blocked/Failed          🚀 Launch/Growth
🛠️ Operations/Tools        👥 Team/People
📋 Process/Checklist       💡 Insight/Idea
🏆 Achievement             🔑 Key/Critical
⏰ Time/Schedule           📅 Calendar
🌱 Growth/Start            🌳 Maturity
🔥 Hot/Urgent              ❄️ Cold/Stale
➡️ Next/Flow               ⬆️ Up/Improve
```

---

## Required Visualisation Components

### 1. Diagnostic Gauges (Business Vitals)

Half-circle doughnut charts showing health status. Create gauges for:
- Revenue Rhythm (based on cashflow stability)
- Operational Maturity (based on systems/processes)
- Sales Precision (based on conversion rate)
- Team Clarity (based on role/structure description)

**Chart.js configuration:**
```javascript
{
    type: 'doughnut',
    options: {
        circumference: 180,
        rotation: -90,
        cutout: '75%',
        plugins: { legend: { display: false }, tooltip: { enabled: false } }
    }
}
```

### 2. Strategic Pivot (Before/After Bar Chart)

Contrast current state vs. target state using horizontal bar chart:
- Lead Volume
- Conversion Rate
- Cash Cycle Days
- Owner Hours/Week

### 3. Rhythm Projection (Line Chart)

Show transition from chaos to rhythm over 12 months:
- Dashed line: "Without Structure" (volatile)
- Solid line: "With Rhythm" (steady upward)

### 4. 12-Month Roadmap (CSS Timeline)

Fully responsive, no diagram libraries. Uses alternating left/right card layout on desktop, stacked on mobile.

---

## Data Extraction From Report

Map these report elements to infographic data:

| Report Element | Infographic Component |
|----------------|----------------------|
| Lifecycle stage | Gauge: Operational Maturity |
| Conversion rate | Gauge: Sales Precision |
| Cashflow description | Gauge: Revenue Rhythm |
| Role clarity | Gauge: Team Clarity |
| Current lead volume | Pivot: Before state |
| Target metrics | Pivot: After state |
| 90-day actions | Timeline: Q1 |
| Q2-Q4 coaching plan | Timeline: Q2-Q4 |

---

## Mobile Responsiveness

Key breakpoints:
- `sm`: 640px (mobile landscape)
- `md`: 768px (tablet)
- `lg`: 1024px (desktop)

Timeline adjusts:
- Desktop: Alternating left/right
- Tablet: All left-aligned
- Mobile: Stacked vertically

---

## Label Wrapping Utility

Required for all charts to prevent overflow:

```javascript
function wrapLabel(label, maxWidth) {
    if (!label || label.length <= maxWidth) return label;
    const words = label.split(' ');
    const lines = [];
    let currentLine = '';
    words.forEach(word => {
        if ((currentLine + ' ' + word).trim().length <= maxWidth) {
            currentLine = (currentLine + ' ' + word).trim();
        } else {
            if (currentLine) lines.push(currentLine);
            currentLine = word;
        }
    });
    if (currentLine) lines.push(currentLine);
    return lines;
}
```
