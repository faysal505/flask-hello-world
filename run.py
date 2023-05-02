from flask import Flask, render_template, request
import requests
import json




app = Flask(__name__)

@app.route("/")
@app.route("/home")
def inxex():
    return render_template("index.html")










gmailCheck_header = {
	"Authorization": "SAPISIDHASH 1683001846_f0ee0c6472c87a04e26c19b1f1009d25275e3140",
	"Cookie": "NID=511=Bm6o44A1AduglytkHSoHm447bP1HjoDY5vxRxHrspSQBuhNmIVUY0hybtxh7pOwUTPkYssCpuik62EAi-p_8pD5Rc2XXmkzGkML0-crfYcLhnj7WI3lZkv0al9US1TYgvnDp0fc3uZxwPJtgIPwqSn-iGgwm3LncuwMgi8sF8QPFx8Fbk9fcfbCNvOnmfxQrPgB0M5rT4qRO2Ne1kWi3-45UT7jQX1IkMqdJZVLsNXYCYB_xwoqvoRRDSCa4M4DmNimkJ7aCVUhk-AlXA5MaZrv3bjwp7gtFWkHgBfnGkzB2gh7e7sXs5Wt4_MhIDT-5qP7DKw; SEARCH_SAMESITE=CgQIlpgB; 1P_JAR=2023-05-02-04; AEC=AUEFqZf620gSAiACt9hnvDBpdxGjM8uuzJmiV3NKRtzgOuIxkcAPa7D0l9M; ANID=AHWqTUksKZ-MTfUKg-kbQOaBm_jSr7EsR_k6VfTYHQzfoED1BwV4TDB0d4FcilLO; OGPC=19034204-1:19022622-1:; SID=WAhs_pgRiOkiunpiJoR_MESwC2Ra4PYzCHW8wvIwiv1HhZiRwuey6DdJ37HTf9tm0JXARg.; __Secure-1PSID=WAhs_pgRiOkiunpiJoR_MESwC2Ra4PYzCHW8wvIwiv1HhZiRo9OpHMTCkcQwWDOvM-7c1A.; __Secure-3PSID=WAhs_pgRiOkiunpiJoR_MESwC2Ra4PYzCHW8wvIwiv1HhZiRZ1FRLNHNVKBf0I9RB2l99Q.; HSID=AKKK7bgwZQjLzhhsC; SSID=A7_g1LjHSJnkZVURw; APISID=F89dbfHpDqHqyK7V/AXPS50MM4uK7Rxu9a; SAPISID=RAM_xgJlwJeskD5j/AwZWerfO_qp4Ibssr; __Secure-1PAPISID=RAM_xgJlwJeskD5j/AwZWerfO_qp4Ibssr; __Secure-3PAPISID=RAM_xgJlwJeskD5j/AwZWerfO_qp4Ibssr; SIDCC=AP8dLtxHRdZnEiWI1sZVlG_pi9GRYyc6x_HQahYF4EMI3ZfwG3E7Hn7LrL7SsGoRgrfumBG3Gg; __Secure-1PSIDCC=AP8dLty9G93EtdrsNrZQ16dLTmAynGqE-3WJjop0hGwMFUyw5h-VHpQDrUPjTg2JmTAPL6qP9w; __Secure-3PSIDCC=AP8dLtzQoixwWWTx_yScmd7Gg5GYJenvEB-2TfYxFobqLMD1mcE6yCUzhuJ6epl9utlXQmpyJ5c",
	"X-Goog-Api-Key": "AIzaSyC4JjdyoZPBZbhiXypJRsdhGicms9lgzoA",
	"Content-Type": "application/json+protobuf",
	"Origin": "https://docs.google.com",
}

@app.route("/check", methods=['POST'])
def check():
    Gmails = request.form['gmlist']
    GmailList =Gmails.split("\n")
    GmailFrshList = []
    for gmail in GmailList:
        fresh = gmail.replace("\r", "")
        GmailFrshList.append(fresh)
    gmailResult = []
    for gmail in GmailFrshList:
        gmailForm = [
            58,
            [
                1
            ],
            [
                [
                    gmail
                ]
            ]
        ]

        url = "https://peoplestack-pa.clients6.google.com/$rpc/peoplestack.PeopleStackAutocompleteService/Lookup"
        r = requests.post(url, data=json.dumps(gmailForm), headers=gmailCheck_header)
        if 1 in r.json()[0][0]:
            gmailResult.append(f'<td class="text-warning">{gmail}</td>')

        else:
            gmailResult.append(f'<td class="text-success">{gmail}</td>')


    return render_template("index.html", data=gmailResult, data2=GmailFrshList)


if __name__ == '__main__':
    app.run(debug=True)
