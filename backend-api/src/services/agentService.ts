export async function getAgentStatus() {

    return {
        status: "running",
        strategies_loaded: 3
    }
}

export async function startAgent() {

    return {
        message: "Agent started"
    }
}

export async function stopAgent() {

    return {
        message: "Agent stopped"
    }
}
