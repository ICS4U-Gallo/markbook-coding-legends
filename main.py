from data_managment_methods import initialize_session
from user_interface_center import user_interface_controller

session_data, filename = initialize_session()

usr_interface = user_interface_controller(session_data, filename)

print(" \n Type \"help\" and press Enter to see command list. \n")

while True:

	user_input = input()

	user_input = user_input.lower()

	if user_input == "exit":
		usr_interface.update("save")
		break

	usr_interface.update(user_input)
