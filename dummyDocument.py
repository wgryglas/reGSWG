class StringArrayMocup:
    def __init__(self, base_text="Some"):
        self.base = base_text

    def __getitem__(self, item):
        return "%s[%d]" % (self.base, item)


class GenericObject:
    def __init__(self):
        pass


dummy_webpage = GenericObject()
dummy_webpage.__dict__["domain_address"] = "https://www.sim-flow.com"
dummy_webpage.__dict__["documents"] = []

dummy_document = GenericObject()
dummy_document.__dict__["title"] = "Dummy Title"
dummy_document.__dict__["subtitles"] = StringArrayMocup("Dummy subtitle")
dummy_document.__dict__["local_address"] = "dummy-page"
dummy_document.__dict__["next"] = dummy_document
dummy_document.__dict__["prev"] = None#dummy_document
dummy_document.__dict__["full_address"] = "%s/%s" % (dummy_webpage.domain_address, dummy_document.local_address)