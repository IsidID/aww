import requests
import unittest
import json

import test


class TestCreateNewProfilePositive(unittest.TestCase):
    def test_login(self):
        body = {"email": "1olena.pedash@awwcor.com", "password": "Password1"}
        response = requests.post("https://a-qa-api-security.azurewebsites.net/Account/login", json=body)
        assert response.status_code == 200
        assert response.json().get('token')
        token = response.json().get('token')
        # print(response.json().get('token'))
        assert response.json().get('person') == {'dob': None,
                                                 'emailAddress': '1olena.pedash@awwcor.com',
                                                 'firstName': 'Olena',
                                                 'genderSysCodeValue': None,
                                                 'lastName': 'Pedash',
                                                 'mobilePhone': None,
                                                 'personId': None}
        assert isinstance(response.json().get('token'), str)
        return token
TestCreateNewProfilePositive()


class SwitchtoJobSeeker(unittest.TestCase):
    def test_switching(self):
        # JobseekerROLE
        token = TestCreateNewProfilePositive.test_login(str)
        data = {"employerId": None, "accountLevel": 16, "accountId": None, "returnUrl": ""}
        jobseeker = requests.put("https://a-qa-api-security.azurewebsites.net/Account/RefreshToken",
                                 headers={"Authorization": "Bearer " + token}, json=data)
        tokenjobs = jobseeker.json().get('token')
        assert jobseeker.status_code == 200

        jobseekerrole = requests.get("https://a-qa-api-security.azurewebsites.net/Account/GetAccountInfo",
                                     headers={"Authorization": "Bearer " + tokenjobs})
        assert jobseekerrole.json().get("data") == [
            {"levelName": "Admin", "levelCode": 1, "isSet": False, "companyEmployers": None},
            {"levelName": "Company", "levelCode": 2, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": "AWWCOR, INC", "employerId": None, "employerName": None,
                 "isSet": False}]}, {"levelName": "Customer", "levelCode": 4, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]}, {"levelName": "Employee", "levelCode": 8, "isSet": False, "companyEmployers": [
                {"accountId": None, "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]},
            {"levelName": "JobSeeker", "levelCode": 16, "isSet": True, "companyEmployers": None}]
        assert jobseekerrole.status_code == 200
        return tokenjobs


SwitchtoJobSeeker()


class createnewprofile(unittest.TestCase):
    def test_creation(self):
        token = SwitchtoJobSeeker.test_switching(str)
        data = {"profileId": 0, "title": "AutoTestPosition", "rate": {"rate": 45, "rateTypeSysCode": 109010},
                "languages": [{"languageNameUniqueId": 129330, "languageLevelUniqueId": 9030}],
                "skills": ["Angular.js"],
                "portfolio": "", "aboutYourself": "", "resume": "https://google.com",
                "workExperienceSysCodeUniqueID": None,
                "linkedin": None, "resumeFile": None}
        creating = requests.post("https://a-qa-api-main.azurewebsites.net/Profile/Post",
                                 headers={"Authorization": "Bearer " + token}, json=data)
        assert creating.status_code == 200
        assert creating.json().get('message') == "Added successfully"
        profile = requests.get("https://a-qa-api-main.azurewebsites.net/Profile/getListByState/true",
                               headers={"Authorization": "Bearer " + token}).json()['items'][0]['profileId']
        print(profile)
        return profile


createnewprofile()


class deactivateprofile(unittest.TestCase):
    def test_deactivate(self):

        token = SwitchtoJobSeeker.test_switching(str)
        data = createnewprofile.test_creation(int)
        disable = requests.put('https://a-qa-api-main.azurewebsites.net/Profile/Disable/' + str(data),
                               headers={"Authorization": "Bearer " + token}, json=data)
        assert disable.status_code == 200
        assert disable.json().get('message') == "Disableded Successfully"
        print(data)


deactivateprofile()
class deleteprofile(unittest.TestCase):
    def test_delete(self):
        token = SwitchtoJobSeeker.test_switching(str)
        data = createnewprofile.test_creation(int)
        delete = requests.delete('https://a-qa-api-main.azurewebsites.net/Profile/delete/' + str(data),
                                 headers={"Authorization": "Bearer " + token}, json=data)
        assert delete.status_code == 200
        assert delete.json().get('message') == "Deleted successfully"
deleteprofile()