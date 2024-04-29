class SignUpRequestDto:
  email: str
  password: str
  first_name: str
  last_name: str

  def __init__(self, email, password, first_name, last_name):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
