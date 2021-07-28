# coding: utf-8
# @Time : 2021/3/8 8:13 AM

from loguru import logger

from glom import glom

from lxml.etree import HTML


def parse(result, rules):
    def _pack_json(result, rules):
        item = {}

        for p_rule in rules:

            if p_rule.get("$value_type") == "raw":
                if p_rule.get("$parse_method") == "json":
                    item[p_rule.get("$name")] = glom(result, p_rule.get("$parse_rule"))
                else:
                    # print(p_rule.get("$parse_rule"))
                    # result = result.xpath(p_rule.get("$parse_rule"))
                    item[p_rule.get("$name")] = result.xpath(p_rule.get("$parse_rule"))

            elif p_rule.get("$value_type") == "recursion":
                if p_rule.get("$parse_method") == "json":
                    tmp_result = glom(result, p_rule.get("$parse_rule"))
                    total_result = []
                    for per_r in tmp_result:
                        total_result.append(_pack_json(per_r, p_rule.get("$each")))
                    item[p_rule.get("$name")] = total_result
                else:
                    tmp_result = result.xpath(p_rule.get("$parse_rule"))
                    total_result = []
                    for per_r in tmp_result:
                        total_result.append(_pack_json(per_r, p_rule.get("$each")))
                    item[p_rule.get("$name")] = total_result

        return item

    def _unpack_datas(result: dict) -> list:
        if "__datas__" not in result:
            return [result]

        item_results = []
        all_item = result.pop("__datas__")

        for per_item in all_item:
            if "__datas__" in per_item:
                tmp_datas = per_item.pop("__datas__")
                for per_tmp_data in tmp_datas:
                    tmp_item = _unpack_datas(per_tmp_data)
                    for per_tmp_item in tmp_item:
                        item_results.append({**per_tmp_item, **per_item})
            else:
                item_results.append({**result, **per_item})

        return item_results

    pack_result = _pack_json(result, rules)
    logger.info(pack_result)
    return _unpack_datas(pack_result)


data = {
    "a": "a",
    "b": [
        {"c": "c1", "d": "d1"},
        {"c": "c2", "d": "d2"}]
}

rule = [
    # {
    #     "$name": "dis",
    #     "$value_type": "raw",
    #     "$parse_method": "xpath",
    #     "$parse_rule": "//div[@class='columnarDistribution']/span//text()",
    #     "$each": []
    # },
    {
        "$name": "__datas__",
        "$value_type": "recursion",
        "$parse_method": "xpath",
        "$parse_rule": "//div[@class='list-info-item']",
        "$each": [
            {
                "$name": "nickname",
                "$value_type": "raw",
                "$parse_method": "xpath",
                "$parse_rule": "string(./div/div/span/text())",
                "$each": []
            },
            # {
            #     "$name": "d",
            #     "$value_type": "raw",
            #     "$parse_method": "json",
            #     "$parse_rule": "d",
            #     "$each": []
            # }
        ]
    }
]





if __name__ == '__main__':

    cookies = "Hm_lvt_b9de64757508c82eff06065c30f71250=1617019784,1617019793; Hm_lpvt_b9de64757508c82eff06065c30f71250=1617019793; _uab_collina=161701979656018344291546; ASP.NET_SessionId=xrghh2h0j4en2gmx2oxgtghv; 73b7b7d76f5d53ed2083763fef553399=11c014ebad67002f7ad1f454a99db94fc4f4968f7bc168ffb3c4f27f4fa4b1adf335e43c82e48bab83158fb86d22d80b0e00f39dc9eedd907d0c24304d8751b8cfa163728f200e5a2fa074442b4c6cc36d8ee10153965e90070d00abb723147ba3c20fdd120393a46fc0dde09da6a7e82b17414d1a4f64aadeaf8684c4a9c822; SaveUserName=; DashBoard_RealtimeLiveRoom_SelectedTab_1000857832=live; chl=key=www.google.com.hk; Hm_lvt_876e559e9b273a58993289470c10403b=1617019797,1617070744; CurrentRank_606359=1; FEIGUA=UserId=87a648de8ed8ca31ee7e9b77f6127b88&SubUserId=ded4613cc4a00329&NickName=885e7ec5b9522412&checksum=1505d959f661&FEIGUALIMITID=f7ec0c27f6a941e7a5f60c35720f2ea9; 048cc82ea1430e95aa0c7b709666c462=11c014ebad67002f7ad1f454a99db94fc4f4968f7bc168ffb3c4f27f4fa4b1adf335e43c82e48bab83158fb86d22d80b0e00f39dc9eedd900d8885e0e6dbe3f8ddd41559bd3b291b7eb610a8b30b84c424332cce3cdfbf8ff703c1694304dfb87010397ae81527685dd83d4a46c03cc630b5a08ee0617e2c085b893fea87c6e8; Hm_lpvt_876e559e9b273a58993289470c10403b=1617089667"

    headers = {"referer": "https://dy.feigua.cn/Member",
               "cookie": cookies}

    # url = "https://dy.feigua.cn/Aweme/GetAwemeDetail"
    url = "https://dy.feigua.cn/Aweme/GetComment?uid=58867705068&awemeId=6945034582165064991&page=1&_=1617093561394"

    # post_data = {
    #     "promotionId": "62773954552500",
    #     "id": "26837",
    #     "awemeid": "6945034582165064991",
    # }

    import requests
    # res = requests.post(url, data=post_data, headers=headers)
    res = requests.get(url, headers=headers)

    # print(res.text)
    from lxml import etree

    print(res.text)
    res_html = HTML(res.text)

    # items = res_html.xpath("//dl[@class='one-info']/dt//a")

    # for per_item in items:
    #     print(per_item.xpath("string(./@href)"))

    # print(res_html.xpath("//div[@class='Distribution']/ul//li"))
    # with open("../tmp/tmp_html_data", "r") as f:
    #     resp_content = "".join(f.readlines())[15:]
    #     data = HTML(resp_content)
    #     print(data)
    # print(res.text)
    parse_result = parse(res_html, rule)
    logger.info(parse_result)


