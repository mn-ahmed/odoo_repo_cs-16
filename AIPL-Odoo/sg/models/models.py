# -*- coding: utf-8 -*-

from odoo import models, fields


class SGOrganisation(models.Model):
    _name = "sg.organisation"
    _description = "SG Organisation"
    _rec_name = "b_no"

    organisation_name = fields.Char(string="Organisation Name")
    department_name = fields.Char()
    b_no = fields.Integer()
    pc_no = fields.Integer()
    name = fields.Char()
    designation = fields.Char()
    # attendance_details = fields.One2many('sg.attendance', 'b_no')

    def print_report(self):
        result = SGOrganisation.searchByEmployee(self)
        response = {
            "data": result,
            "name": self.name,
            "designation": self.designation,
            "department_name": self.department_name,
            "organisation_name": self.organisation_name,
        }
        return self.env.ref("sg.report_attendance_details_empwise").report_action(self, data=response)

    def searchByEmployee(self):
        # employee_list = self.env.cr("select B_No, name from AIPL.SGOrganisation")
        self.env.cr.execute(
            """
                            SELECT
                    *, DATE(Timestamp), SG_ORGANISATION.B_No AS "Org-B_No"
                FROM
                    SG_ATTENDANCE
                        right JOIN
                        SG_ORGANISATION
                    ON SG_ATTENDANCE.B_No = SG_ORGANISATION.id
                    where SG_ORGANISATION.B_No = {}
                    ORDER BY DATE(SG_ATTENDANCE.Timestamp), Duty ASC;
        """.format(
                self.b_no
            )
        )
        data = self.env.cr.dictfetchall()
        # if not data:
        #     flash("No Attendance Record found", "danger")
        #     return redirect(url_for('aipl.attendance'))

        updatedList, present_list = [], []
        payload = {}
        counter = 0
        for x in data:
            try:
                diff = data[counter]["timestamp"] - data[counter + 1]["timestamp"]
                hours = diff.seconds // (60 * 60)
                mins = (diff.seconds // 60) % 60
                payload = {
                    "Method": data[counter]["method"],
                    "DutyOn": data[counter + 1]["timestamp"],
                    "DutyOff": data[counter]["timestamp"],
                    "TimeDiff": str(hours) + ":" + str(mins),
                }
                updatedList.append(payload)
                counter += 2
            except IndexError:
                pass

        payload = {
            "Organisation_Name": data[0]["organisation_name"],
            "Department_Name": data[0]["department_name"],
            "Name": data[0]["name"],
            "Designation": data[0]["designation"],
            "data": updatedList,
            "from_date": "",
            "to_date": "",
        }
        return payload


class SGAttendance(models.Model):
    _name = "sg.attendance"
    _description = "SG Attendance"
    _rec_name = "b_no"

    b_no = fields.Many2one("sg.organisation", "b_no")
    employee_name = fields.Char(related="b_no.name")
    duty = fields.Char()
    method = fields.Char()
    timestamp = fields.Datetime()


# class sg(models.Model):
#     _name = 'sg.sg'
#     _description = 'sg.sg'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
