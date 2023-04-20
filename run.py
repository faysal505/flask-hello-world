from flask import Flask, render_template, request
import requests
import json




app = Flask(__name__)

@app.route("/")
@app.route("/home")
def inxex():
    return render_template("index.html")










gmailCheck_header = {
	"Authorization": "SAPISIDHASH 1681964510_944c0facd66c7225e009957e79edf4e7c75c54d9",
	"Cookie": "NID=511=kTFmwJ2MYVehk2H_cv4KQb2QYC8FEVzTc4R0MRcDrfx4tQYX34yFtmeqXp7_CVHEkCbbQTeHuK7T94cjh8bN4s7SHgP5F2WtG-r3qdgrcDNgTzUuvN7WEiJRoDpB5IetARvxf6i4_RApRGxhb8ZNkPMkDML1xqD-V7c9-gRrfG2GmkUSZelYAo8d-RMVZHcDpMBNDe7kR1GceF9jKg8T7JFBsuvIv8sMFSSdGFNDIVKaujx2bEnmjBgNLQOZbGqmpc3ZZ--9_ECUOxJHdtZOqjiHsBADMw; SID=VAhs_vQGQYNSXSmGninU6tBsONFBZqPo9gkIQgX3yyYz2_rvYdVDZFBFtk81LwDQ4Z4P3A.; __Secure-1PSID=VAhs_vQGQYNSXSmGninU6tBsONFBZqPo9gkIQgX3yyYz2_rvrU4Ow6FwPipyWfAW2NafDw.; __Secure-3PSID=VAhs_vQGQYNSXSmGninU6tBsONFBZqPo9gkIQgX3yyYz2_rvCv13cX7PFw-xNRGIhd1dLw.; HSID=AaU4Ugkz0gNDYlbWN; SSID=AhaJrnB_hjkgAQbT8; APISID=_yMV3vRq6ihRzFjm/AljVTIhRYyAD1_cZh; SAPISID=a8S0BejbZ9z_vYBe/AJVHM9SNXEQmJGnvL; __Secure-1PAPISID=a8S0BejbZ9z_vYBe/AJVHM9SNXEQmJGnvL; __Secure-3PAPISID=a8S0BejbZ9z_vYBe/AJVHM9SNXEQmJGnvL; SIDCC=AP8dLtxSbX0Azk9km0mOrp8tclBK3r7LqaKyiZQo58F66yEj1y9teD2wNmUusex2ytK915s3v9k; __Secure-1PSIDCC=AP8dLtzBVfvXWpNu43YpwjX1PeL7pAsRBfHWzkh5jyHrNEPkBJj6fUZrTXqBAXYH9UNEBddlMA; __Secure-3PSIDCC=AP8dLtzpmUw_o5So0IKseRBTRyO1cJFFqfCQPYXDs7mLU2IRwRqeXr0iVUSOzviBgqa5EzMPtA; SEARCH_SAMESITE=CgQI-ZcB; 1P_JAR=2023-04-18-08; AEC=AUEFqZfHUSKEwdYHPBzKnEUhYTeALJQmM9sKgJbES5J1c51Eho36R6HDU8g; ANID=AHWqTUkhC2BAiFC3-XL5TTQ8bmn9mmHRmwBrFL_laziZ-jaJZ_OrVUv6rLp_LSxv; OGPC=19034204-1:19022622-1:",
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
