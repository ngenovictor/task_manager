def show_course_list():
	courses = {'Version Control': 0, 'Agile Methodology': 0, 'Programming Logic': 0}
	return courses

def input_progress():
	progress = input("Enter course progress")
	return progress

def show_menu():
	menu = ["1. Show List of Courses.", "2. Update courses progress."]
	for m in menu:
		print (m)
	menu_selected = input("Enter choice selected: ")
	if (menu_selected == 1):
		print(show_course_list())

show_menu()





