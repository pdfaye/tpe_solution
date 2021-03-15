# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from ast import literal_eval

from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _name = 'tpe.accueil'

    nom_tpe = fields.Char(String='Nom de l\'entreprise')
    taille_tpe = fields.Integer(String='Nombre Employe')