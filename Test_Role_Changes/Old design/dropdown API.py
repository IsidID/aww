import requests

#merge
class TestDropDown():
    def test_login(self):
        body = {"email": "1olena.pedash@awwcor.com", "password": "Password1"}
        response = requests.post("https://a-qa-api-security.azurewebsites.net/Account/login", json=body)
        assert response.status_code == 200
        assert response.json().get('token')
        token = response.json().get('token')
        assert response.json().get('person') == {'dob': None,
                                                 'emailAddress': '1olena.pedash@awwcor.com',
                                                 'firstName': 'Olena',
                                                 'genderSysCodeValue': None,
                                                 'lastName': 'Pedash',
                                                 'mobilePhone': None,
                                                 'personId': None}
        assert isinstance(response.json().get('token'), str)
        print(token, response.status_code)
        return token

    def test_adminrole(self):
        # ADMINROLE
        token = TestDropDown.test_login(str)
        data = {"employerId": "", "accountLevel": 1, "accountId": "", "returnUrl": ""}
        admin = requests.put("https://a-qa-api-security.azurewebsites.net/Account/RefreshToken",
                             headers={"Authorization": "Bearer " + token}, json=data)
        tokenadm = admin.json().get('token')
        # print(admin.text)
        assert admin.status_code == 200
        adminroledata = {"data": {"levelName": "Admin", "levelCode": 1, "isSet": "True"}}
        adminrole = requests.get("https://a-qa-api-security.azurewebsites.net/Account/GetAccountInfo",
                                 headers={"Authorization": "Bearer " + tokenadm},
                                 json=adminroledata)
        assert adminrole.status_code == 200
        print(tokenadm, adminrole.status_code)
        return tokenadm

    def test_companyrole(self):
        # CompanyROLE
        token = TestDropDown.test_adminrole(str)
        data = {"employerId": "", "accountLevel": 2, "accountId": 4, "returnUrl": ""}
        company = requests.put("https://a-qa-api-security.azurewebsites.net/Account/RefreshToken",
                               headers={"Authorization": "Bearer " + token}, json=data)
        tokencom = company.json().get('token')
        assert company.status_code == 200
        companynrole = requests.get("https://a-qa-api-security.azurewebsites.net/Account/GetAccountInfo",
                                    headers={"Authorization": "Bearer " + tokencom})
        assert companynrole.json().get('data') == [
            {"levelName": "Admin", "levelCode": 1, "isSet": False, "companyEmployers": None},
            {"levelName": "Company", "levelCode": 2, "isSet": True, "companyEmployers": [
                {"accountId": "4", "companyName": "AWWCOR, INC", "employerId": None, "employerName": None,
                 "isSet": True}]}, {"levelName": "Customer", "levelCode": 4, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]}, {"levelName": "Employee", "levelCode": 8, "isSet": False, "companyEmployers": [
                {"accountId": None, "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]},
            {"levelName": "JobSeeker", "levelCode": 16, "isSet": False, "companyEmployers": None}]
        assert companynrole.status_code == 200
        print(tokencom, companynrole.status_code)
        return tokencom

    def test_customerrole(self):
        # CUSTOMERROLE
        token = TestDropDown.test_companyrole(str)
        data = {"employerId": 3, "accountLevel": 4, "accountId": 4, "returnUrl": ""}
        customer = requests.put("https://a-qa-api-security.azurewebsites.net/Account/RefreshToken",
                                headers={"Authorization": "Bearer " + token}, json=data)
        tokencust = customer.json().get('token')
        assert customer.status_code == 200

        customerrole = requests.get("https://a-qa-api-security.azurewebsites.net/Account/GetAccountInfo",
                                    headers={"Authorization": "Bearer " + tokencust})
        assert customerrole.json().get("data") == [
            {"levelName": "Admin", "levelCode": 1, "isSet": False, "companyEmployers": None},
            {"levelName": "Company", "levelCode": 2, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": "AWWCOR, INC", "employerId": None, "employerName": None,
                 "isSet": False}]}, {"levelName": "Customer", "levelCode": 4, "isSet": True, "companyEmployers": [
                {"accountId": "4", "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": True}]}, {"levelName": "Employee", "levelCode": 8, "isSet": False, "companyEmployers": [
                {"accountId": None, "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]},
            {"levelName": "JobSeeker", "levelCode": 16, "isSet": False, "companyEmployers": None}]
        assert customerrole.status_code == 200
        print(tokencust, customer.status_code)
        return tokencust

    def test_employeerole(self):
        # EmployeeROLE
        token = TestDropDown.test_customerrole(str)
        data = {"employerId": 3, "accountLevel": 8, "accountId": None, "returnUrl": ""}
        employee = requests.put("https://a-qa-api-security.azurewebsites.net/Account/RefreshToken",
                                headers={"Authorization": "Bearer " + token}, json=data)
        tokenemplo = employee.json().get('token')
        assert employee.status_code == 200

        employeerole = requests.get("https://a-qa-api-security.azurewebsites.net/Account/GetAccountInfo",
                                    headers={"Authorization": "Bearer " + tokenemplo})
        assert employeerole.json().get("data") == [
            {"levelName": "Admin", "levelCode": 1, "isSet": False, "companyEmployers": None},
            {"levelName": "Company", "levelCode": 2, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": "AWWCOR, INC", "employerId": None, "employerName": None,
                 "isSet": False}]}, {"levelName": "Customer", "levelCode": 4, "isSet": False, "companyEmployers": [
                {"accountId": "4", "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": False}]}, {"levelName": "Employee", "levelCode": 8, "isSet": True, "companyEmployers": [
                {"accountId": None, "companyName": None, "employerId": "3", "employerName": "AWWcor FTEs",
                 "isSet": True}]},
            {"levelName": "JobSeeker", "levelCode": 16, "isSet": False, "companyEmployers": None}]
        assert employeerole.status_code == 200
        print(tokenemplo, employee.status_code)
        return tokenemplo

    def test_jobseekerrole(self):
        # JobseekerROLE
        token = TestDropDown.test_employeerole(str)
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
        print(tokenjobs, jobseeker.status_code)
        return tokenjobs


TestDropDown()
