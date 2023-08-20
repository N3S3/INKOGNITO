// javascript:

function FindProxyForURL(url, host) {
    // List of proxies
    var proxies = [
        "proxy1.example.com:8080",
        "proxy2.example.com:8080",
        "proxy3.example.com:8080",
        "proxy4.example.com:8080",
        // ... (add more proxies as needed)
    ];

    // Generate a seed based on the current minute
    var date = new Date();
    var seed = date.getUTCFullYear() * 525600 + date.getUTCMonth() * 43200 + date.getUTCDate() * 1440 + date.getUTCHours() * 60 + date.getUTCMinutes();

    // Seeded random function
    function seededRandom() {
        var x = Math.sin(seed++) * 10000;
        return x - Math.floor(x);
    }

    // Randomly select 3 distinct proxies
    var selectedProxies = [];
    while (selectedProxies.length < 3) {
        var randomIndex = Math.floor(seededRandom() * proxies.length);
        if (selectedProxies.indexOf(proxies[randomIndex]) === -1) {
            selectedProxies.push(proxies[randomIndex]);
        }
    }

    // Construct the proxy chain
    var proxyConfig = "PROXY " + selectedProxies.join("; PROXY ");

    return proxyConfig;
}
