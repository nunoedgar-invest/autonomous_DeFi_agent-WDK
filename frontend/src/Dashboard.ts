import * as api from "./api"

export async function renderDashboard() {

    const status = await api.getAgentStatus()
    const wallet = await api.getWallet()
    const trades = await api.getTrades()

    const statusEl = document.getElementById("status")
    const walletEl = document.getElementById("wallet")
    const tradesEl = document.getElementById("trades")

    if (statusEl) {

        statusEl.innerHTML = `
        Agent Status: ${status.status} <br>
        Strategies Loaded: ${status.strategies_loaded}
        `
    }

    if (walletEl) {

        walletEl.innerHTML = `
        Wallet Address: ${wallet.address} <br>
        Balance: ${wallet.balance} ETH
        `
    }

    if (tradesEl) {

        tradesEl.innerHTML = `
        Trades Executed: ${trades.length}
        `
    }

}
