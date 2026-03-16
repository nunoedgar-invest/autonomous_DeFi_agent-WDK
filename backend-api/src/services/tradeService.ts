let trades: any[] = []

export async function getTrades() {

    return trades
}

export async function executeTrade(trade: any) {

    trades.push(trade)

    return {
        message: "Trade executed",
        trade
    }
}
