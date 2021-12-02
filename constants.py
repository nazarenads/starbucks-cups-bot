HOST_STARBUCKS = 'https://pedicafe.com.ar/'
STORES = [
    {
        "name": 'Alto Palermo',
        "url": f"{HOST_STARBUCKS}starbucks_alto_palermo_32499?category=304"
    },
    {
        "name": 'Abasto',
        "url": f"{HOST_STARBUCKS}/starbucks_abasto_ii_40067?category=1143"
    },
    {
        "name": 'DOT',
        "url": f'{HOST_STARBUCKS}/starbucks_dot_pb_40006?category=1143'
    },
    {
        "name": "Alto Avellaneda",
        "url": f"{HOST_STARBUCKS}/starbucks_alto_avellaneda_40012?category=1143"
    }
]

MESSAGE_TITLE = "Tazas disponibles en sucursal {store_name}: \n"

XPATH_PRODUCTS_CONTAINER = '//*[@id="web-view"]/ui-view/div[1]/div[1]/div[' \
                          '1]/div[2]/div[2]/div[1]'

TELEGRAM_BOT_API_HOST = 'https://api.telegram.org/bot'

TELEGRAM_BOT_API_SEND_MESSAGE_URL = 'https://api.telegram.org/bot{api_token}' \
                                    '/sendMessage?chat_id={chat_id}&parse_mo' \
                                    'de=Markdown&text={text}'