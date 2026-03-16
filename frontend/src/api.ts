const API_BASE = "http://localhost:3001/api"

export async function getAgentStatus() {

    const res = await fetch(`${API_BASE}/agent/status`)
    return res.json()

}

export async function startAgent() {

    const res = await fetch(`${API_BASE}/agent/start`, {
        method: "POST"
    })

    return res.json()

}

export async function stopAgent() {

    const res = await fetch(`${API_BASE}/agent/stop`, {
        method: "POST"
    })

    return res.json()

}

export async function getWallet() {

    const res = await fetch(`${API_BASE}/wallet`)
    return res.json()

}

export async function getTrades() {

    const res = await fetch(`${API_BASE}/trades`)
    return res.json()

}

export async function executeTrade(trade: any) {

    const res = await fetch(`${API_BASE}/trades/execute`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(trade)
    })

    return res.json()

}
