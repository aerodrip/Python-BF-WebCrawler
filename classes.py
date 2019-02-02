class Studio:
    def __init__(self, id, title, address, telNr, linkUrl, imgUrl):
        self.id = id
        self.title = title
        self.address = address
        self.telNr = telNr
        self.linkUrl = linkUrl
        self.imgUrl = imgUrl

    def getBeschreibung(self):
        print("------------------------------------------------------------------------------------------------------")
        print("ID:              " + str(self.id))
        print("Titel:           " + self.title)
        print("Addresse:        " + str(self.address))
        #self.locationObj.getBeschreibung()
        print("Tel:             " + self.telNr)
        print("Homepage:        " + self.linkUrl)
        print("Image:           " + self.imgUrl)
        print("")


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

#class BufferList:

