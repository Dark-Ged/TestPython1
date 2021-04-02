import requests
import json


class DealsExtractor:
    def extract(self):

        payload = {
            "filter[>ID]": "0",
            "select[0]": 'ID',
            "select[1]": 'TITLE',
            "select[2]": 'DATE_CREATE',
            "select[2]": 'COMPANY_ID'

        }
        r = requests.post('https://b24-q6xa77.bitrix24.ru/rest/1/5kwccacplmtdw0pp/crm.deal.list.json', data=payload)

        if r.status_code == 200:
            j = r.json()
            return j
        else:
            print("Error with http code: {0}".format(r.status_code))


class CompaniesExtractor:
    def extract(self):

        payload = {
            "filter[>ID]": "0",
            "select[0]": 'ID',
            "select[1]": 'TITLE'

        }
        r = requests.post('https://b24-q6xa77.bitrix24.ru/rest/1/5kwccacplmtdw0pp/crm.company.list.json', data=payload)

        if r.status_code == 200:
            j = r.json()
            return j

        else:
            print("Error with http code: {0}".format(r.status_code))


class Transformer:
    def transform(self, deal, company):

        r = []

        for dl in deal["result"]:
           for cm in company["result"]:
               if dl["COMPANY_ID"] == cm["ID"]:
                   r.append(dl["TITLE"] + " " + cm["TITLE"])
        return r

class Loader:
    def load(self, data):

        for s in data:
            print(s)


class JobRegistry:
    def __init__(self):
        self.jobs = {
            "BitrixJob": BitrixJob()
        }

    def getJob(self, name):
        return self.jobs[name]


class BitrixJob():
    def run(self):
        deals_extractor = DealsExtractor()
        companies_extractor = CompaniesExtractor()
        DealsAndCompaniesTransformer = Transformer()
        Loader1 = Loader()
        Loader1.load(DealsAndCompaniesTransformer.transform(deals_extractor.extract(), companies_extractor.extract()))



#main
JobRegistry().getJob("BitrixJob").run()