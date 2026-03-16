import express from "express"
import cors from "cors"

const app = express()

app.use(cors())
app.use(express.json())

app.get("/api/status", async (req, res) => {
    res.json({
        agent: "running",
        network: "Ethereum",
        strategies_loaded: 3
    })
})

app.get("/api/wallet", async (req, res) => {
    res.json({
        address: "0xAgentWallet",
        balance: 1.52
    })
})

app.get("/api/trades", async (req, res) => {
    res.json({
        trades: []
    })
})

app.post("/api/agent/start", async (req, res) => {
    res.json({ message: "Agent started" })
})

app.post("/api/agent/stop", async (req, res) => {
    res.json({ message: "Agent stopped" })
})

app.listen(3001, () => {
    console.log("Agent API running on port 3001")
})
