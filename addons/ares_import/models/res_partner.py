from odoo import models, _
from odoo.exceptions import UserError
from ..services.ares_client import fetch_company_from_ares
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_fetch_ares_data(self):
        for partner in self:
            ico = (partner.vat or "").strip().replace("CZ", "").replace(" ", "")
            if not ico.isdigit() or len(ico) != 8:
                raise UserError(_("Zadejte prosím platné IČO (8 číslic) do pole DIČ."))
            if not ico:
                raise UserError(_("Zadejte prosím IČO do pole DIČ a uložte kontakt."))

            _logger.warning(f"ARES lookup triggered with ICO: {ico}")
            data = fetch_company_from_ares(ico)
            _logger.warning(f"After running fetch_company_data_from_ares, the data received are: {data}")
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
