# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo51y(models.Model):
     _name = 'odoo51y.modelo51y'
     _description = 'model modelo51y'

     name = fields.Char('ID', required=True)
     titulo = fields.Char(String = 'titulo', required = True)
     autor = fields.Many2many('odoo51y.autores51y', string='Autor')#autores manytomany
     editorial= fields.Many2one('odoo51y.editoriales51y', string='Editorial')#editoriales manytoone
     genero = fields.Many2many('odoo51y.generos', string='Género')#generos manytomany
     premios= fields.Many2many('odoo51y.librospremiados', string='Premios')#libros premiados many to many
     precio= fields.Many2one('odoo51y.librospago', string='Precio')#libros pago many to one
     gratis= fields.Many2one('odoo51y.librosgratis', string='Gratis')#libros gratis many to one
     popular= fields.Many2many('odoo51y.librosvendidos', string='Popular')#libros mas vendidos many to many
     saga= fields.Many2one('odoo51y.sagas', string='Saga')#sagas many to one
     trilogia= fields.Many2one('odoo51y.trilogias', string='Trilogia')#trilogias many to one


#2do Trimestre (Odoo)
#Segundo modelo.

class autores51y(models.Model):
     _name = 'odoo51y.autores51y'
     _description = 'model autores51y'

     #Campos
     name = fields.Char('ID', required = True)
     nombre = fields.Char(String = 'nombre', required = True)
     pais_Nacimiento = fields.Char(String = 'pais nacimiento')
     libro = fields.Many2many('odoo51y.modelo51y', 'autor', string='Libro')

#Tercer modelo
class editoriales51y(models.Model):
     _name = 'odoo51y.editoriales51y'
     _description = 'model editoriales51y'

     #Campos
     name = fields.Char('ID', required=True)
     nombre = fields.Char(String='nombre', required=True)
     fundador = fields.Char(String='fundador', required = True)
     pais = fields.Char(String='pais')
     libro = fields.One2many('odoo51y.modelo51y', 'editorial', string='Libro')#libro many to one

#9 modelos con relaciones

class librospremiados(models.Model):
     _name='odoo51y.librospremiados'
     _descripcion = 'model librospremiados'

     #Campos
     name = fields.Char('ID', required = True)
     nombre_premio = fields.Char(String = 'nombre_premio', required = True)
     libro = fields.Many2many('odoo51y.modelo51y', 'premios', string='Libro')#libro many to many

class librosvendidos(models.Model):
     _name='odoo51y.librosvendidos'
     _descripcion = 'model librosvendidos'

     #Campos
     name = fields.Char('ID', required = True)
     anio = fields.Char(String = 'año', required = True)
     libro = fields.Many2many('odoo51y.modelo51y', 'popular', string='Libro')#libro many to many

class sagas(models.Model):
     _name='odoo51y.sagas'
     _descripcion = 'model sagas'

     #Campos
     name = fields.Char('ID', required = True)
     saga = fields.Char(String = 'saga', required = True)
     libro = fields.One2many('odoo51y.modelo51y', 'saga', string='Libro')#libro many to one

class trilogias(models.Model):
     _name='odoo51y.trilogias'
     _descripcion = 'model trilogias'

     #Campos
     name = fields.Char('ID', required = True)
     trilogia = fields.Char(String = 'trilogia', required = True)
     libro = fields.One2many('odoo51y.modelo51y', 'trilogia', string='Libro')#libro many to one

class librospago(models.Model):
     _name='odoo51y.librospago'
     _descripcion = 'model librospago'

     #Campos
     name = fields.Char('ID', required = True)
     precio = fields.Char(String = 'precio', required = True)
     libro = fields.One2many('odoo51y.modelo51y', 'precio', string='Libro')#libro many to one

class librosgratis(models.Model):
     _name='odoo51y.librosgratis'
     _descripcion = 'model librosgratis'

     #Campos
     name = fields.Char('ID', required = True)
     gratis = fields.Char(String = 'gratis', required = True)
     libro = fields.One2many('odoo51y.modelo51y', 'gratis', string='Libro')#libro many to one

class generos(models.Model):
     _name='odoo51y.generos'
     _descripcion = 'model generos'

     #Campos
     name = fields.Char('ID', required = True)
     genero = fields.Char(String = 'genero', required = True)
     libro = fields.Many2many('odoo51y.modelo51y', 'genero', string='Libro')#libro many to many
