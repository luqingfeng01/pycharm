import  requests,json

url = "http://120.78.181.36:8081/ext/api/collection/submit-relief"
header ={"Content-Type":"application/json; charset=UTF-8","OPERATOR":"kredito"}
# 按费用项目减免
data1 =  {

        "userId": 206,
        "penaltyAmount": 150000,
        "overdueInterestAmount": 150000,
        "coverChargeAmount": 150000,
        "interestAmount": 150000,
        "discountAmount": 200000,
        "discountReason": "test",
        "remark": "test",
        "validityPeriod": 1546545111,
        "operator": "kredito"

}
# 自定义减免
data2={
 "userId": 206,
 "discountAmount": 200000,
 "remark":"test",
 "operator":"kredito"
}
r = requests.post(url=url,headers= header,data=json.dumps(data1))
print(r.json())