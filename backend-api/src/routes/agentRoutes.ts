import { Router } from "express"
import { startAgent, stopAgent, getStatus } from "../controllers/agentController"

const router = Router()

router.get("/status", getStatus)

router.post("/start", startAgent)

router.post("/stop", stopAgent)

export default router
