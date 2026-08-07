import os
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

from src.services.patient_service import (
    get_patient_appointments,
    get_patient_referrals,
    get_patient_lab_results,
    get_patient_documents
)

def style_table(table, header_color):

    style = TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("BACKGROUND", (0, 0), (-1, 0), header_color),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

        ("TOPPADDING", (0, 0), (-1, 0), 8),

        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),

        ("TOPPADDING", (0, 1), (-1, -1), 6),

        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ])

    for row in range(1, len(table._cellvalues)):

        if row % 2 == 0:

            style.add(
                "BACKGROUND",
                (0, row),
                (-1, row),
                colors.HexColor("#F8F9FA")
            )

    table.setStyle(style)

def add_page_number(canvas, doc):

    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        9
    )

    canvas.drawString(
        40,
        20,
        "Healthcare Patient Registration System | Confidential"
    )

    canvas.drawRightString(
        560,
        20,
        f"Page {doc.page}"
    )

    canvas.restoreState()

def safe(value):

    if value is None:
        return "N/A"

    if str(value).strip() == "":
        return "N/A"

    return str(value)

def generate_patient_report(patient):

    reports_folder = "reports"

    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    filename = (
        f"{patient.first_name}_"
        f"{patient.last_name}_"
        f"Report_{timestamp}.pdf"
    )

    path = os.path.join(
        reports_folder,
        filename
    )

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(path)

    story = []

    appointments = get_patient_appointments(
        patient.patient_id
    )

    referrals = get_patient_referrals(
        patient.patient_id
    )

    labs = get_patient_lab_results(
        patient.patient_id
    )

    documents = get_patient_documents(
        patient.patient_id
    )

    appointment_count = len(appointments)
    referral_count = len(referrals)
    lab_count = len(labs)
    document_count = len(documents)

    story.append(
        Paragraph(
            "<font size=24><b>Healthcare Patient Report</b></font>",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Patient:</b> {patient.first_name} {patient.last_name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Patient ID:</b> {patient.patient_id}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1,0.5*inch)
    )

    story.append(
        Paragraph(
            "This report contains the patient's demographic information, appointments, referrals, laboratory results, and uploaded documents.",
            styles["Italic"]
        )
    )

    story.append(
        Spacer(1,0.15*inch)
    )

    story.append(
        Paragraph(
            "<font color='red'><b>CONFIDENTIAL:</b></font> This report contains protected personal health information and is intended only for authorized healthcare personnel.",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1,0.5*inch)
    )

    story.append(PageBreak())

    story.append(
        Paragraph(
            "<b>Patient Summary</b>",
            styles["Heading2"]
        )
    )

    summary_table = Table([

        ["Appointments", appointment_count],

        ["Referrals", referral_count],

        ["Lab Results", lab_count],

        ["Documents", document_count]

    ])

    summary_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EAECEE")),

        ("BOTTOMPADDING",(0,0),(-1,-1),6),

        ("TOPPADDING",(0,0),(-1,-1),6)

    ]))

    story.append(summary_table)

    story.append(
        Spacer(1,0.35*inch)
    )

    story.append(
        Paragraph(
            "<b>Patient Information</b>",
            styles["Heading2"]
        )
    )

    

    patient_table = Table([

        ["Patient ID", safe(patient.patient_id)],

        ["Name", f"{safe(patient.first_name)} {safe(patient.last_name)}"],

        ["Date of Birth", safe(str(patient.date_of_birth))],

        ["Sex", safe(patient.sex)],

        ["Blood Type", safe(patient.blood_type)],

        ["Phone", safe(patient.phone)],

        ["Email", safe(patient.email)],

        ["Health Card", safe(patient.health_card_number)],

        ["Family Doctor", safe(patient.family_doctor)]

    ])

    patient_table.setStyle(TableStyle([

        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

        ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#EAECEE")),

        ("BOTTOMPADDING", (0,0), (-1,-1), 6),

        ("TOPPADDING", (0,0), (-1,-1), 6),

        ("VALIGN", (0,0), (-1,-1), "MIDDLE")

    ]))

    story.append(patient_table)
    story.append(
        Spacer(1,0.35*inch)
    )

    story.append(
        Paragraph(
            "Appointments",
            styles["Heading2"]
        )
    )

    rows = [[
        "Date",
        "Time",
        "Reason",
        "Status",
        "Room"
    ]]

    for appointment in appointments:

        rows.append([

            str(appointment.appointment_date),

            str(appointment.appointment_time)[:5],

            safe(appointment.appointment_reason),

            safe(appointment.appointment_status),

            str(appointment.room_number)

        ])

    if len(rows) == 1:

        story.append(
            Paragraph(
                "No appointments found.",
                styles["Italic"]
            )
        )

    else:

        table = Table(rows)
        style_table(
            table,
            colors.HexColor("#2E86C1")
        )
        story.append(table)
        story.append(
            Spacer(1,0.1*inch)
        )

        story.append(
            Paragraph(
                f"<b>Total Appointments:</b> {len(appointments)}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1,0.3*inch)
    )

    story.append(
        Paragraph(
            "Referrals",
            styles["Heading2"]
        )
    )

    rows = [[
        "Clinic",
        "Department",
        "Date",
        "Status"
    ]]

    for referral in referrals:

        rows.append([

            safe(referral.referring_clinic),

            safe(referral.department_name),

            str(referral.referral_date),

            safe(referral.status)

        ])

    table = Table(
        rows,
        colWidths=[2.5*inch, 1.8*inch, 1.2*inch, 1.0*inch]
    )

    style_table(
        table,
        colors.HexColor("#D68910")
    )

    story.append(table)

    story.append(
        Spacer(1,0.1*inch)
    )

    story.append(
        Paragraph(
            f"<b>Total Referrals:</b> {len(referrals)}",
            styles["BodyText"]
        )
    )
    story.append(
        Spacer(1,0.30*inch)
    )

    story.append(
        Paragraph(
            "Lab Results",
            styles["Heading2"]
        )
    )

    rows = [[
        "Date",
        "Test",
        "Result",
        "Notes"
    ]]

    for lab in labs:

        rows.append([

            str(lab.test_date),

            safe(lab.test_name),

            safe(lab.result),

            safe(lab.notes)

        ])

    table = Table(
        rows,
        colWidths=[1.2*inch, 2.2*inch, 1.0*inch, 2.6*inch]
    )

    style_table(
        table,
        colors.HexColor("#229954")
    )

    story.append(table)
    story.append(
        Spacer(1,0.1*inch)
    )

    story.append(
        Paragraph(
            f"<b>Total Lab Results:</b> {len(labs)}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1,0.30*inch)
    )

    story.append(
        Paragraph(
            "Documents",
            styles["Heading2"]
        )
    )

    rows = [[
        "Type",
        "Filename",
        "Upload Date",
        "Uploaded By"
    ]]

    for document in documents:

        rows.append([

            safe(document.document_type),

            safe(document.file_name),

            str(document.upload_date).replace("T", " ")[:16],

            safe(document.uploaded_by)

        ])

    table = Table(
        rows,
        colWidths=[1.5*inch, 2.5*inch, 1.5*inch, 1.5*inch]
    )

    style_table(
        table,
        colors.HexColor("#CA6F1E")
    )

    story.append(table)
    story.append(
        Spacer(1,0.1*inch)
    )

    story.append(
        Paragraph(
            f"<b>Total Documents:</b> {len(documents)}",
            styles["BodyText"]
        )
    )
    
            
    doc.build(

        story,

        onFirstPage=add_page_number,

        onLaterPages=add_page_number

    )

    return os.path.abspath(path)

