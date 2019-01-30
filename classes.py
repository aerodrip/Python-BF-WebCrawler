class Studio:
    def __init__(self, id, Title, locationObj, _work_hours):
        self.id = id
        self.Title = Title
        self.locationObj = locationObj
        self._work_hours = _work_hours

    def getWorkHours(self):
        return self._work_hours

    def getTest(self):
        print(str(self._work_hours))

    def getBeschreibung(self):
        print("ID:              " + str(self.id))
        print("Title:           " + self.Title)
        self.locationObj.getBeschreibung()
        print("Opening Hours:   " + self._work_hours)

        # studio_id:int
        # name: string
        # address_id: int
        # telNr: string



class Address:
    def __init__(self, address_id, street, number, plz, ort, country):
        self.address_id = int(address_id)
        self.street = str(street)
        self.number = str(number)
        self.plzOrt = str(plz).strip()
        self.ort = str(ort).strip()
        self.country = str(country).strip()

    def getBeschreibung(self):
        print("Address:Strasse  " + self.street)
        print("        PlZ\ORT  " + str(self.plzOrt))
        print("        land     " + self.land)
