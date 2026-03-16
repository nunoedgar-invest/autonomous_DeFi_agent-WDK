export function statusComponent(status: any) {

    return `
    <div class="card">

        <h3>Agent Status</h3>

        <p>Status: ${status.status}</p>
        <p>Strategies: ${status.strategies_loaded}</p>

    </div>
    `
}
