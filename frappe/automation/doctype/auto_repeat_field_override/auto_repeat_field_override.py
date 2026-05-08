# Copyright (c) 2026, Frappe Technologies and contributors
# License: MIT. See LICENSE

from frappe.model.document import Document


class AutoRepeatFieldOverride(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		field: DF.Literal[None]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		value: DF.SmallText | None
	# end: auto-generated types

	pass
