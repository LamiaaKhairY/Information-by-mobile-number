import phonenumbers
from number import mynumber
from phonenumbers import carrier

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number=mynumber,)
print(geocoder.description_for_number(ch_number,"en"))
servece = phonenumbers.parse(number=mynumber,)
print(carrier.name_for_number(servece,"en"))


def get_canonical_form(input_data):
        """ Validate and return a canonical form to be stored in DB
        and compared against.
        Returns ``None`` if input isn't a valid phone number.
        """
        import phonenumbers

        try:
            z = phonenumbers.parse(
                input_data,
            )
            if phonenumbers.is_valid_number(z):
                return phonenumbers.format_number(
                    z, phonenumbers.PhoneNumberFormat.E164
                )
            return None
        except phonenumbers.phonenumberutil.NumberParseException:
            return None 
print(get_canonical_form(mynumber))