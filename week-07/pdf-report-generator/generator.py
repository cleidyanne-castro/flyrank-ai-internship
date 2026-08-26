import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


REQUIRED_FIELDS = ("project_name", "role", "summary", "technologies", "links", "outcomes")


def validate_project(data: dict) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    if not isinstance(data["technologies"], list) or not data["technologies"]:
        raise ValueError("technologies must be a non-empty list")
    if not isinstance(data["links"], list):
        raise ValueError("links must be a list")
    if not isinstance(data["outcomes"], list) or not data["outcomes"]:
        raise ValueError("outcomes must be a non-empty list")


def make_styles():
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("ReportTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=24, leading=29, textColor=colors.HexColor("#172323"), alignment=TA_LEFT, spaceAfter=8),
        "subtitle": ParagraphStyle("ReportSubtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=15, textColor=colors.HexColor("#677270"), spaceAfter=18),
        "heading": ParagraphStyle("ReportHeading", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.HexColor("#172323"), spaceBefore=14, spaceAfter=7),
        "body": ParagraphStyle("ReportBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=15, textColor=colors.HexColor("#263333"), spaceAfter=8),
        "small": ParagraphStyle("ReportSmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor("#677270")),
        "bullet": ParagraphStyle("ReportBullet", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=14, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#263333"), spaceAfter=4),
    }


def link_markup(label: str, url: str) -> str:
    return f'<link href="{url}" color="#1D4ED8"><u>{label}</u></link>'


def build_story(data: dict):
    validate_project(data)
    styles = make_styles()
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    story = [
        Paragraph(data["project_name"], styles["title"]),
        Paragraph(f'{data["role"]} | Generated {generated}', styles["subtitle"]),
        Paragraph("Summary", styles["heading"]),
        Paragraph(data["summary"], styles["body"]),
        Paragraph("Technologies", styles["heading"]),
        Paragraph(" | ".join(data["technologies"]), styles["body"]),
        Paragraph("Outcomes", styles["heading"]),
    ]
    story.extend(Paragraph(f"- {outcome}", styles["bullet"]) for outcome in data["outcomes"])
    if data["links"]:
        story.append(Paragraph("Links", styles["heading"]))
        link_rows = [[Paragraph(link_markup(item["label"], item["url"]), styles["body"])] for item in data["links"]]
        links_table = Table(link_rows, colWidths=[160 * mm])
        links_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7F7")),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5D4")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#E4E9E8")),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(links_table)
    story.append(Spacer(1, 8))
    story.append(Paragraph("The report keeps project data separate from the layout template so the same generator can be reused for another case study.", styles["small"]))
    return story


def generate_report(data: dict, output_path: str | Path) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=25 * mm, leftMargin=25 * mm, topMargin=22 * mm, bottomMargin=20 * mm, title=data.get("project_name", "Project report"))
    document.build(build_story(data))
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a recruiter-friendly project PDF")
    parser.add_argument("--input", required=True, help="Path to a project JSON file")
    parser.add_argument("--output", required=True, help="Path for the generated PDF")
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    generate_report(data, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
