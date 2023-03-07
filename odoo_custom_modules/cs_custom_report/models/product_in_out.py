# Copyright 2021 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models, api


# from odoo.addons import decimal_precision as dp


class StockMove(models.Model):
    _inherit = 'stock.move'

    stock_in_out_difference_quantity = fields.Float('My Quantity', compute='_compute_stock_in_out_difference_quantity',
                                                    default=1.0, required=True, digits=0, readonly=True,
                                                    precompute=False, compute_sudo=False, store=True,
                                                    group_operator='sum',
                                                    help='Quantity in the default UoM of the product'
                                                    )
    stock_in_quantity = fields.Float('Stock IN Quantity', compute='_compute_stock_in_out_difference_quantity',
                                     default=1.0, required=True, digits=0, readonly=True,
                                     precompute=False, compute_sudo=False, store=True,
                                     group_operator='sum',
                                     help='Quantity in the default UoM of the product'
                                     )

    stock_out_quantity = fields.Float('Stock Out Quantity', compute='_compute_stock_in_out_difference_quantity',
                                      default=1.0, required=True, digits=0, readonly=True,
                                      precompute=False, compute_sudo=False, store=True,
                                      group_operator='sum',
                                      help='Quantity in the default UoM of the product'
                                      )

    internal_in_quantity = fields.Float('Internal IN Quantity', compute='_compute_stock_internal_in_quantity',
                                        default=1.0, required=True, digits=0, readonly=True,
                                        precompute=False, compute_sudo=False, store=True,
                                        group_operator='sum',
                                        help='Quantity in the default UoM of the product'
                                        )

    # internal_out_quantity = fields.Float('Internal Out Quantity', compute='_compute_stock_internal_out_quantity',
    #                                      default=1.0, required=True, digits=0, readonly=True,
    #                                      precompute=False, compute_sudo=False, store=True,
    #                                      group_operator='sum',
    #                                      help='Quantity in the default UoM of the product'
    #                                      )

    @api.depends('product_uom_qty', 'location_id', 'location_id.usage')
    def _compute_stock_in_out_difference_quantity(self):
        for move in self.filtered(
                lambda x: x.product_uom_qty and x.location_id
        ):
            if (move.location_usage in ('internal', 'transit')) and (
                    move.location_dest_usage not in ('internal', 'transit')):
                move.stock_in_out_difference_quantity = (move.product_uom_qty * -1)
                move.stock_in_quantity = 0
                move.stock_out_quantity = move.product_uom_qty
            else:
                move.stock_in_out_difference_quantity = (move.product_uom_qty * 1)
                move.stock_in_quantity = move.product_uom_qty
                move.stock_out_quantity = 0


    @api.depends('product_uom_qty', 'location_id', 'location_id.usage')
    def _compute_stock_internal_in_quantity(self):
        for move in self.filtered(
                lambda x: x.product_uom_qty and x.location_id
        ):
            if move.location_usage in 'internal':
                move.internal_in_quantity = move.product_uom_qty
            else:
                move.internal_in_quantity = 0

    # @api.depends('product_uom_qty', 'location_id', 'location_id.usage')
    # def _compute_stock_internal_out_quantity(self):
    #     for move in self.filtered(
    #             lambda x: x.product_uom_qty and x.location_id
    #     ):
    #         if self.location_dest_usage in 'internal':
    #             move.internal_out_quantity = move.product_uom_qty
    #         else:
    #             move.internal_out_quantity = 0
