#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai",
#     "python-dotenv",
#     "pillow",
# ]
# ///
"""
Generate AI backgrounds using Nano Banana Pro (Gemini 3 Pro Image)
for Sourya's personal website.

Usage:
    uv run scripts/generate-backgrounds.py [--light-only] [--dark-only] [--prompt-variant N]
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from google import genai
from google.genai import types

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "static" / "images"
# Available image models:
# - gemini-2.5-flash-image (faster, good quality)
# - gemini-3-pro-image-preview (Nano Banana Pro - highest quality, slower)
MODEL = "gemini-3-pro-image-preview"  # Nano Banana Pro - best quality

# Prompt variants for iteration
# Variants 0-2: Plain textures (no fusion elements)
# Variants 3-5: Fusion elements with handwritten ink style

LIGHT_PROMPTS = [
    # Variant 0: Plain parchment
    """Seamless tileable texture of aged parchment paper with subtle ink wash stains
    and faint fabric weave pattern. Warm cream sepia tones matching #FAF8F5.
    Very minimal contrast, scholarly aesthetic. Suitable for website background.
    The texture should tile perfectly without visible seams.""",

    # Variant 1: Plain organic
    """Seamless repeating pattern of antique handmade paper with natural fiber texture.
    Subtle tea-stained watercolor washes. Warm cream background close to #FAF8F5.
    Very soft organic texture, minimalist and elegant. Must tile seamlessly.""",

    # Variant 2: Plain manuscript
    """Seamless tileable aged manuscript paper texture. Faded parchment with subtle
    foxing and age spots. Warm ivory sepia tones. Hints of old library or archive.
    Minimal contrast for readability. Perfect for scholarly website background.""",

    # Variant 3: Fusion - Primary (handwritten ink style)
    """Seamless tileable aged parchment texture with very subtle hand-drawn ink
    sketches faded over time. Include delicate handwritten elements: small
    lotus flower sketches, flowing calligraphic brush strokes, faint
    constellation-like dots connected by thin hand-drawn lines, and loose
    mandala doodles. Drawn in sepia/brown ink that has faded to ghostly
    impressions. Warm cream tones #FAF8F5. Like an old scholar's notebook
    with mystical marginalia. Must tile seamlessly.""",

    # Variant 4: Fusion - Botanical/Sacred
    """Seamless tileable antique paper with faded hand-drawn botanical sketches
    and sacred geometry. Delicate ink drawings of lotus flowers, flowing
    vine tendrils, and hand-sketched mandala patterns. Include fragments of
    handwritten script or calligraphy practice. Brown ink faded to subtle
    watermarks. Warm cream #FAF8F5. Like pages from an old naturalist's
    journal mixed with a monk's meditation notes. Must tile perfectly.""",

    # Variant 5: Fusion - Manuscript/Network
    """Seamless tileable aged manuscript paper with ghostly hand-drawn diagrams.
    Faded ink sketches of interconnected dots like star maps or thought
    webs, flowing curves like breath drawings, and traces of handwritten
    calligraphy in various scripts. Sepia ink aged to near-invisible.
    Like a polyglot scholar's private notebook. Warm ivory tones.
    Must tile seamlessly.""",

    # Variant 6: Scientific Scholar (SUBTLE - Primary)
    """Seamless tileable aged parchment with EXTREMELY FAINT hand-drawn scholarly
    marginalia. Barely visible ghostly traces of: mathematical notation and
    small equations, interconnected node diagrams like thought maps, fragments
    of handwritten text in different scripts (Greek, Sanskrit letters), small
    coordinate axes and arrows, flowing sine wave sketches. All elements must
    be watermark-faint (5-10% visibility), like century-old pencil marks nearly
    erased. Warm cream #FAF8F5. Primarily paper texture with hints of a
    polymath's notebook. Must tile seamlessly. Must not interfere with readability.""",

    # Variant 7: Etymology/Language Focus (SUBTLE)
    """Seamless tileable antique manuscript paper with extremely subtle linguistic
    marginalia. Ghostly traces of: handwritten letters from various alphabets
    (Devanagari, Greek, Latin, Arabic shapes), small word etymology trees,
    flowing calligraphic practice strokes, faint phonetic notation marks.
    All barely visible like faded watermarks. Warm cream sepia tones #FAF8F5.
    Like a linguist's aged notebook. Elements at 5% opacity feel. Must tile
    seamlessly. Readability is priority.""",

    # Variant 8: Research/Network Focus (SUBTLE)
    """Seamless tileable aged paper with extremely faint research diagram traces.
    Barely visible: interconnected dot-and-line networks, small graph sketches,
    coordinate systems with curves, arrow flows, mathematical symbols scattered
    sparsely. Like a researcher's whiteboard photographed through fog. Warm
    cream paper #FAF8F5. Watermark-subtle, must not compete with content.
    Must tile seamlessly.""",

    # Variant 9: Minimal Fusion (MOST SUBTLE)
    """Seamless tileable aged parchment texture with extremely sparse, nearly
    invisible scholarly marks. Only occasional: single flowing curves, isolated
    mathematical symbols, tiny dot clusters, faint single letters. 95% pure
    paper texture, 5% ghostly hints of scholarship. Warm cream #FAF8F5.
    Maximum subtlety. Must tile seamlessly.""",

    # === NEW AESTHETIC: Zen + Matrix + Etymology (clean backgrounds) ===

    # Variant 10: Zen Matrix (Primary)
    """Seamless tileable pattern on clean cream background #FAF8F5. Features
    VISIBLE floating elements: flowing zen brushstroke curves, falling
    characters from multiple scripts (Sanskrit, Greek, Japanese, Latin),
    interconnected neural network nodes with flowing lines, mathematical
    symbols (∫, Σ, ∂, π). Elements should be medium-sized and clearly
    visible but not overwhelming. Ink-brush aesthetic for organic feel.
    Mix of digital matrix streams and meditative flowing forms. Modern
    and enlightened. Must tile seamlessly.""",

    # Variant 11: Etymology Stream
    """Seamless tileable pattern on clean cream #FAF8F5. Features clearly
    visible floating characters from many writing systems: Devanagari,
    Greek letters, Latin, Arabic, Chinese/Japanese characters, mathematical
    notation. Characters should be medium-large size, arranged in flowing
    streams like falling rain or floating upward. Some characters connected
    by thin flowing lines. Polyglot linguistic tapestry. Modern clean
    aesthetic. Must tile seamlessly.""",

    # Variant 12: Neural Zen
    """Seamless tileable on cream background #FAF8F5. Features visible
    neural network node patterns with flowing organic connections,
    interspersed with zen enso circles (incomplete brush circles),
    flowing sine waves, and scattered script characters. Nodes are
    medium-sized circles connected by flowing brush-like lines. Balance
    of digital structure and zen organic flow. Must tile seamlessly.""",

    # Variant 13: Enlightened Code
    """Seamless tileable on clean cream #FAF8F5. Matrix-inspired falling
    streams of characters mixing: code symbols ({}, [], <>, =), Sanskrit
    letters, Greek alphabet, mathematical operators. Streams flow vertically
    with slight organic waviness. Characters medium-sized and readable.
    Enlightenment meets technology. Clean modern feel. Must tile seamlessly.""",

    # === SUBTLE WATERMARK VARIANTS (prioritize readability) ===

    # Variant 14: Subtle Fusion Watermark (Primary)
    """Seamless tileable watermark pattern on clean cream #FAF8F5. VERY SUBTLE
    ghostly silhouettes at 10% opacity: meditating yogi figure, lotus flower
    outlines, neural network node diagrams, simple robot silhouettes,
    scattered multi-script letters (Sanskrit, Greek, Devanagari). Elements
    EXTREMELY FAINT like watermarks on paper. Sparse placement with lots of
    empty space. Must not interfere with text readability. Clean modern
    aesthetic. Must tile seamlessly.""",

    # Variant 15: Minimal Icons
    """Seamless tileable pattern on cream #FAF8F5. Sparse VERY FAINT line-art
    icons: seated meditation pose, lotus symbol, simple brain/neural icon,
    friendly robot outline, Greek/Sanskrit letters. Icons at 8% opacity,
    thin strokes only. Large spacing between elements. Minimal, clean,
    readable background. Must tile seamlessly.""",

    # Variant 16: Etymology Focus
    """Seamless tileable on cream #FAF8F5. Extremely subtle floating letters
    from many scripts: Devanagari, Greek, Latin, Kanji - scattered sparsely.
    Occasional lotus or meditation silhouette. All at watermark opacity (10%).
    Maximum whitespace, minimal density. Clean and readable. Must tile
    seamlessly.""",

    # Variant 17: Tech Zen Balance
    """Seamless tileable on cream #FAF8F5. Ghostly watermark elements: neural
    network graphs, matrix-style character columns (very faint), enso circles,
    yogi silhouette. All extremely subtle at 8-12% opacity. Mostly empty
    background with sparse scattered elements. Prioritize readability.
    Must tile seamlessly.""",

    # === PURE WHITE + LARGE ARTIFACTS ===

    # Variant 18: Large Artifacts on White
    """Seamless tileable pattern on PURE WHITE background #FFFFFF. Features
    LARGE clearly visible silhouettes: meditating yogi figures (large,
    prominent), friendly robot outlines (large), neural network node
    diagrams with connected circles (large scale), lotus flower symbols,
    scattered multi-script letters (Sanskrit, Greek, Devanagari, π, Σ).
    Elements should be LARGE enough to see clearly without zooming -
    approximately 100-200 pixels each. Use medium gray tones (#888888)
    for the silhouettes. Sparse placement with good spacing between
    elements. Clean modern aesthetic. Must tile seamlessly.""",

    # Variant 19: Large Artifacts on TRUE WHITE (no tint)
    """Seamless tileable pattern. Background MUST be exactly RGB(255,255,255)
    pure white with ZERO color tint - no cream, no pink, no warm tones.
    Features LARGE gray silhouettes (#777777): meditating yogi figures,
    friendly robot outlines, neural network node diagrams, lotus flowers,
    Sanskrit/Greek/Devanagari letters, π, Σ symbols. Elements 100-200 pixels.
    CRITICAL: Background must be perfectly white #FFFFFF with no tint at all.
    Must tile seamlessly.""",
]

DARK_PROMPTS = [
    # Variant 0: Plain charcoal
    """Seamless tileable texture of dark charcoal paper with subtle depth variations
    and faint fabric texture. Warm black tones matching #1C1B1A. Elegant minimal.
    Suitable for dark mode website background. Must tile perfectly without seams.""",

    # Variant 1: Plain atmospheric
    """Seamless repeating pattern of dark handmade paper with subtle fiber texture.
    Warm charcoal black close to #1C1B1A. Faint ink wash shadows adding depth.
    Minimal contrast, sophisticated and moody. Must tile seamlessly.""",

    # Variant 2: Plain scholarly dark
    """Seamless tileable aged dark paper texture. Deep warm charcoal like old binding cloth.
    Subtle texture variations. Matching #1C1B1A warm black. Hints of leather or linen.
    Perfect for dark mode scholarly website background.""",

    # Variant 3: Fusion - Primary (handwritten ink style)
    """Seamless tileable dark charcoal paper with very subtle hand-drawn ink
    sketches in faded silver/cream tones. Delicate handwritten elements:
    small lotus sketches, flowing calligraphic strokes, constellation dots
    connected by thin lines, and loose mandala doodles. Like chalk or
    silver ink drawings faded on dark paper. Warm black #1C1B1A. Old
    scholar's dark notebook aesthetic. Must tile seamlessly.""",

    # Variant 4: Fusion - Botanical/Sacred
    """Seamless tileable dark handmade paper with faded hand-drawn botanical
    and geometric sketches. Ghostly cream-toned ink drawings of lotus
    flowers, flowing vines, and mandala patterns. Hints of handwritten
    script. Warm charcoal #1C1B1A. Like moonlit pages of an artist's
    sketchbook. Must tile perfectly.""",

    # Variant 5: Fusion - Manuscript/Network
    """Seamless tileable dark aged paper with ethereal hand-drawn diagrams
    in faded light ink. Sketch-like constellation patterns, flowing
    breath-wave drawings, and traces of calligraphic practice in multiple
    scripts. Deep warm charcoal. Like a midnight scholar's research notes.
    Must tile seamlessly.""",

    # Variant 6: Scientific Scholar (SUBTLE - Primary)
    """Seamless tileable dark charcoal paper with EXTREMELY FAINT chalk-like
    scholarly marks. Barely visible ghostly traces of: small equations and
    mathematical notation, interconnected node diagrams, fragments of text
    in different scripts (Greek, Sanskrit letters), coordinate axes, flowing
    wave sketches. All watermark-faint (5-10% visibility), like aged chalk
    nearly wiped away. Warm black #1C1B1A. Primarily texture with hints of
    a polymath's blackboard. Must tile seamlessly. Must not interfere with
    readability.""",

    # Variant 7: Etymology/Language Focus (SUBTLE)
    """Seamless tileable dark paper with extremely subtle linguistic traces.
    Ghostly marks of: letters from various alphabets (Devanagari, Greek,
    Latin shapes), word trees, calligraphic strokes, phonetic marks. All
    barely visible like moonlit chalk. Warm charcoal #1C1B1A. Like a
    midnight scholar's board. 5% opacity feel. Must tile seamlessly.""",

    # Variant 8: Research/Network Focus (SUBTLE)
    """Seamless tileable dark aged paper with extremely faint diagram traces.
    Barely visible: dot-and-line networks, small graphs, coordinate curves,
    arrow flows, scattered math symbols. Like chalk diagrams photographed
    in dim light. Warm charcoal #1C1B1A. Watermark-subtle. Must tile seamlessly.""",

    # Variant 9: Minimal Fusion (MOST SUBTLE)
    """Seamless tileable dark charcoal texture with extremely sparse, nearly
    invisible scholarly marks. Only occasional: single curves, isolated
    symbols, tiny dot clusters, faint letters. 95% pure texture, 5% ghostly
    scholarship hints. Warm black #1C1B1A. Maximum subtlety. Must tile seamlessly.""",

    # === NEW AESTHETIC: Zen + Matrix + Etymology (clean backgrounds) ===

    # Variant 10: Zen Matrix (Primary)
    """Seamless tileable pattern on clean dark charcoal #1C1B1A. Features
    VISIBLE floating elements in soft cream/silver tones: flowing zen
    brushstroke curves, falling characters from multiple scripts (Sanskrit,
    Greek, Japanese, Latin), interconnected neural network nodes with
    flowing lines, mathematical symbols. Elements medium-sized, clearly
    visible. Mix of digital matrix streams and meditative forms. Modern
    enlightened aesthetic. Must tile seamlessly.""",

    # Variant 11: Etymology Stream
    """Seamless tileable on clean dark charcoal #1C1B1A. Visible floating
    characters in cream/silver from many writing systems: Devanagari,
    Greek, Latin, Arabic, Chinese/Japanese, math notation. Medium-large
    characters in flowing streams. Some connected by thin flowing lines.
    Polyglot tapestry on dark background. Modern clean. Must tile seamlessly.""",

    # Variant 12: Neural Zen
    """Seamless tileable on dark charcoal #1C1B1A. Visible neural network
    nodes in soft cream with flowing organic connections, zen enso circles,
    flowing waves, scattered script characters. Medium-sized nodes connected
    by brush-like lines. Digital structure meets zen flow. Must tile seamlessly.""",

    # Variant 13: Enlightened Code
    """Seamless tileable on dark charcoal #1C1B1A. Matrix-inspired falling
    streams of characters in cream/green tones: code symbols, Sanskrit,
    Greek, math operators. Vertical streams with organic waviness. Medium
    readable characters. Technology meets enlightenment. Must tile seamlessly.""",

    # === SUBTLE WATERMARK VARIANTS (prioritize readability) ===

    # Variant 14: Subtle Fusion Watermark (Primary)
    """Seamless tileable watermark pattern on dark charcoal #1C1B1A. VERY SUBTLE
    ghostly silhouettes at 10-15% opacity in soft cream tones: meditating yogi
    figure, lotus flower outlines, neural network diagrams, robot silhouettes,
    scattered multi-script letters (Sanskrit, Greek, Devanagari). Elements
    EXTREMELY FAINT like watermarks. Sparse placement with lots of empty space.
    Must not interfere with text readability. Must tile seamlessly.""",

    # Variant 15: Minimal Icons
    """Seamless tileable pattern on dark charcoal #1C1B1A. Sparse VERY FAINT
    line-art icons in soft cream: seated meditation pose, lotus symbol, simple
    brain/neural icon, friendly robot outline, Greek/Sanskrit letters. Icons
    at 10% opacity, thin strokes only. Large spacing between elements.
    Minimal, clean, readable background. Must tile seamlessly.""",

    # Variant 16: Etymology Focus
    """Seamless tileable on dark charcoal #1C1B1A. Extremely subtle floating
    letters in cream from many scripts: Devanagari, Greek, Latin, Kanji -
    scattered sparsely. Occasional lotus or meditation silhouette. All at
    watermark opacity (10-12%). Maximum space, minimal density. Clean and
    readable. Must tile seamlessly.""",

    # Variant 17: Tech Zen Balance
    """Seamless tileable on dark charcoal #1C1B1A. Ghostly watermark elements
    in soft cream: neural network graphs, matrix-style character columns
    (very faint), enso circles, yogi silhouette. All extremely subtle at
    10-15% opacity. Mostly empty background with sparse scattered elements.
    Prioritize readability. Must tile seamlessly.""",

    # === PURE WHITE + LARGE ARTIFACTS ===

    # Variant 18: Large Artifacts on Dark
    """Seamless tileable pattern on dark charcoal #1C1B1A. Features LARGE
    clearly visible silhouettes in soft cream/white tones: meditating
    yogi figures (large, prominent), friendly robot outlines (large),
    neural network node diagrams with connected circles (large scale),
    lotus flower symbols, scattered multi-script letters (Sanskrit, Greek,
    Devanagari, π, Σ). Elements should be LARGE enough to see clearly -
    approximately 100-200 pixels each. Sparse placement with good spacing.
    Must tile seamlessly.""",

    # Variant 19: Large Artifacts on TRUE Dark (matching v19 light)
    """Seamless tileable pattern on dark charcoal #1C1B1A. Features LARGE
    cream/white silhouettes (#E8E0D8): meditating yogi figures, friendly
    robot outlines, neural network node diagrams, lotus flowers,
    Sanskrit/Greek/Devanagari letters, π, Σ symbols. Elements 100-200 pixels.
    Must tile seamlessly.""",
]


def generate_background(prompt: str, output_filename: str, client: genai.Client) -> bool:
    """Generate a single background image using Nano Banana Pro."""
    print(f"\nGenerating: {output_filename}")
    print(f"Prompt: {prompt[:100]}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        # Check for valid response
        if not response.candidates:
            print("No candidates in response")
            return False

        candidate = response.candidates[0]
        if not candidate.content or not candidate.content.parts:
            print("No content parts in response")
            print(f"Full response: {response}")
            return False

        # Extract and save the image
        for part in candidate.content.parts:
            if part.inline_data is not None:
                output_path = OUTPUT_DIR / output_filename

                # Save the image
                image_data = part.inline_data.data
                with open(output_path, "wb") as f:
                    f.write(image_data)

                print(f"Saved: {output_path}")
                return True
            elif part.text:
                print(f"Model response: {part.text}")

        print("No image generated in response")
        return False

    except Exception as e:
        print(f"Error generating image: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate AI backgrounds for website")
    parser.add_argument("--light-only", action="store_true", help="Generate only light mode background")
    parser.add_argument("--dark-only", action="store_true", help="Generate only dark mode background")
    parser.add_argument("--prompt-variant", type=int, default=19, choices=list(range(20)),
                        help="Prompt variant: 0-2=plain, 3-5=lotus, 6-9=scholarly, 10-13=zen, 14-17=subtle, 18=large, 19=TRUE white (default: 19)")
    parser.add_argument("--output-suffix", type=str, default="",
                        help="Suffix to add to output filenames (e.g., '-v4' creates bg-light-v4.png)")
    args = parser.parse_args()

    # Check API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment or .env file")
        sys.exit(1)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Initialize client
    client = genai.Client(api_key=api_key)

    print(f"Using model: {MODEL}")
    print(f"Prompt variant: {args.prompt_variant}")
    print(f"Output directory: {OUTPUT_DIR}")

    success = True

    # Determine output filenames
    suffix = args.output_suffix
    light_filename = f"bg-light{suffix}.png"
    dark_filename = f"bg-dark{suffix}.png"

    # Generate light mode background
    if not args.dark_only:
        light_prompt = LIGHT_PROMPTS[args.prompt_variant]
        if not generate_background(light_prompt, light_filename, client):
            success = False

    # Generate dark mode background
    if not args.light_only:
        dark_prompt = DARK_PROMPTS[args.prompt_variant]
        if not generate_background(dark_prompt, dark_filename, client):
            success = False

    if success:
        print("\n=== Generation complete! ===")
        print("Next steps:")
        print("1. Check the generated images in static/images/")
        print("2. Run 'hugo server' to preview")
        print("3. If not satisfied, try: python scripts/generate-backgrounds.py --prompt-variant 1")
    else:
        print("\n=== Some generations failed ===")
        print("Check the error messages above and try again.")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
