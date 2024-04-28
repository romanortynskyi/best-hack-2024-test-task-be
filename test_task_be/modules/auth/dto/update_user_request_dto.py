class UpdateUserRequestDto:
  email: str
  first_name: str
  last_name: str
  is_provider: bool

  def __init__(self, email, first_name, last_name, is_provider):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
    self.is_provider = is_provider
