# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bank_book(models.Model):
    _name = 'bank.book'
    _description = 'Bank Book'

    date = fields.Date()
    particulars = fields.Char()
    received_from = fields.Char()
    vch_type =  fields.Char()
    transaction_type = fields.Char()
    instrument_no = fields.Char()
    instrument_date = fields.Date()
    bank_date = fields.Date()
    debit = fields.Float()
    credit = fields.Float()
    is_reconciled = fields.Boolean(string='is_reconciled', default=False)

class account_statement(models.Model):
    _name = 'account.statement'
    _description = 'account statement'

    date = fields.Date()
    tran_id = fields.Char()
    remarks = fields.Char()
    utr_number = fields.Char()
    instr_id = fields.Char()
    withdrawals = fields.Float()
    deposit = fields.Float()
    balance = fields.Float()
    is_reconciled = fields.Boolean(string='is_reconciled',default=False)


class reconciled_entries(models.Model):
    _name="reconciled.entries"
    _description = "Reconciled Entries"

    statement_id = fields.Many2one('account.statement', string="Statement")
    statement_remarks = fields.Char('Remarks', related = 'statement_id.remarks')
    statement_withdrawls = fields.Float('Statement Withdrawls', related = 'statement_id.withdrawals')
    bank_book_id = fields.Many2one('bank.book', string='Bank Book')
    bank_book_particulars = fields.Char('Particulars', related='bank_book_id.particulars')
    bank_book_credit = fields.Float('Bank Book Credit', related='bank_book_id.credit')
    bank_book_debit = fields.Float('Bank Book Debit', related='bank_book_id.debit')

    def run_reconciliation(self):
        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid,account_statement.date as asdate
          FROM account_statement 
          JOIN bank_book 
            ON instr_id LIKE CONCAT('%',instrument_no,'%')
           AND instr_id !=''
           AND instrument_no !=''
           AND account_statement.is_reconciled = False
           AND bank_book.is_reconciled = False;"""
        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")

        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid, account_statement.date as asdate
          FROM account_statement 
          JOIN bank_book 
            ON remarks LIKE CONCAT('%',instrument_no,'%')
           AND instrument_no is not null
           AND instrument_no != 'NEFT'
           AND (deposit = debit OR withdrawals = credit)
           AND account_statement.is_reconciled = False 
           AND bank_book.is_reconciled = False;
        """

        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")

        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid,instr_id,instrument_no, account_statement.date as asdate
          FROM account_statement 
          JOIN bank_book 
            ON remarks LIKE CONCAT('%',particulars,'%')
           AND instr_id !=''
           AND instrument_no !=''
           AND account_statement.is_reconciled = False
           AND bank_book.is_reconciled = False
        """
        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")
        
        # INDIVIDUAL STATEMENTS
        # Amount: 59
        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid,credit,debit, account_statement.date as asdate
          FROM bank_book,account_statement
         WHERE bank_book.date = account_statement.date
           AND bank_book.particulars ilike '%bank charges%'
           AND (bank_book.credit = account_statement.withdrawals)
           AND withdrawals = 59
        """
        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")
        
        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid, account_statement.date as asdate
          FROM bank_book,account_statement
         WHERE bank_book.date = account_statement.date 
           AND LOWER(TRIM(bank_book.transaction_type)) = 'cash'
           AND LOWER(TRIM(account_statement.remarks)) = 'by cash'
           AND (bank_book.debit = account_statement.deposit)
           AND account_statement.is_reconciled = False
           AND bank_book.is_reconciled = False"""
        
        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")
        
        
        query = """
        SELECT bank_book.id as bbid, account_statement.id as asid, account_statement.date as asdate 
        FROM account_statement,bank_book 
       WHERE remarks iLIKE concat('%By INST ',TRIM(leading '0' from instrument_no),' :%')
         AND instrument_no is not null
         AND (bank_book.debit = account_statement.deposit)
         AND account_statement.is_reconciled = False
         AND bank_book.is_reconciled = False"""
        
        self.env.cr.execute(query)
        resultant_records = self.env.cr.dictfetchall()
        for x in resultant_records:
            self.env.cr.execute(f"update bank_book set is_reconciled='t', bank_date='{x.get('asdate')}' where id={x.get('bbid')}")
            self.env.cr.execute(f"update account_statement set is_reconciled='t' where id={x.get('asid')}")
            self.env.cr.execute(f"insert into reconciled_entries(bank_book_id,statement_id) values({x.get('bbid')}, {x.get('asid')})")
