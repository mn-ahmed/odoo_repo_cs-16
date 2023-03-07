# -*- coding: utf-8 -*-

from odoo import models, fields, api


class day_wise(models.TransientModel):
    _name = "sg.daily.report"
    _description = "sg.day_wise"

    date = fields.Date(string="Date")

    def action_print_report(self):
        # srch = '2021-03-12'
        result = day_wise.search_daywise_attendance(self)
        department_list = self.env.cr.execute(""" SELECT DISTINCT department_name FROM sg_organisation;""")
        department_list = self.env.cr.dictfetchall()
        organisation_name = self.env.cr.execute(""" SELECT organisation_name FROM sg_organisation limit 1;""")
        organisation_name = self.env.cr.dictfetchall()
        data = {
            "data": result,
            "department_list": department_list,
            "date": self.date,
            "organisation_name": organisation_name[0]["organisation_name"],
        }
        return self.env.ref("sg.daily_report_action").report_action(self, data=data)

    def search_daywise_attendance(self):
        self.env.cr.execute(
            """
        SELECT *,
        DATE(TIMESTAMP),
        SG_ATTENDANCE.ID AS "SGAID",
        SG_ORGANISATION.B_NO AS "Org-B_No"
            FROM SG_ATTENDANCE
            RIGHT JOIN SG_ORGANISATION ON SG_ATTENDANCE.B_NO = SG_ORGANISATION.ID
            AND DATE(SG_ATTENDANCE.TIMESTAMP) = '{}'
            ORDER BY SG_ORGANISATION.B_NO,
        SG_ATTENDANCE.DUTY DESC;
        """.format(
                self.date
            )
        )
        data = self.env.cr.dictfetchall()

        updatedList, present_list = [], []
        for absentee in data:
            if absentee["SGAID"] is None and absentee["method"] is None:
                updatedData = {
                    "B_No": absentee["b_no"],
                    "organisation_name": absentee["organisation_name"],
                    "DutyOn": "AB",
                    "DutyOff": "AB",
                    "TimeDiff": "AB",
                    "department_name": absentee["department_name"],
                    "name": absentee["name"],
                    "designation": absentee["designation"],
                    "Method": "AB",
                    "Org-B_No": absentee["Org-B_No"],
                }
                updatedList.append(updatedData)
            else:
                present_list.append(absentee)

        counter = 1
        for _ in present_list:
            try:
                if present_list[counter]["b_no"] == present_list[counter - 1]["b_no"]:
                    diff = present_list[counter]["timestamp"] - present_list[counter - 1]["timestamp"]
                    hours = diff.seconds // (60 * 60)
                    mins = (diff.seconds // 60) % 60

                    updatedData = {
                        "b_no": present_list[counter]["b_no"],
                        "organisation_name": present_list[counter]["organisation_name"],
                        "DutyOn": present_list[counter - 1]["timestamp"],
                        "DutyOff": present_list[counter]["timestamp"],
                        "TimeDiff": str(hours) + ":" + str(mins),
                        "department_name": present_list[counter]["department_name"],
                        "name": present_list[counter]["name"],
                        "designation": present_list[counter]["designation"],
                        "Method": present_list[counter]["method"],
                        "Org-B_No": present_list[counter]["Org-B_No"],
                    }
                    updatedList.append(updatedData)
                counter = counter + 2
            except IndexError:
                pass

        data = updatedList
        updated_list_v2 = dict()
        for x in data:
            if x["department_name"] in updated_list_v2:
                updated_list_v2[x["department_name"]].append(x)
            else:
                updated_list_v2.update({x["department_name"]: []})

        # PRINTING FORMAT
        # for x, y in updated_list_v2.items():
        #     print(x)
        #     for data in y:
        #         print("                     ", data)
        sorted_dict = {k: updated_list_v2[k] for k in sorted(updated_list_v2)}
        updated_list_v2 = sorted_dict
        return updated_list_v2
