export function tradesComponent(trades: any[]) {

    let rows = trades.map(t => {

        return `
        <li>
        ${t.type} ${t.amount} ${t.from_token} → ${t.to_token}
        </li>
        `
    }).join("")

    return `
    <div class="card">

        <h3>Trades</h3>

        <ul>
        ${rows}
        </ul>

    </div>
    `
}

