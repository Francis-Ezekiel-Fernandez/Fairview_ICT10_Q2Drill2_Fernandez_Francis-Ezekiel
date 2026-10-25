from pyscript import document

grade_7 = {'John Basco', 'Julius Gong', 'Sadie Wen', 'Mark Grayson', 'Benjamin Netanyahu'}
grade_8 = {'Khadija Lucman', 'Jibril Abdul', 'Maria Bamba', 'Zander Mira', 'Lucas Ladion'}
grade_9 = {'Georgina Gamponia', 'Rafael de Castro', 'Erich Garaza', 'Yanis Concepcion', 'Francesca Daquigan'}
grade_10 = {'Francis Fernandez', 'Cassiopeia Rigodon', 'Jarvis Joven', 'Cheree Mendoza', 'Edrian Correa'}
omg_old = grade_7 | grade_8 | grade_9 | grade_10
display(omg_old, target="members_display")
def add_new(e):
    firstname = document.getElementById("fname").value
    lastname = document.getElementById("lname").value
    full_name = f"{firstname} {lastname}"
    
    # Only add if the input fields are not empty
    if firstname.strip() and lastname.strip():
        add = {full_name}
        final_omg = grade_7 | grade_8 | grade_9 | grade_10 | add
        total = len(final_omg)

        document.getElementById("members_display").innerHTML = str(final_omg)