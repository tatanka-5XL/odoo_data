from odoo import models, _
from odoo.exceptions import UserError
from ..services.ares_client import fetch_company_from_ares

class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_fetch_ares_data(self):
        for partner in self:
            print("XXXXXXX" + partner.vat + "XXXXXXXX")            
            ico = partner.vat
            if not ico:
                raise UserError(_("Zadejte prosím IČO do pole DIČ a uložte kontakt."))

            data = fetch_company_from_ares(ico)
            if not data:
                raise UserError(_("Společnost nenalezena v registru ARES."))

            partner.name = data.get("name")
            partner.street = data.get("street")
            partner.city = data.get("city")
            partner.zip = data.get("zip")
            partner.vat = data.get("vat")  # In case it's returned in ARES

            country = self.env.ref("base.cz", raise_if_not_found=False)
            if country:
                partner.country_id = country.id
