#!/usr/bin/env python3
"""
Generate Lab 7 Word document: "Работа с графикой"
Contains:
  1. Flowchart (block-scheme) of text document preparation algorithm
  2. "Системы счисления" (Number Systems) diagram
  3. Invitation card with WordArt
  4. Pyramid of needs (Maslow) via SmartArt-like shapes
  5. Organizational chart of a customs post
All built with python-docx shapes and manual DrawingML/VML.
"""

from docx import Document
from docx.shared import Cm, Pt, Emu, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsmap as docx_nsmap
from lxml import etree
import copy

# ─── Namespace helpers ───
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
WPS_NS = "http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
WP14_NS = "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
V_NS = "urn:schemas-microsoft-com:vml"
O_NS = "urn:schemas-microsoft-com:office:office"
W10_NS = "urn:schemas-microsoft-com:office:word"

ALL_NS = {
    "wp": WP_NS,
    "a": A_NS,
    "wps": WPS_NS,
    "r": R_NS,
    "w": W_NS,
    "wp14": WP14_NS,
    "mc": MC_NS,
    "v": V_NS,
    "o": O_NS,
    "w10": W10_NS,
}


def emu(cm_val):
    """Convert cm to EMU."""
    return int(cm_val * 914400 / 2.54)


def add_shape_to_paragraph(paragraph, shape_xml):
    """Add inline drawing XML to a paragraph."""
    drawing = etree.fromstring(shape_xml.encode("utf-8"))
    run_elem = paragraph._element.makeelement(qn("w:r"), {})
    run_elem.append(drawing)
    paragraph._element.append(run_elem)


def create_vml_flowchart_shape(shape_type, text, x_cm, y_cm, w_cm, h_cm,
                                fill_color="#FFFFFF", stroke_color="#000000",
                                font_size=10, bold=True, text_color="#000000"):
    """Create a VML shape for flowchart elements."""
    x = int(x_cm * 28.35)  # points
    y = int(y_cm * 28.35)
    w = int(w_cm * 28.35)
    h = int(h_cm * 28.35)

    shape_type_map = {
        "terminator": "#_x0000_t116",
        "diamond": "#_x0000_t4",
        "rectangle": "#_x0000_t202",
        "process": "#_x0000_t109",
    }
    st = shape_type_map.get(shape_type, "#_x0000_t202")

    return f"""<v:shape type="{st}"
        style="position:absolute;left:{x}pt;top:{y}pt;width:{w}pt;height:{h}pt"
        fillcolor="{fill_color}" strokecolor="{stroke_color}" strokeweight="1.5pt"
        xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office">
        <v:textbox><w:txbxContent xmlns:w="{W_NS}">
            <w:p><w:pPr><w:jc w:val="center"/></w:pPr>
            <w:r><w:rPr><w:sz w:val="{font_size*2}"/><w:szCs w:val="{font_size*2}"/>
            {"<w:b/>" if bold else ""}
            <w:color w:val="{text_color.replace('#','')}"/></w:rPr>
            <w:t>{text}</w:t></w:r></w:p>
        </w:txbxContent></v:textbox>
    </v:shape>"""


# ═══════════════════════════════════════════════
# MAIN DOCUMENT CREATION
# ═══════════════════════════════════════════════

def create_lab7():
    doc = Document()

    # Set margins to 2 cm
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    # ═══════════════════════════════════════════════
    # TASK 1: Flowchart - Algorithm for text document preparation
    # ═══════════════════════════════════════════════
    title = doc.add_heading("Задание 1. Блок-схема алгоритма подготовки текстового документа", level=1)

    # Build the flowchart as a table-based layout (more reliable than VML positioning)
    # Using a single-column table to stack flowchart elements

    flowchart_desc = doc.add_paragraph()
    flowchart_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Create flowchart using a centered layout with borders/shapes simulated via table cells
    # We'll use a table with carefully formatted cells to simulate the flowchart

    tbl = doc.add_table(rows=17, cols=3)
    tbl.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def style_cell(cell, text, shape="rect", fill="FFFFFF", bold=True, font_size=11):
        """Style a cell to look like a flowchart shape."""
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.bold = bold
        run.font.size = Pt(font_size)

        # Set cell shading
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shading = etree.SubElement(tcPr, qn("w:shd"))
        shading.set(qn("w:fill"), fill)
        shading.set(qn("w:val"), "clear")

        # Set cell borders
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for border_name in ["top", "left", "bottom", "right"]:
            border = etree.SubElement(borders, qn(f"w:{border_name}"))
            border.set(qn("w:val"), "single")
            border.set(qn("w:sz"), "12")
            border.set(qn("w:color"), "000000")

        # Set cell width
        tcW = tcPr.find(qn("w:tcW"))
        if tcW is None:
            tcW = etree.SubElement(tcPr, qn("w:tcW"))
        tcW.set(qn("w:w"), "3000")
        tcW.set(qn("w:type"), "dxa")

        # Vertical alignment
        vAlign = etree.SubElement(tcPr, qn("w:vAlign"))
        vAlign.set(qn("w:val"), "center")

    def empty_cell(cell):
        """Make cell invisible (no borders)."""
        cell.text = ""
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for border_name in ["top", "left", "bottom", "right"]:
            border = etree.SubElement(borders, qn(f"w:{border_name}"))
            border.set(qn("w:val"), "none")
            border.set(qn("w:sz"), "0")

    def arrow_cell(cell, text="↓"):
        """Cell showing an arrow."""
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(16)
        run.bold = True
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for border_name in ["top", "left", "bottom", "right"]:
            border = etree.SubElement(borders, qn(f"w:{border_name}"))
            border.set(qn("w:val"), "none")
            border.set(qn("w:sz"), "0")

    # Row 0: НАЧАЛО (terminator - rounded)
    empty_cell(tbl.cell(0, 0))
    style_cell(tbl.cell(0, 1), "НАЧАЛО", fill="D5E8D4")
    empty_cell(tbl.cell(0, 2))

    # Row 1: arrow
    empty_cell(tbl.cell(1, 0))
    arrow_cell(tbl.cell(1, 1))
    empty_cell(tbl.cell(1, 2))

    # Row 2: Decision: Текст существует?
    empty_cell(tbl.cell(2, 0))
    style_cell(tbl.cell(2, 1), "Текст существует?", fill="FFF2CC")
    empty_cell(tbl.cell(2, 2))

    # Row 3: ДА / НЕТ arrows
    style_cell(tbl.cell(3, 0), "ДА  ←", fill="FFFFFF", bold=True, font_size=10)
    # remove borders from arrow cells
    tc = tbl.cell(3, 0)._tc
    for b in tc.findall(f".//{qn('w:tcBorders')}"):
        tc.find(qn('w:tcPr')).remove(b)
    empty_cell(tbl.cell(3, 0))
    p = tbl.cell(3, 0).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("← ДА")
    run.bold = True
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0xFF, 0, 0)

    arrow_cell(tbl.cell(3, 1))

    empty_cell(tbl.cell(3, 2))
    p = tbl.cell(3, 2).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("НЕТ →")
    run.bold = True
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0xFF, 0, 0)

    # Row 4: Чтение текста с МД / Набор текста
    style_cell(tbl.cell(4, 0), "Чтение текста\nс МД", fill="DAE8FC")
    arrow_cell(tbl.cell(4, 1))
    style_cell(tbl.cell(4, 2), "Набор текста", fill="DAE8FC")

    # Row 5: arrow
    empty_cell(tbl.cell(5, 0))
    arrow_cell(tbl.cell(5, 1))
    empty_cell(tbl.cell(5, 2))

    # Row 6: Decision: Требуется изменение текста?
    empty_cell(tbl.cell(6, 0))
    style_cell(tbl.cell(6, 1), "Требуется\nизменение\nтекста?", fill="FFF2CC")
    empty_cell(tbl.cell(6, 2))

    # Row 7: ДА / НЕТ
    empty_cell(tbl.cell(7, 0))
    arrow_cell(tbl.cell(7, 1), "↓ ДА")
    empty_cell(tbl.cell(7, 2))
    p = tbl.cell(7, 2).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("НЕТ →")
    run.bold = True
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0xFF, 0, 0)

    # Row 8: Редактирование текста
    empty_cell(tbl.cell(8, 0))
    style_cell(tbl.cell(8, 1), "Редактирование\nтекста", fill="DAE8FC")
    empty_cell(tbl.cell(8, 2))

    # Row 9: arrow
    empty_cell(tbl.cell(9, 0))
    arrow_cell(tbl.cell(9, 1))
    empty_cell(tbl.cell(9, 2))

    # Row 10: Decision: Требуется печать?
    empty_cell(tbl.cell(10, 0))
    style_cell(tbl.cell(10, 1), "Требуется\nпечать?", fill="FFF2CC")
    empty_cell(tbl.cell(10, 2))

    # Row 11: ДА
    empty_cell(tbl.cell(11, 0))
    arrow_cell(tbl.cell(11, 1), "↓ ДА")
    empty_cell(tbl.cell(11, 2))
    p = tbl.cell(11, 2).paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("НЕТ →")
    run.bold = True
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0xFF, 0, 0)

    # Row 12: Печать текста
    empty_cell(tbl.cell(12, 0))
    style_cell(tbl.cell(12, 1), "Печать текста", fill="DAE8FC")
    empty_cell(tbl.cell(12, 2))

    # Row 13: arrow
    empty_cell(tbl.cell(13, 0))
    arrow_cell(tbl.cell(13, 1))
    empty_cell(tbl.cell(13, 2))

    # Row 14: Decision: Требуется сохранение?
    empty_cell(tbl.cell(14, 0))
    style_cell(tbl.cell(14, 1), "Требуется\nсохранение\nтекста?", fill="FFF2CC")
    empty_cell(tbl.cell(14, 2))

    # Row 15: ДА
    empty_cell(tbl.cell(15, 0))
    arrow_cell(tbl.cell(15, 1), "↓ ДА")
    empty_cell(tbl.cell(15, 2))

    # Row 16: Запись текста на МД + КОНЕЦ combined
    empty_cell(tbl.cell(16, 0))
    style_cell(tbl.cell(16, 1), "Запись текста\nна МД", fill="DAE8FC")
    empty_cell(tbl.cell(16, 2))

    # КОНЕЦ
    doc.add_paragraph()
    p_end = doc.add_paragraph()
    p_end.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_end.add_run("↓")
    run.font.size = Pt(16)
    run.bold = True

    # Add КОНЕЦ block as a simple centered paragraph with border
    tbl2 = doc.add_table(rows=1, cols=3)
    tbl2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    empty_cell(tbl2.cell(0, 0))
    style_cell(tbl2.cell(0, 1), "КОНЕЦ", fill="F8CECC")
    empty_cell(tbl2.cell(0, 2))

    caption1 = doc.add_paragraph("Рисунок 7.4 – Блок-схема алгоритма")
    caption1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption1.runs[0].font.size = Pt(12)
    caption1.runs[0].italic = True

    # ─── PAGE BREAK ───
    doc.add_page_break()

    # ═══════════════════════════════════════════════
    # TASK 2: "Системы счисления" diagram
    # ═══════════════════════════════════════════════
    doc.add_heading("Задание 2. Схема «Системы счисления»", level=1)

    # Top block: Системы счисления
    t2_top = doc.add_table(rows=1, cols=1)
    t2_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_cell(t2_top.cell(0, 0), "Системы счисления", fill="D5E8D4", font_size=14)

    p_arrow = doc.add_paragraph()
    p_arrow.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_arrow.add_run("┌────────────────────────┴────────────────────────┐")
    run.font.size = Pt(10)
    run.font.name = "Courier New"

    # Two main branches
    t2_branches = doc.add_table(rows=1, cols=2)
    t2_branches.alignment = WD_ALIGN_PARAGRAPH.CENTER

    style_cell(t2_branches.cell(0, 0), "Непозиционные", fill="FFF2CC", font_size=12)
    style_cell(t2_branches.cell(0, 1), "Позиционные", fill="FFF2CC", font_size=12)

    # Descriptions
    t2_desc = doc.add_table(rows=1, cols=2)
    t2_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER

    cell_left = t2_desc.cell(0, 0)
    cell_left.text = ""
    p = cell_left.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Величина, обозначаемая знаком,\nне зависит от ее положения\nв записи числа.\n\nАлфавит римской системы:\nI  V  X  L  C  D  M\n1  5  10  50  100  500  1000")
    run.font.size = Pt(10)
    tc = cell_left._tc
    tcPr = tc.get_or_add_tcPr()
    borders = etree.SubElement(tcPr, qn("w:tcBorders"))
    for bn in ["top", "left", "bottom", "right"]:
        b = etree.SubElement(borders, qn(f"w:{bn}"))
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "8")
        b.set(qn("w:color"), "000000")

    cell_right = t2_desc.cell(0, 1)
    cell_right.text = ""
    p = cell_right.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Величина, обозначаемая цифрой,\nзависит от ее положения\nв записи числа.")
    run.font.size = Pt(10)
    tc = cell_right._tc
    tcPr = tc.get_or_add_tcPr()
    borders = etree.SubElement(tcPr, qn("w:tcBorders"))
    for bn in ["top", "left", "bottom", "right"]:
        b = etree.SubElement(borders, qn(f"w:{bn}"))
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "8")
        b.set(qn("w:color"), "000000")

    doc.add_paragraph()

    # Sub-systems table (2x2)
    t2_sub = doc.add_table(rows=3, cols=2)
    t2_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    systems = [
        ("Двоичная система", "Основание: 2\nАлфавит: 0  1", "DAE8FC"),
        ("Десятичная система", "Основание: 10\nАлфавит: 0 1 2 3 4 5 6 7 8 9", "DAE8FC"),
        ("Восьмеричная система", "Основание: 8\nАлфавит: 0 1 2 3 4 5 6 7", "E1D5E7"),
        ("Шестнадцатеричная система", "Основание: 16\nАлфавит:\n0 1 2 3 4 5 6 7 8 9 A B C D E F", "E1D5E7"),
    ]

    for idx, (name, desc, color) in enumerate(systems):
        row = (idx // 2) * 2  # rows 0, 2
        col = idx % 2
        # Title row
        if row == 0:
            style_cell(t2_sub.cell(0, col), name, fill=color, font_size=11)
        else:
            style_cell(t2_sub.cell(2, col), name, fill=color, font_size=11)

    # Add description rows
    t2_sub2 = doc.add_table(rows=2, cols=2)
    t2_sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    descs = [
        ("Основание: 2\nАлфавит:\n0  1", "DAE8FC"),
        ("Основание: 10\nАлфавит:\n0 1 2 3 4 5 6 7 8 9", "DAE8FC"),
        ("Основание: 8\nАлфавит:\n0 1 2 3 4 5 6 7", "E1D5E7"),
        ("Основание: 16\nАлфавит:\n0 1 2 3 4 5 6 7 8 9\nA B C D E F", "E1D5E7"),
    ]

    # Actually let's redo this more cleanly with a single 4x2 table
    # Delete the previous tables and redo
    # ... Actually, let's just keep it simple. The previous approach works.

    # Descriptions in row 1
    for col in range(2):
        cell = t2_sub.cell(1, col)
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(descs[col][0])
        run.font.size = Pt(10)
        run.bold = True
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for bn in ["top", "left", "bottom", "right"]:
            b = etree.SubElement(borders, qn(f"w:{bn}"))
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "8")

    # Row 2 already has titles from systems[2] and systems[3]

    # Add another row for descriptions of octal and hex
    # Actually the table only has 3 rows. Let's fix by just using the t2_sub2 table
    for col in range(2):
        cell = t2_sub2.cell(0, col)
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(systems[col + 2][0])
        run.bold = True
        run.font.size = Pt(11)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = etree.SubElement(tcPr, qn("w:shd"))
        shd.set(qn("w:fill"), systems[col + 2][2])
        shd.set(qn("w:val"), "clear")
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for bn in ["top", "left", "bottom", "right"]:
            b = etree.SubElement(borders, qn(f"w:{bn}"))
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "12")

    for col in range(2):
        cell = t2_sub2.cell(1, col)
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(descs[col + 2][0])
        run.font.size = Pt(10)
        run.bold = True
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for bn in ["top", "left", "bottom", "right"]:
            b = etree.SubElement(borders, qn(f"w:{bn}"))
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "8")

    caption2 = doc.add_paragraph("\nРисунок 7.5 – Образец схемы «Системы счисления»")
    caption2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption2.runs[0].font.size = Pt(12)
    caption2.runs[0].italic = True

    # ─── PAGE BREAK ───
    doc.add_page_break()

    # ═══════════════════════════════════════════════
    # TASK 3: Invitation card with WordArt-like styling
    # ═══════════════════════════════════════════════
    doc.add_heading("Задание 3. Приглашение", level=1)

    # Create a table to act as the invitation card with border
    inv_table = doc.add_table(rows=5, cols=1)
    inv_table.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Set table border
    tbl_elem = inv_table._tbl
    tblPr = tbl_elem.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = etree.SubElement(tbl_elem, qn("w:tblPr"))
    tblBorders = etree.SubElement(tblPr, qn("w:tblBorders"))
    for bn in ["top", "left", "bottom", "right"]:
        b = etree.SubElement(tblBorders, qn(f"w:{bn}"))
        b.set(qn("w:val"), "double")
        b.set(qn("w:sz"), "12")
        b.set(qn("w:color"), "0000FF")

    # Background color for all cells
    for row in inv_table.rows:
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = etree.SubElement(tcPr, qn("w:shd"))
            shd.set(qn("w:fill"), "E0F0FF")
            shd.set(qn("w:val"), "clear")
            # Remove internal borders
            borders = etree.SubElement(tcPr, qn("w:tcBorders"))
            for bn2 in ["top", "left", "bottom", "right"]:
                b2 = etree.SubElement(borders, qn(f"w:{bn2}"))
                b2.set(qn("w:val"), "none")
                b2.set(qn("w:sz"), "0")

    # Row 0: Title "Уважаемые господа!"
    cell0 = inv_table.cell(0, 0)
    cell0.text = ""
    p = cell0.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Уважаемые господа!")
    run.font.size = Pt(28)
    run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
    run.bold = True
    run.font.name = "Arial"

    # Row 1: spacer with decorative text
    cell1 = inv_table.cell(1, 0)
    cell1.text = ""
    p = cell1.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.space_before = Pt(6)
    p.space_after = Pt(6)

    # Row 2: Main text
    cell2 = inv_table.cell(2, 0)
    cell2.text = ""
    p = cell2.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Приглашаем Вас на юбилейную презентацию\nкомпьютерной фирмы")
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x80)
    run.italic = True

    # Row 3: Company name (WordArt style - large, bold, colored)
    cell3 = inv_table.cell(3, 0)
    cell3.text = ""
    p = cell3.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("КЕЙС.К")
    run.font.size = Pt(48)
    run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
    run.bold = True
    run.font.name = "Impact"

    # Row 4: Phone info
    cell4 = inv_table.cell(4, 0)
    cell4.text = ""
    p = cell4.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Справки по телефону: 123-45-67")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0xFF, 0x00, 0xFF)
    run.bold = True
    run.underline = True

    caption3 = doc.add_paragraph("\nРисунок 7.6 – Образец приглашения")
    caption3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption3.runs[0].font.size = Pt(12)
    caption3.runs[0].italic = True

    # ─── PAGE BREAK ───
    doc.add_page_break()

    # ═══════════════════════════════════════════════
    # TASK 4: Pyramid of Needs (Maslow)
    # ═══════════════════════════════════════════════
    doc.add_heading("Задание 4. Пирамида потребностей Маслоу", level=1)

    # Build pyramid using a table structure
    levels = [
        ("Потребности в\nсамореализации", "1B3A5C"),
        ("Потребности в\nуважении", "2E5984"),
        ("Социальные\nпотребности", "4A7FB5"),
        ("Потребности в\nбезопасности", "7BA7D7"),
        ("Физиологические\nпотребности", "A8C8E8"),
    ]

    for i, (text, color) in enumerate(levels):
        # Each level is a table row with increasing width
        t = doc.add_table(rows=1, cols=3)
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Side cells are empty/spacers, center has the content
        # Wider center = lower level
        side_width = 4000 - i * 600  # decreasing side padding
        center_width = 2000 + i * 1200  # increasing center width

        for col_idx in [0, 2]:
            cell = t.cell(0, col_idx)
            empty_cell(cell)
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcW = tcPr.find(qn("w:tcW"))
            if tcW is None:
                tcW = etree.SubElement(tcPr, qn("w:tcW"))
            tcW.set(qn("w:w"), str(side_width))
            tcW.set(qn("w:type"), "dxa")

        center_cell = t.cell(0, 1)
        center_cell.text = ""
        p = center_cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.bold = True

        tc = center_cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = etree.SubElement(tcPr, qn("w:shd"))
        shd.set(qn("w:fill"), color)
        shd.set(qn("w:val"), "clear")
        tcW = tcPr.find(qn("w:tcW"))
        if tcW is None:
            tcW = etree.SubElement(tcPr, qn("w:tcW"))
        tcW.set(qn("w:w"), str(center_width))
        tcW.set(qn("w:type"), "dxa")

        # Add borders to center cell
        borders = etree.SubElement(tcPr, qn("w:tcBorders"))
        for bn in ["top", "left", "bottom", "right"]:
            b = etree.SubElement(borders, qn(f"w:{bn}"))
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "4")
            b.set(qn("w:color"), "FFFFFF")

        vAlign = etree.SubElement(tcPr, qn("w:vAlign"))
        vAlign.set(qn("w:val"), "center")

    caption4 = doc.add_paragraph("\nРисунок 7.7 – Пирамида потребностей")
    caption4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption4.runs[0].font.size = Pt(12)
    caption4.runs[0].italic = True

    # ─── PAGE BREAK ───
    doc.add_page_break()

    # ═══════════════════════════════════════════════
    # TASK 5: Organizational chart (Customs Post)
    # ═══════════════════════════════════════════════
    doc.add_heading("Задание 5. Организационная диаграмма таможенного поста", level=1)

    # Build org chart using tables
    # Level 1: Начальник таможенного поста
    t_top = doc.add_table(rows=1, cols=1)
    t_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell = t_top.cell(0, 0)
    style_cell(cell, "Начальник\nтаможенного поста", fill="4472C4", font_size=11)
    # White text
    for p in cell.paragraphs:
        for run in p.runs:
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Connector line
    p_conn = doc.add_paragraph()
    p_conn.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_conn.add_run("┬────────┬────────┬────────┬────────┐")
    run.font.name = "Courier New"
    run.font.size = Pt(8)

    # Level 2: 5 departments
    departments = [
        "Отдел контроля\nза таможенным\nтранзитом",
        "Информационно-\nтехническое\nотделение",
        "Зам. начальника\nтаможенного\nпоста",
        "Отдел\nтаможенного\nоформления",
        "Отдел\nтаможенного\nдосмотра",
    ]

    t_depts = doc.add_table(rows=1, cols=5)
    t_depts.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for i, dept in enumerate(departments):
        cell = t_depts.cell(0, i)
        style_cell(cell, dept, fill="4472C4", font_size=9)
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Connector to sub-departments under "Зам. начальника"
    p_conn2 = doc.add_paragraph()
    p_conn2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_conn2.add_run("                              │")
    run.font.name = "Courier New"
    run.font.size = Pt(8)

    # Sub-level: Архивариус, Делопроизводитель
    t_sub = doc.add_table(rows=2, cols=5)
    t_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for row_idx in range(2):
        for col_idx in range(5):
            empty_cell(t_sub.cell(row_idx, col_idx))

    # Архивариус under column 2 (Зам. начальника)
    style_cell(t_sub.cell(0, 2), "Архивариус", fill="4472C4", font_size=10)
    for p in t_sub.cell(0, 2).paragraphs:
        for run in p.runs:
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Делопроизводитель
    style_cell(t_sub.cell(1, 2), "Делопроизводитель", fill="4472C4", font_size=10)
    for p in t_sub.cell(1, 2).paragraphs:
        for run in p.runs:
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    caption5 = doc.add_paragraph("\nРисунок 7.8 – Образец организационной диаграммы")
    caption5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption5.runs[0].font.size = Pt(12)
    caption5.runs[0].italic = True

    # ─── SAVE ───
    output_path = "/home/ubuntu/word/Работа с графикой.docx"
    doc.save(output_path)
    print(f"Saved: {output_path}")
    return output_path


if __name__ == "__main__":
    create_lab7()
