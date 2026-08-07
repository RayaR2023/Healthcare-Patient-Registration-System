import customtkinter as ctk
from tkinter import ttk


class LabResultsFrame(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        add_callback=None,
        edit_callback=None,
        delete_callback=None
    ):

        super().__init__(parent)

        self.add_callback = add_callback
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback

        self.results = []
        self.selected_lab = None


        # ==========================
        # Layout
        # ==========================

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # ==========================
        # Title
        # ==========================

        ctk.CTkLabel(
            self,
            text="Lab Results",
            font=("Segoe UI",18,"bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,5)
        )


        # ==========================
        # Buttons
        # ==========================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )


        self.add_button = ctk.CTkButton(
            button_frame,
            text="Add Lab Result",
            command=self.add_callback
        )

        self.add_button.pack(
            side="left",
            padx=5
        )


        self.edit_button = ctk.CTkButton(
            button_frame,
            text="Edit Lab Result",
            command=self.edit_callback
        )

        self.edit_button.pack(
            side="left",
            padx=5
        )


        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete Lab Result",
            command=self.delete_callback
        )

        self.delete_button.pack(
            side="left",
            padx=5
        )


        # ==========================
        # Table
        # ==========================

        table_frame = ctk.CTkFrame(self)

        table_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=20,
            pady=10
        )


        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )


        columns = (
            "ID",
            "Date",
            "Test Name",
            "Result",
            "Notes"
        )


        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )


        for column in columns:

            self.table.heading(
                column,
                text=column
            )


            self.table.column(
                column,
                anchor="center"
            )


        self.table.column(
            "ID",
            width=70
        )

        self.table.column(
            "Date",
            width=120
        )

        self.table.column(
            "Test Name",
            width=250
        )

        self.table.column(
            "Result",
            width=150
        )

        self.table.column(
            "Notes",
            width=400
        )


        self.table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )


        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )


        self.table.configure(
            yscrollcommand=scrollbar.set
        )


        self.table.bind(
            "<<TreeviewSelect>>",
            self.select_lab
        )


    # ==========================
    # Display
    # ==========================

    def display_lab_results(
        self,
        results
    ):

        self.results = results

        self.selected_lab = None


        for row in self.table.get_children():

            self.table.delete(row)



        for lab in results:

            self.table.insert(
                "",
                "end",
                iid=str(lab.result_id),
                values=(
                    lab.result_id,
                    lab.test_date,
                    lab.test_name,
                    lab.result,
                    lab.notes
                )
            )


    # ==========================
    # Select
    # ==========================

    def select_lab(self,event):

        selected = self.table.selection()


        if not selected:

            self.selected_lab = None
            return



        lab_id = int(selected[0])


        for lab in self.results:

            if lab.result_id == lab_id:

                self.selected_lab = lab


                print(
                    "Selected Lab:",
                    lab.result_id
                )


                return



    # ==========================
    # Getter
    # ==========================

    def get_selected_lab(self):

        return self.selected_lab