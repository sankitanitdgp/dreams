class User:
	first_name = ''
	last_name = ''
	username = ''
	password = ''
	active = False

	def __init__(self, first_name, last_name, username, password, active=False):
		self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
		self.active = active

	# add type assertions for all placeholder params
	def update_profile(self, str_p1, str_p2, str_p3, str_p4):
		return None

	def create_list(self, str_p1, str_p2, list_p3):
		return None

	def show_lists(self):
		return None

	def view_list(self, int_p1):
		return None

	def update_list(self, str_p1, str_p2, list_p1):
		return None

	def delete_list(self, int_p1):
		return None
