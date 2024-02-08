from odoo import models, fields


gender_selection = [('male', 'Male'), ('female', 'Female')]

class DigizillaUser(models.Model):
    _name = 'digizilla.user'
    _description = 'Digizilla Model'
    _inherit = ['mail.thread'] # Enable the track of changes on the model by extending the mail.thread model
    _track = True

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection(gender_selection, string='Gender', tracking=True)
    country = fields.Many2one('res.country', string='Country', tracking=True)
    joining_date = fields.Date(string='Joining date', tracking=True)
    tags = fields.Char(string='Tags', tracking=True)
    customers = fields.Many2many('res.partner', string='Customers', tracking=True)
    company = fields.Many2one('res.company', string='Company', required=True, tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    comments = fields.Char(string='Comments', tracking=True)
