const axios = require('axios');
const https = require('https');

const config = {
    url: 'https://httpbin.org/ip',
    method: 'get',
    proxy: {
        host: '192.168.64.98',
        port: 8080,
    },
    httpsAgent: new https.Agent({
        rejectUnauthorized: false,
    }),
};

axios(config)
    .then((response) => {
        console.log('Response status:', response.status);
        console.log('Response data:', response.data);
    })
    .catch((error) => {
        console.error('Error making the request:', error.message);
    });
