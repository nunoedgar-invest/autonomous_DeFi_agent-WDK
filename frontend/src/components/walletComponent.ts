export function walletComponent(wallet: any) {

    return `
    <div class="card">

        <h3>Wallet</h3>

        <p>Address: ${wallet.address}</p>
        <p>Balance: ${wallet.balance} ETH</p>

    </div>
    `
}
