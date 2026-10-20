from pyscript import document

def add_new(e):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    new_member = f"{fname} {lname}"
    all_members.append(new_member)
    display(all_members, target="members_display") 
    grade_7 = ('John Basco', 'Julius Gong', 'Sadie Wen', 'Mark Grayson', 'Benjamin Netanyahu')
    grade_8 = ('Khadija Lucman', 'Jibril Abdul', 'Maria Bamba', 'Zander Mira', 'Lucas Ladion')
    grade_9 = ('Georgina Gamponia', 'Rafael de Castro', 'Erich Garaza', 'Yanis Concepcion', 'Francesca Daquigan')
    grade_10 = ('Francis Fernandez', 'Cassiopeia Rigodon', 'Jarvis Joven', 'Cheree Mendoza', 'Edrian Correa')

    all_members = list(grade_7 + grade_8 + grade_9 + grade_10)

    display(list(all_members), target="members_display")