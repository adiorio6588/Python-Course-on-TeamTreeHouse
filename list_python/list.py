attendees = ["Luke", "Han", "Chewy"]
attendees.append("Leia")
attendees.extend(["C3PO", "R2D2"])
optional_invitees = ["Obi Wan", "Yoda"]
potential_attendees = attendees + optional_invitees
print("There are", len(attendees), "attending the event")


# print(attendees)
# print(optional_invitees)
# print(potential_attendees)

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To:  " + to_line)
print("Cc:  " + cc_line)