from setup import *

id = 4646
def getSolutionData(url):
    solutionUrl = url
    response = requests.get(
        solutionUrl,
        headers=headers,
        auth=(username,password),
        verify=False
    )
    solution_data = response.json()
    solution_data = solution_data["resources"][0]["summary"]["text"]
    return

# find solution IDs for vulnerability list of given assets in Nexpose
# but only can return max 500 size json data!!!! meaning that can return only 500 available vulnerability id at max
# + you can not filter vulnerability list by severity
id = 16501

vulnUrl = '{}/assets/{}/vulnerabilities?size=500'.format(nexpose, id)
# solutionUrl = '{}/assets/{}/vulnerabilities/'.format(nexpose,id)

response = requests.get(
    vulnUrl,
    headers=headers,
    auth=(username, password),
    verify=False
)

if response.status_code == 200:
    vuln_data = response.json()
    vuln_data = vuln_data["resources"]
    for i in vuln_data:
        getSolutionData(i["links"][3]["href"])
else:
    pass

#