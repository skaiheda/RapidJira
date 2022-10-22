#It is main script where we call methods and process the data.
#Script to automate vulnerability remediation check in Rapid7 Nexpose and change the status of related JIRA ticket issues.

from setup import *
from data import *

start_Time=time.time()
# Enter JIRA ticket ID range and simply iterate the data from jira requests.
print("Enter first ticket id number: ")
x = int(input())
print("Enter last ticket id number: ")
y = int(input())
all_Ip_List = []
dict_ticket = {}

for num in range(x,y+1):
    ticketUrl = 'https://jira-support.kapitalbank.az/rest/api/2/issue/NEX-{}'.format(num)
    # result type is tuple
    result = extractFromJira(ticketUrl)
    # error => NoneType’ object is not subscriptable(indexable)
    try:
        ipList = extractIpAddress(result[2])
        all_Ip_List = all_Ip_List + ipList
        dict_ticket[result[0]] = result[1]
    except TypeError as err:
        print(err)

# remove duplicates in the all ip address list & create dictionary of tickets
print("Ticket List: ",dict_ticket)
l = list(dict.fromkeys(all_Ip_List))
# time complexity - O(n) => O(low n) : in list_updated => in range(len(list_updated))
# enumeration - for list items, range(len) - for index
a = [findAssetId(l[i]) for i in range(len(l))]
print("Script took", time.time() - start_Time, "to run")

