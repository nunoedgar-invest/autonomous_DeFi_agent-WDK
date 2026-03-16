import { Router } from "express"
import { getTrades, executeTrade } from "../controllers/tradeController"

const router = Router()

router.get("/", getTrades)

router.post("/execute", executeTrade)

export default router
