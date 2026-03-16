const API = "http://localhost:3001/api"

async function loadStatus() {

    const res = await fetch(`${API}/status`)
    const data = await res.json()

    const el = document.getElementById("status")

    if (el) {

        el.innerHTML = `
        Agent Status: ${data.agent} <br>
        Network: ${data.network} <br>
        Strategies: ${data.strategies_loaded}
        `
    }
}

async function loadWallet() {

    const res = await fetch(`${API}/wallet`)
    const data = await res.json()

    const el = document.getElementById("wallet")

    if (el) {

        el.innerHTML = `
        Wallet: ${data.address} <br>
        Balance: ${data.balance} ETH
        `
    }
}

async function startAgent() {

    await fetch(`${API}/agent/start`, { method: "POST" })

    loadStatus()
}

async function stopAgent() {

    await fetch(`${API}/agent/stop`, { method: "POST" })

    loadStatus()
}

document.getElementById("startAgent")?.addEventListener("click", startAgent)
document.getElementById("stopAgent")?.addEventListener("click", stopAgent)

loadStatus()
loadWallet()
