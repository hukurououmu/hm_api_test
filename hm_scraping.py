import requests
import pandas as pd

name = []
brand = []
current_price = []
previous_price = []

for i in range(0, 759, 36):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www2.hm.com/ja_jp/sale/shopbyproductmen/view-all.html?sort=stock&image-size=small&image=stillLife&offset=0&page-size=72',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    params = {
        'sort': 'stock',
        'image-size': 'small',
        'image': 'stillLife',
        'offset': '0',
        'page-size': '36',
    }

    response = requests.get('https://www2.hm.com/ja_jp/sale/shopbyproductmen/view-all/_jcr_content/main/productlisting_9436.display.json',
                            params=params, headers=headers)

    json_obj = response.json()
    result_items = json_obj["products"]

    for result in result_items:
        name.append(result["title"])
        brand.append(result["brandName"])
        current_price.append(result["redPrice"])
        previous_price.append(result["price"])

df_hm = pd.DataFrame({"Name": name, "Brand": brand, "Current Price": current_price,
                      "Previous Price": previous_price})
df_hm.to_excel("hm.xlsx", index=False)
