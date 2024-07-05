import http.client
import json

conn = http.client.HTTPSConnection("1vdmlx.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"213790074707"}],
            "from": "ServiceSMS",
            "text": "Congratulations on sending your first message.\nGo ahead and check the delivery report in the next step."
        }
    ]
})
headers = {
    'Authorization': 'App c4fea0ef887a51f1d42c512785a90192-6c9cf915-1a47-4a13-968f-cd2b74ab7e63',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))