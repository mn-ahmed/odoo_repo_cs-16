# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    # action_merge_records
    def action_merge_records(self):   
        init_record_partner_id = self[0].partner_id.id
        init_record_state = self[0].state

        order_lines, prepare_product = [], {}
        for record in self:
            if record.partner_id.id != init_record_partner_id:
                raise UserError(_("You can't merge records with different partners."))
            elif record.state != init_record_state:
                raise UserError(_("You can't merge records with different states."))
            else:
                order_lines += record.order_line
        dis_average = 1
        for line in order_lines:
            if not line.tax_id or not line.product_id.default_code:
                raise UserError(_("You can't merge records with product that dont have taxes or Internal Reference set."))
            if line.product_id.default_code in prepare_product:
                prepare_product[line.product_id.default_code]['qte'] += line.product_uom_qty
                prepare_product[line.product_id.default_code]['unit_price'] += line.price_unit
                prepare_product[line.product_id.default_code]['dis_average'] += 1
                prepare_product[line.product_id.default_code]['discount'] += line.discount
                prepare_product[line.product_id.default_code]['price_subtotal'] += line.price_subtotal
            else:
                prepare_product[line.product_id.default_code] = {
                    'default_code': line.product_id.default_code,
                    'name': line.name,
                    'qte': line.product_uom_qty,
                    'unit_price': line.price_unit,
                    'tax_id': list(line.tax_id.ids),
                    'price_subtotal': line.price_subtotal,
                    'discount': line.discount,
                    'dis_average': dis_average,
                }

        new_so = {'name':'New', 'partner_id': init_record_partner_id, 'state': init_record_state}
        sale_order = super(SaleOrder, self).create(new_so)

        merge_sale_order_lines = []
        for default_code, infor in prepare_product.items():
            if product_id := self.env['product.product'].search(
                [('default_code', '=', default_code)]
            ):
                merge_sale_order_lines.append({
                    'product_id': product_id.id,
                    'order_id': sale_order.id,
                    'name': infor['name'],
                    'product_uom_qty': infor['qte'],
                    'price_unit': infor['unit_price']/infor['dis_average'],
                    'discount': infor['discount']/infor['dis_average'],
                    'price_subtotal': infor['price_subtotal'],
                    'tax_id': [(6, 0, [line.tax_id.id])]
                })


        self.env['sale.order.line'].create(merge_sale_order_lines)

        message_body = """
        Merged sale order created from:
        """
        for record in self:
            message_body += f"""<a href=# data-oe-model=sale.order data-oe-id={record.id}>{record.name}</a>, """
            cancel_message = f""" Record Cancelled as it is merged with <a href=# data-oe-model=sale.order data-oe-id={sale_order.id}>{sale_order.name}</a>"""
            record.message_post(body=cancel_message)
            record.state="cancel"

        sale_order.message_post(body=message_body)
        return {
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'sale.order',
        'res_id': sale_order.id,
        'type': 'ir.actions.act_window',
        'target': 'popup',
        }
