from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

from reportlab.lib import colors

from datetime import datetime

from tkinter import filedialog
from tkinter import messagebox


def add_page_number(canvas, doc):

    canvas.saveState()


    # Header

    canvas.setFont(
        "Helvetica-Bold",
        10
    )

    canvas.drawString(
        50,
        760,
        "Healthcare Patient Registration System"
    )


    # Footer

    canvas.setFont(
        "Helvetica",
        8
    )

    canvas.drawString(
        50,
        30,
        "CONFIDENTIAL - Patient Information"
    )


    canvas.drawRightString(
        550,
        30,
        f"Page {doc.page}"
    )


    canvas.restoreState()

def format_datetime(value):
    if value is None:
        return ""

    try:
        return value.strftime("%Y-%m-%d %H:%M")
    except AttributeError:
        return str(value)[:16]

def export_patient_report(
    patient,
    appointments,
    referrals,
    lab_results,
    documents
):

    filename = filedialog.asksaveasfilename(

        defaultextension=".pdf",

        filetypes=[
            ("PDF Files", "*.pdf")
        ],

        initialfile=f"{patient.first_name}_{patient.last_name}_Report.pdf"

    )

    if filename == "":
        return

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(
        filename,
        pagesize = letter
    )

    story = []

    #
    # Title
    #

    story.append(
        Paragraph(
            "<b>Healthcare Patient Registration System</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    #
    # Patient Information
    #

    patient_data = [

        ["Field", "Information"],

        [
            "Name",
            f"{patient.first_name} {patient.last_name}"
        ],

        [
            "Date of Birth",
            str(patient.date_of_birth)
        ],

        [
            "Health Card",
            patient.health_card_number
        ],

        [
            "Phone",
            patient.phone
        ],

        [
            "Email",
            patient.email
        ],

        [
            "Doctor",
            patient.family_doctor
        ],

        [
            "Blood Type",
            patient.blood_type
        ],

        [
            "Allergies",
            patient.allergies
        ]

    ]


    patient_table = Table(
        patient_data,
        colWidths=[
            120,
            300
        ],
        repeatRows=1
    )

    patient_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])
    )


    story.append(
        patient_table
    )
    story.append(Spacer(1, 20))

    
    #
    # Appointments
    #

    story.append(
        Paragraph(
            "<b>Appointments</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Spacer(1,10)
    )


    appointment_data = [

        [
            "Date",
            "Time",
            "Reason",
            "Status"
        ]

    ]


    if appointments:

        for appt in appointments:

            appointment_data.append(

                [
                    format_datetime(str(appt.appointment_date)),
                    format_datetime(str(appt.appointment_time)),
                    appt.appointment_reason,
                    appt.appointment_status
                ]

            )

    else:

        appointment_data.append(
            [
                "None",
                "",
                "",
                ""
            ]
        )



    appointment_table = Table(
        appointment_data,
        colWidths=[
            90,
            80,
            200,
            100
        ],
        repeatRows=1
    )


    appointment_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])
    )


    story.append(
        appointment_table
    )


    story.append(
        Spacer(1,20)
    )
    

    #
    # Referrals
    #

    story.append(
        Paragraph(
            "<b>Referrals</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Spacer(1,10)
    )


    referral_data = [

        [
            "Date",
            "Clinic",
            "Department",
            "Status"
        ]

    ]


    if referrals:

        for referral in referrals:

            referral_data.append(

                [
                    format_datetime(str(referral.referral_date)),
                    referral.referring_clinic,
                    referral.department_name,
                    referral.status
                ]

            )


    else:

        referral_data.append(
            [
                "None",
                "",
                "",
                ""
            ]
        )



    referral_table = Table(
        referral_data,
        colWidths=[
            90,
            170,
            120,
            80
        ],
        repeatRows=1
    )


    referral_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])
    )


    story.append(
        referral_table
    )


    story.append(
        Spacer(1,20)
    )

    #
    # Lab Results
    #

    story.append(
        Paragraph(
            "<b>Lab Results</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Spacer(1,10)
    )


    lab_data = [

        [
            "Date",
            "Test",
            "Result",
            "Notes"
        ]

    ]


    if lab_results:

        for lab in lab_results:

            lab_data.append(

                [
                    format_datetime(str(lab.test_date)),
                    lab.test_name,
                    lab.result,
                    lab.notes
                ]

            )


    else:

        lab_data.append(
            [
                "None",
                "",
                "",
                ""
            ]
        )



    lab_table = Table(
        lab_data,
        colWidths=[
            90,
            140,
            100,
            170
        ],
        repeatRows=1
    )


    lab_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])
    )


    story.append(
        lab_table
    )


    story.append(
        Spacer(1,20)
    )

    #
    # Documents
    #

    story.append(
        Paragraph(
            "<b>Documents</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Spacer(1,10)
    )


    document_data = [

        [
            "Type",
            "File Name",
            "Upload Date"
        ]

    ]


    if documents:

        for doc in documents:

            document_data.append(

                [
                    doc.document_type,
                    doc.file_name,
                    format_datetime(str(doc.upload_date))
                ]

            )


    else:

        document_data.append(
            [
                "None",
                "",
                ""
            ]
        )



    document_table = Table(
        document_data,
        colWidths=[
            120,
            220,
            120
        ],
        repeatRows=1
    )

    document_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])
    )


    story.append(
        document_table
    )

    pdf.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    messagebox.showinfo(
        "Export Complete",
        "Patient report exported successfully."
    )