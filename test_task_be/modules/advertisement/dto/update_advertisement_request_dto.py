class UpdateAdvertisementRequestDto:
  first_name: str
  last_name: str
  phone_number: str
  city: str
  description: str

  def __init__(self, first_name, last_name, phone_number, city, description):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.city = city
    self.description = description
