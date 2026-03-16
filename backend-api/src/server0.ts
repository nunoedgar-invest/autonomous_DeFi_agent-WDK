import express from "express"
import cors from "cors"

import agentRoutes from "./routes/agentRoutes"
import walletRoutes from "./routes/walletRoutes"
import tradeRoutes from "./routes/tradeRoutes"

const app = express()

app.use(cors())
app.use(express.json())

app.use("/api/agent", agentRoutes)
app.use("/api/wallet", walletRoutes)
app.use("/api/trades", tradeRoutes)

app.listen(3001, () => {

    console.log("API running on port 3001")

})
