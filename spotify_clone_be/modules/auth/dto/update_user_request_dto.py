class UpdateUserRequestDto:
  email: str
  first_name: str
  last_name: str

  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
