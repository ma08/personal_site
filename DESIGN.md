# Design Aesthetic: Scholarly Fusion

> "A researcher's private study where ancient Sanskrit texts sit next to machine learning papers—warm lamplight on aged wood, terracotta pottery holding pencils, faded equations on the walls."

## Design Philosophy

This website embodies **Scholarly Fusion**—a blend of:
- **Research/Tech**: Neural networks, gradient descent, matrices, cryptography
- **Spiritual/Cultural**: Kolam patterns, yantra geometry, Sanskrit, meditation

The aesthetic conveys a **polyglot, multidisciplinary hacker** who loves etymology, spirituality, culture, history, and the fusion of old-school wisdom with modern research.

---

## Typography System

| Role | Font | Character |
|------|------|-----------|
| **Headings** | Inknut Antiqua | Indic calligraphy essence in Latin letterforms. Distinctive, warm, fusion identity. |
| **Body** | Vollkorn | Organic German serif. Warm, readable, excellent for long-form content. |
| **Code** | IBM Plex Mono | Intellectual, clean. Bridges scholarly and tech worlds. |

### Font Loading (Google Fonts)
```css
@import url('https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@400;500;600;700&family=Vollkorn:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&display=swap');
```

### Font Sizing
- Body: 18px, line-height 1.75
- H1/Post titles: 2.25rem (36px)
- H2: 1.75rem (28px)
- H3: 1.4rem (22px)
- Profile name: 2.5rem (40px)

---

## Color Palette: Saffron & Ink

### Light Mode
| Variable | Hex | Usage |
|----------|-----|-------|
| `--theme` | `#FAF8F5` | Background (cream/aged paper) |
| `--entry` | `#FFFFFF` | Card backgrounds |
| `--primary` | `#1A1A1A` | Headings (deep charcoal) |
| `--secondary` | `#4A4A4A` | Secondary text |
| `--content` | `#2C2C2C` | Body text |
| `--accent` | `#C05746` | Links, highlights (terracotta) |
| `--accent-hover` | `#A84637` | Hover state |
| `--border` | `#E5E0D8` | Borders (warm beige) |
| `--code-bg` | `#F0EBE3` | Inline code background |
| `--code-block-bg` | `#1C1B1A` | Code block background |

### Dark Mode
| Variable | Hex | Usage |
|----------|-----|-------|
| `--theme` | `#1C1B1A` | Background (warm charcoal) |
| `--entry` | `#252321` | Card backgrounds |
| `--primary` | `#F5F0E8` | Headings (warm cream) |
| `--secondary` | `#B8B2A8` | Secondary text |
| `--content` | `#E0DBD3` | Body text |
| `--accent` | `#D4705F` | Links (lighter terracotta) |
| `--accent-hover` | `#E8887A` | Hover state |
| `--border` | `#3A3836` | Borders |
| `--code-bg` | `#2A2826` | Code backgrounds |

### Accent Color Rationale
**Terracotta (#C05746)** evokes:
- Temple brick and pottery
- Earth and groundedness
- Indian textiles and warmth
- Spiritual without being overtly religious

---

## Fusion Watermarks

Subtle background patterns that blend tech and spiritual imagery—like equations drawn on aged manuscript paper.

### Fusion Elements

| Tech/Research | ↔ | Spiritual/Cultural |
|---------------|---|-------------------|
| Neural network nodes & edges | | Kolam dot patterns |
| Gradient descent contours | | Mountain/valley yantra |
| Graph theory diamonds | | Buddhist endless knot |
| Matrix/array grids | | Sanskrit syllable charts |
| Sine wave functions | | Pranayama breath cycles |

### Watermark Files
- **Light mode**: `/static/images/watermark-light.svg`
- **Dark mode**: `/static/images/watermark-dark.svg`

### Watermark Settings

| Mode | Opacity | Stroke Color | Stroke Width |
|------|---------|--------------|--------------|
| Light | 22% | `#5A4332` (dark brown) | 1.5-2.5px |
| Dark | 12% | `#E8DDD0` (warm cream) | 1-2px |

### Pattern Components
1. **Neural Kolam** (center): Diamond curves with node dots
2. **Gradient Yantra** (top-left): Loss landscape contours with descent arrow
3. **Endless Knot** (top-right): Graph theory diamond with cross connections
4. **Breath Wave** (bottom): Sine waves with peak markers
5. **Sanskrit Matrix** (varies): 3×3 grid with intersection dots

---

## CSS Architecture

### File Locations
- **Custom CSS**: `/assets/css/extended/custom.css`
- **Theme variables**: `/themes/PaperMod/assets/css/core/theme-vars.css`

### Key CSS Customizations
```css
/* Override PaperMod's .list background for watermarks */
body,
body.list,
.list {
    background-color: var(--theme);
    background-image: url('/images/watermark-light.svg');
    background-size: 600px;
    background-position: center;
    background-repeat: repeat;
}

body.dark,
body.dark.list,
.dark.list {
    background-color: var(--theme);
    background-image: url('/images/watermark-dark.svg');
}
```

---

## Layout Principles

- **Generous whitespace**: Breathing room, meditative feel
- **Strong type hierarchy**: Inknut Antiqua headings stand out
- **Warm, not cold**: Rounded corners (6px), soft shadows
- **Manuscript margins**: Content max-width 720px

---

## Interactive Elements

### Links
- Color: Terracotta accent
- Underline with 3px offset
- Hover: Darker terracotta

### Buttons
- Border radius: 6px
- Hover: Fill with terracotta

### Code
- Inline: Warm off-white background, 4px radius
- Blocks: Dark warm charcoal, syntax highlighting

### Selection
- Background: Terracotta tint (10-15% opacity)

---

## Design Maintenance

### To adjust watermark visibility:
1. Edit `/static/images/watermark-light.svg` or `watermark-dark.svg`
2. Change the `opacity` value in the main `<g>` element
3. Adjust stroke colors if needed

### To change accent color:
1. Edit `/assets/css/extended/custom.css`
2. Update `--accent` and `--accent-hover` in both `:root` and `.dark`

### To modify typography:
1. Update Google Fonts import URL
2. Change `--font-heading`, `--font-body`, `--font-mono` variables

---

## Credits

- **Theme**: PaperMod by Aditya Telange
- **Fonts**: Google Fonts (Inknut Antiqua, Vollkorn, IBM Plex Mono)
- **Design concept**: Scholarly Fusion - blending research aesthetics with spiritual/cultural elements
