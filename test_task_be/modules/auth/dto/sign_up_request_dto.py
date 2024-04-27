class SignUpRequestDto:
  email: str
  password: str
  first_name: str
  last_name: str
  is_provider: bool

  def __init__(self, email, password, first_name, last_name, is_provider):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.is_provider = is_provider
