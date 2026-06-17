from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path


input_file = Path(
    "research/report/quant_research_report.md"
)

output_file = Path(
    "research/report/Quant_Research_Report.pdf"
)

doc = SimpleDocTemplate(
    str(output_file)
)

styles = getSampleStyleSheet()

story = []

with open(input_file, "r") as f:
    text = f.read()

for line in text.split("\n"):

    line = line.strip()

    if not line:
        story.append(Spacer(1, 6))
        continue

    if line.startswith("# "):
        story.append(
            Paragraph(
                line.replace("# ", ""),
                styles["Title"],
            )
        )

    elif line.startswith("## "):
        story.append(
            Paragraph(
                line.replace("## ", ""),
                styles["Heading1"],
            )
        )

    elif line.startswith("### "):
        story.append(
            Paragraph(
                line.replace("### ", ""),
                styles["Heading2"],
            )
        )

    else:
        story.append(
            Paragraph(
                line,
                styles["BodyText"],
            )
        )

doc.build(story)

print(
    f"PDF generated: {output_file}"
)