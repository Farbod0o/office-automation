

class Property:
    def __init__(self,property_code,group_code,property_name,property_description,label_code,
                 count,property_price,delivery_data,section_code,personal_code_delivery
                 ,image,status):

        self._property_code = property_code
        self._group_code = group_code
        self._property_name = property_name
        self._property_description = property_description
        self._label_code = label_code
        self._count = count
        self._property_price = property_price
        self._delivery_data = delivery_data
        self._section_code = section_code
        self._personal_code_delivery = personal_code_delivery
        self._image = image
        self._status = status
