def generate_invitations(template, attendees):
    # تحقق من النوع
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # تحقق من الفراغ
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # معالجة البيانات
    for i, attendee in enumerate(attendees, start=1):
        text = template

        text = text.replace("{name}", str(attendee.get("name", "N/A")))
        text = text.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        text = text.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        text = text.replace("{event_location}", str(attendee.get("event_location", "N/A")))

        # حفظ الملف
        filename = f"output_{i}.txt"
        with open(filename, "w") as file:
            file.write(text)