from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = "car.car"
    name = fields.Char(string='Name')
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string="Doors Number")
    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    feature_ids = fields.Many2many('car.feature', string='Features')
    total_speed = fields.Integer(string='Speed Total', compute='get_total_speed')
    status = fields.Selection([('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string='Status', default='new')
    car_sequence = fields.Char(string='Sequence')

    def set_car_to_used(self):
        self.status = 'used'

    def set_car_to_sold(self):
        self.status = 'sold'

    # random_message = fields.Char(string='Message', compute='say_hello')

    # Create Function
    @api.model
    def create(self, vals):
        # print('** create *** ')
        # if vals['name'] == 'abcd':
        #     vals['name'] = 'bmw x seven'
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result

    # Write Function
    # @api.model
    # def write(self, vals):
    #     print('** write ** ')
    #     # if vals['horse_power'] == 10:
    #     #     raise ValidationError(_('The horse power can t be greater than 10'))
    #     result = super(Car, self).write(vals)
    #     return result
    #

    # Delete Function
    # @api.model
    # def unlink(self):
    #     print('** unlink **')
    #
    #     # for rec in self :
    #     #     if rec.horse_power==5:
    #     #         raise ValidationError(_('Remove not possible  !!!!!!'))
    #
    #     return super(Car,self).unlink()

    # def say_hello(self):
    #     self.random_message = 'hello ' + self.driver_id.name

    def get_total_speed(self):
        self.total_speed = self.horse_power * 50


class Parking(models.Model):
    _name = "parking.parking"
    name = fields.Char(string='Name')
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')


class CarFeatures(models.Model):
    _name = "car.feature"

    name = fields.Char(string='Name')
    # value=fields.Char(string='Value')
