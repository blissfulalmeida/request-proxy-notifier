# Setting up bot to send message to the channel

1. Create bot via @botfather (suppose the id is `7514011991:AAF-8dzHVIISowicdAF26zJJriImb3S8Uf1`)
1. Create a public group (suppose the name is `@some_group`)
1. Send a request `curl "https://api.telegram.org/bot{BOT_ID}/sendMessage?chat_id={GROUP_NAME}&text=123"`
Example: `curl "https://api.telegram.org/bot7514011991:AAF-8dzHVIISowicdAF26zJJriImb3S8Uf1/sendMessage?chat_id=@some_group&text=123"`
1. In the response get the id of the channel like: `-1002292296247`
1. Send a request `curl "https://api.telegram.org/bot{BOT_ID}/sendMessage?chat_id={GROUP_ID}&text=123"`
Example: `curl "https://api.telegram.org/bot7514011991:AAF-8dzHVIISowicdAF26zJJriImb3S8Uf1/sendMessage?chat_id=-1002292296247&text=123"`
1. Make the cahnnel private
1. Send previous request to verify
