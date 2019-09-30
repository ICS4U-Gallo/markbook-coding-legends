from data_managment_methods import initialize_session
from user_interface_center import user_interface_controller

#Run initialization functions, reading, writing, or removing class files.
session_data, filename = initialize_session()

#Initialize the user input controller class, with the current classroom json data, and it's corrosponding file name.
usr_interface = user_interface_controller(session_data, filename)

msg = "\nNow interacting with %s, enter \"help\" for the list of commands\n" % (session_data["course_code"])
print(msg)

#An infinite while loop for the user interaction session
while True:

	user_input = input("\n")

	user_input = user_input.lower()
	
	#If the user enters "exit", then save the data and break from the loop.
	if user_input == "exit":
		usr_interface.update("save")
		break
	
	#Use the user_interface's update function to fufill user request.
	usr_interface.update(user_input)
